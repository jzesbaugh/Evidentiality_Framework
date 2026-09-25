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
