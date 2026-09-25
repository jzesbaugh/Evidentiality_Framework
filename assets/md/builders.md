> Stopping hallucinations spreading between AI agents: Provenance labels that survive hand-offs between AI agents, plus a fail-closed gate that holds actions built on unchecked claims. Grammar and parser included.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/evidentiality-framework/builders.html. Text CC BY 4.0.

For builders

# Stopping hallucinations spreading between AI agents

**Who this page is for:** engineers building multi-step or multi-agent AI systems.

## What it is, technically

A system prompt ([the instructions](../../spec.html#module), about 450 words) that asks the model to wrap each claim in an inline provenance label, so in a multi-agent pipeline every hand-off carries where each claim came from. Paired with a gate, it gives you a human-in-the-loop approval point exactly where an action rests on something unchecked. There's no model change, no schema and no extra service. Because the labels are plain text inside the prose, they survive the things that strip metadata: copying, summarising, pasting into email, and handing text to another agent.

## The notation

```
claim   := open text close
open    := "(u)" | "(m)" | "(g)"
close   := "(/u" [": " note] ")" | "(/m: " source ["," date] ")" | "(/g" [": " note] ")"
          -- labels may nest, never overlap; (m) must name a source
mention := "`(g)`"   -- a label in backticks is only mentioned, not applied
```

## Parse, check, and gate

The labels only help if something reads them. The simplest useful control: before an agent takes an action, parse its reasoning and hold the action if any of it is labelled (g), **if any sentence carries no label at all**, or if the labels don't balance. It fails closed: a model that forgets to label its text doesn't get through. That also means it holds anything containing a conclusion, since a conclusion is (g); that's the point where a person or a checker should look. Pass `allow_guesses=True` where conclusions are expected. List numbers, bullets, headings and table pipes are ignored; words inside backticks still count as claims. Known limit: a lettered list written "(a) … (g)" is read as labels. `strip()` removes the labels for readers who don't want them. This file is in the [test kit](../../test-kit/marks.py) (MIT); it keeps its original name, `marks.py`, from before the site settled on "labels".

```
"""Parse evidentiality labels ((u)/(m)/(g), called "marks" in earlier versions), check they balance, and gate actions on unchecked claims. MIT licence."""
import re

# Opening (u)/(m)/(g); closing (/u), (/m: note), allowing one level of parentheses inside a note.
TOKEN = re.compile(r"`[^`\n]*`|\((u|m|g)\)|\(/(u|m|g)(?::\s*((?:[^()]|\([^()]*\))*))?\)", re.IGNORECASE)

MARK_ONLY = re.compile(r"\(/?(?:u|m|g)(?::[^)]*)?\)", re.IGNORECASE)
# List numbers, bullets, quote markers and table pipes are layout, not claims.
FORMAT = re.compile(r"^\s*(?:[-*+•]|\d+[.)]|>|\|)\s*|\s*\|\s*$")

def parse(text):
    """Return (spans, problems). Each span: dict(mark, text, note, start, end)."""
    spans, problems, stack = [], [], []
    for t in TOKEN.finditer(text):
        if t.group(0).startswith("`"):
            continue                                    # a mention in backticks, not a mark
        if t.group(1):
            stack.append((t.group(1).lower(), t.start(), t.end()))
            continue
        mark, note = t.group(2).lower(), (t.group(3) or "").strip()
        if not stack or stack[-1][0] != mark:
            problems.append(f"closing ({mark}) at {t.start()} doesn't match an open tag")
            continue
        _, outer_start, inner_start = stack.pop()
        spans.append({"mark": mark, "text": text[inner_start:t.start()].strip(), "note": note,
                      "start": outer_start, "end": t.end()})
    problems += [f"({m}) opened at {pos} never closed" for m, pos, _ in stack]
    for s in spans:
        if s["mark"] == "m" and not s["note"]:
            problems.append(f"checked claim with no source: {s['text'][:60]!r}")
    return spans, problems

def unmarked(text, spans):
    """Text outside every mark (ignoring punctuation, whitespace and backtick mentions)."""
    covered = sorted((s["start"], s["end"]) for s in spans)
    out, pos = [], 0
    for a, b in covered:
        if a > pos:
            out.append(text[pos:a])
        pos = max(pos, b)
    out.append(text[pos:])
    # A backtick mention of a mark is not a claim, but other words in backticks are.
    rest = re.sub(r"`([^`\n]*)`", lambda b: MARK_ONLY.sub(" ", b.group(1)), "".join(out))
    lines = [FORMAT.sub("", ln) for ln in rest.split("\n") if not re.match(r"\s*#{1,6}\s", ln)]  # headings are labels
    parts = [p.strip() for ln in lines for p in re.split(r"(?<=[.!?])\s+", ln)]
    return [p for p in parts if re.search(r"[A-Za-z]", p)]

def gate(text, allow_guesses=False):
    """Fail closed: allow an action only if every claim is marked, the marks balance, and nothing is (g).

    By design this holds any text containing a conclusion, because a conclusion is (g). Use it at the
    point where an action would be taken, and send held items to a person or a checker. Pass
    allow_guesses=True where conclusions are expected; guesses are then listed but don't block.
    Known limit: a lettered list written "(a) … (g)" is read as marks; use "a." or backticks instead.
    """
    spans, problems = parse(text)
    loose = unmarked(text, spans)
    if loose:
        problems.append(f"unmarked text: {loose[0][:60]!r}" + (f" (+{len(loose)-1} more)" if len(loose) > 1 else ""))
    guesses = [s["text"] for s in spans if s["mark"] == "g"]
    return {"allow": not problems and (allow_guesses or not guesses), "problems": problems, "unchecked": guesses}

def strip(text):
    """Remove the marks for a human reader who doesn't want them (keeps the words)."""
    return re.sub(r"\s{2,}", " ", TOKEN.sub(lambda t: t.group(0) if t.group(0).startswith("`") else "", text)).strip()

if __name__ == "__main__":
    demo = ("(u)Stock is 41 tonnes.(/u: warehouse manager) "
            "(m)Donations were 62 tonnes in August.(/m: donor ledger, checked Sept 20) "
            "(g)Stock lasts about 18 days.(/g)")
    print(gate(demo))
```

Running the demo prints `{'allow': False, 'problems': [], 'unchecked': ['Stock lasts about 18 days.']}`: the action is held because it depends on a guess.

## Limits you should design around

- **The instructions also include an output format.** For requests to add to or continue a document, the instructions ask for three sections (CONFLICTS / FROM THE RECORD / ADDED). It sometimes appears on other tasks too, which can break downstream parsers. Add "Answer directly; this is not an add or expand task" where you don't want it.
- **Cost not measured.** We haven't measured the extra tokens or latency.
- **The model labels its own work.** A model can put (m) on a guess. Don't trust incoming (m) labels for anything consequential; have the application or a second model apply (m) only to what it can actually verify.
- **A label you receive is a claim.** An (m) from another agent means that agent says it checked. Treat it as that.
- **Most multi-agent failures aren't about facts.** Coordination and task-following problems are more common ([Cemri et al., 2025](https://arxiv.org/abs/2503.13657)). This addresses the factual part only.
- **Check early.** In a simulated four-agent pipeline, checks at each hand-off cut planted errors that survived from 58% to 16%, and a check at the first hand-off alone caught about three quarters; checking only at the end barely helped ([Singh and Pawar, 2026](https://arxiv.org/abs/2608.14588)).

## Who already does this

Keeping "what we know" separate from "what we concluded" is old practice in fields where mistakes are costly. The framework borrows the idea, not the machinery:

- **US intelligence analysis.** The analytic standards directive, [ICD 203](https://archive.dni.gov/files/documents/ICD/ICD-203.pdf) (2015), requires that analysis "properly distinguishes between underlying intelligence information and analysts' assumptions and judgments" and "properly describes quality and credibility of underlying sources." The ship report is what happens when that line disappears.
- **Source grading.** Military and police intelligence often grade each report twice: how reliable the source is (A to F) and how credible the information is (1 to 6). It's usually called the [Admiralty code](https://en.wikipedia.org/wiki/Admiralty_code), or the NATO system.
- **Data provenance.** Standards such as [W3C PROV](https://www.w3.org/TR/prov-overview/) record where data came from and what was done to it, as metadata beside the data.

The difference here is where the record lives: inside the sentence, in plain text, so it survives being copied, summarised and handed to another AI, which is where metadata usually gets lost. One naming clash to watch: in US classification markings, "(U)" at the start of a paragraph means *unclassified*. If you work with classified material, rename the labels.
