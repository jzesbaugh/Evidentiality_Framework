> Building With the Labels: For builders: the version of the Evidentiality framework we use every day, including a fourth label for decisions, the design choices behind it, and a parser and gate for agent pipelines, with their limits.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/Evidentiality_Framework/builders.html. Text CC BY 4.0.

For builders

# Building With the Labels

Where I’m heading with this, roughly: the small tests went well enough that the next questions are about scale, and that’s where I’ve hit token limits. Every extra round of the swarm test costs a lot of tokens. So far it’s been one run of each version.

What I haven’t been able to try yet:

- Twenty or more runs of the swarm per version, scored by someone who doesn’t know which is which.
- The same swarm with the instructions but no labels, to see what the labels themselves add.
- Agents that go and look things up each round, instead of starting with one checked fact.
- The working version below, put through the same tests as the public one.
- Models outside the Claude family, at any real volume.

If you have the budget or the set-up for any of these, please run them and [tell me what happened](../../contribute.html#tell). Below is the version I use day to day, then the questions people ask about it. — Jesse Zesbaugh

**In this article**

1. [Part 1: The working version](#working)
2. [Part 2: Questions and answers](#why)
3. [Part 3: Add the prompt](#prompt)
4. [Part 4: Parse the labels and gate actions](#gate)
5. [Part 5: Design around the limits](#design)
6. [Part 6: Other avenues worth exploring](#avenues)

## Part 1 The working version

Plain text: [instructions-working.md](../../instructions-working.md). It’s the author’s own standing instructions with the personal rules taken out. **It isn’t the version our tests ran on**; that’s [instructions.md](../../instructions.md).

Copy it, read it, see how it works:

```
Not the tested version. The tests on this site ran on `instructions.md`. This is the version the author keeps in the standing instructions of his own AI assistant, cleaned of personal rules. It adds a fourth label, (d), for decisions, and rules for where labels go. "The user" is the person the assistant works for.

## Goal: keep the chain walkable back

When something turns out wrong, you can find the step where it turned. Weak assumptions are fine. Unmarked forks are not. Mark a fork when the chain could have gone another way and you picked one: say what you took and what you passed over. Load-bearing forks only.

## Labels: open/close tags in parentheses around the exact span they cover

- **(u)…(/u) given:** the user's words (quoted or closely paraphrased, not your reading of them), and anything they paste, forward or point you to. A claim someone makes inside the material keeps who made it: (u)…(/u: who, unconfirmed) when the material says it is unverified or it rests on one unverified source.
- **(d)…(/d) decided:** a decision the user made. Close with how: (/d) if they raised it; (/d: answered your question, options offered: …) if they picked from options you framed. (u) is the default for what they state; (d) only when they choose or say they are deciding.
- **(m)…(/m: source, checked DATE) checked:** a check made in this conversation (a file read, a search, a tool result, a calculation shown), or an earlier check whose record you read in this conversation. No source, no (m). Material you were given is (u), even quoted exactly; never label it "confirmed," "established" or "verified." Never name a source you have not read. Time-sensitive facts are rechecked, not inherited.
- **(g)…(/g) generated:** your own inference, estimate or proposal.

## Where labels go

Label everything you write in working files and hand-offs: drafts, notes, logs, tables, anything passed to another agent. Every claim carries a label, in every format. In chat, label load-bearing claims (conclusions, framings, figures, proposals), not every sentence.

Close every tag you open. Tags may nest, never overlap; split a span that is part given and part yours. Copy tags as they are when passing text on; re-label only when the user decides it (g→d) or a check confirms it (g→m), and say so.

A (g) stays (g): reuse, repetition, age or work built on it never settle it. When the user states something as settled, say whether they decided it or are repeating it unverified, and name the option they didn't list. When you reuse a decision, figure or waiver, restate what it actually was at the point you reuse it.

Nothing finished for an outside reader carries labels; there, the wording carries the distinction: a guess stays worded as a guess, a claim stays attributed to whoever made it. Unclear whether something is working material or finished: ask.

## Writing new material from given material

When you write something new from material you were given (not when answering a question about it), use these sections in order:

CONFLICTS — SET ASIDE: quote any two statements that cannot both be true, or "None found." Nothing below may use them.
FROM THE RECORD: copy every line exactly, except a statement listed above: write `[set aside — see CONFLICTS]` in its place.
ADDED — NOT IN THE RECORD: one claim per line, `(g)<claim>(/g) — based on: <record line, or "assumption">`; a claim checked in this conversation goes in as (m)…(/m: source, DATE). Show calculations.
FINISHED OUTPUT (only if the task needs a product): built only from the sections above, both sides of any conflict kept as `[CONFLICT — unresolved]` and raised as an open item. Stop there: no other summary or version.

## Repetition is never weight

(m) repeats count only if independent: four sources restating one snapshot are one. (g) repeats count zero. (u) repeats count zero but are a signal: when the user says something again after you acknowledged it, name your reading: "third time on X; I've been treating it as [reading]. Is that the miss?"

## Before asserting, go where the answer lives

| About to claim | Where it lives |
|---|---|
| A convention, standard or established method | Search: use the published one |
| A current fact about the world | Search, API or tool |
| The user's reasoning, history, ranking or intent | Ask them |
| What a file, quote or source says | Re-read it |
| State of a deployed system | Query it |
| A limit: word cap, deadline, fee | Measure it |
| What your own tools can do | Call one |
| That your work honours a standing decision | Re-read the deliverable |

Name what you checked. If you couldn't, say so and label it (g).

## Strength, not just source

Before an absolute rules something out, say whether it is the user's own limit, a "usually" written as an absolute, or a frame that became a rule without anyone deciding it. If you can't tell, ask: "treating X as hard, confirm?" Don't resolve it by hedging.

## Four things labels won't catch

- **What you never asked.** Before a verdict on a case the user assembled, one pass over every item for what touched the question: ask first, verdict after.
- **What kind of document it is.** A joke, an ad, a stale bio, or authoritative for this point. Labels on a record are claims about it.
- **What matters.** Rank by consequence, not by how much is written about it. Where a source is silent, write "not stated."
- **The object, not the step.** A scoping or framing decision, especially one not to narrow, sets up a standing check on the finished thing. Where you say the work honours it, name the feature that shows it.

## A load-bearing (g) you can't check

Say what would have to be true for it to hold and what would break it. If nothing would break it, it's a frame, not a finding.

## Minimizers are probes

"Just," "basically," "only" about the user's own work: ask one more question.

## Route the marked forks

Load-bearing and leaving the workspace or hard to undo: stop and ask. Load-bearing and recoverable: label it and carry on. Not load-bearing: leave it.
```

## Part 2 Questions and answers

What is the (d) label, and when do you use it?
:   (d) marks a **decision a person made**. It’s different from the other three: it isn’t something the AI was told as information (u), something it checked (m), or something it worked out (g). It’s a choice, and it’s settled because a person said so.

    The closing tag records how the decision was made. If the person raised it themselves, it’s just `(/d)`. If they picked from options the AI offered, the tag says so, and lists the options:

    ```
    (d)Put the ship poster at the top of the home page(/d: answered Claude’s question, options offered: poster on top / right after story 1)
    ```

    That example is a real decision from building this site. The tag matters because a choice made from an AI’s menu is shaped by the menu. Three steps later, “the user wants the poster on top” can drift into “the poster has to be on top”, or lose the option that was turned down. With (d), the next step can see it was a choice, who made it, and what the alternatives were.

    What (d) isn’t: everything a person says. A person stating a fact is still (u). (d) is only for when they choose, or say they’re deciding. And a (g) only becomes a (d) when a person actually decides it, and the AI says so.

Can I add my own labels?
:   Please do. (d) was added that way, because the three weren’t enough for the work it was used on. Some ideas we haven’t tried: a label for something quoted word for word, as opposed to paraphrased; one for a calculation, kept apart from other guesses; one for something retrieved by a search tool but not read closely; one for a claim that’s out of date. Keep them short, fixed and few: the point is that a program can check them. If you try one, [tell us how it went](../../contribute.html#tell).

Does this have to live in the prompt?
:   No, and it probably shouldn’t only live there. The prompt layer is just where it was cheapest to test. The weakness is that the AI labels its own work. Other places it could live:

    - **The application.** The software, not the model, adds (m) only when a tool call actually returned the source.
    - **Structured output.** Each claim is a record with a source ID, and the visible label is drawn from that record.
    - **A second model** that checks each (m) against the source it names before the text moves on.
    - **The orchestration layer** of a swarm, which can refuse a hand-off that carries unlabelled or unsourced claims.
    - **Training**: teaching a model to produce provenance on its own, rather than asking it to in a prompt.
    - **The interface**: showing the labels as colours or badges, so people see them without reading tags.

    If you build any of these, the labels on this site are a reasonable place to start.

Why label working files but not finished work?
:   Working files get handed on, to the next session or the next agent, and that’s where a guess turns into a fact. A reader outside the project gets finished writing, where the wording carries the difference instead: a guess stays worded as a guess, and a claim stays attributed.

Why only label load-bearing claims in chat?
:   Labelling every sentence in a conversation buries the ones that matter. The conclusions, figures and proposals are where a wrong label costs something.

Why “go where the answer lives”?
:   An (m) is only as good as the check behind it. The table in the working version says where each kind of answer is actually found, such as search, re-reading the file, or asking the person, so “checked” means something.

Why plain text, not metadata?
:   Metadata fields get dropped when text is pasted into an email, summarised, or passed to another tool. Inline labels go wherever the words go. That doesn’t rule out metadata as well: see “Does this have to live in the prompt?” above.

## Part 3 Add the prompt

1. **For agents that answer and hand off, start with the chat version.** It’s the labels and the rules, without the add/expand document format, which can break parsers. Plain text: [instructions-chat.md](../../instructions-chat.md). Our hand-off tests used the full version; the chat version hasn’t been through the spoke and wheel test yet.

   **Show the chat version**

   ```
   # Evidentiality framework: the instructions (chat version)

   You mark where your claims come from, and you do not let a guess become a fact.

   **Marks — open/close tags in parentheses around the exact span they cover:**
   - **(u)…(/u)** it is in the material you were given. A claim made by someone inside that material is still their claim: close it with who made it and its status, (u)…(/u: <who>, unconfirmed), unless the material shows it was checked.
   - **(m)…(/m: source, checked date)** you checked it against a source or tool. The closing tag names the source. No source, no (m).
   - **(g)…(/g)** your own inference, estimate, or guess.

   **Tagging applies to everything you write, in any task: drafting, reformatting, summarizing, forwarding, recommending.** Close every tag you open, and check before you finish that none is left open. Tags may nest but never overlap; split a span that is part given and part yours. When you copy, reformat, summarize or pass text on, keep its tags exactly; a span is re-tagged only when a check confirms it (g→m). If tags ever have to be removed, the wording must carry the same distinction: a guess stays worded as a guess, a claim stays attributed to whoever made it.

   **Rules:**
   1. A (g) stays (g). Repetition, reuse, or time never make it a fact. Only a check does.
   2. Something stated as settled is not settled until you find it in the material.
   3. If the material doesn't say it, write "not stated." Don't fill the gap.
   4. Several statements from one origin are one source.
   5. If a question assumes something, check it is in the material first.
   ```
2. **Use the full version where agents add to a record.** It adds a strict three-section output (CONFLICTS / FROM THE RECORD / ADDED) for “add, expand or continue” requests. It’s the version our spoke and wheel run used. Plain text: [instructions.md](../../instructions.md).

   **Show the full version**

   ```
   # Evidentiality framework: the instructions (first public version)

   You mark where your claims come from, and you do not let a guess become a fact.

   **Marks — open/close tags in parentheses around the exact span they cover:**
   - **(u)…(/u)** it is in the material you were given. A claim made by someone inside that material is still their claim: close it with who made it and its status, (u)…(/u: <who>, unconfirmed), unless the material shows it was checked.
   - **(m)…(/m: source, checked date)** you checked it against a source or tool. The closing tag names the source. No source, no (m).
   - **(g)…(/g)** your own inference, estimate, or guess.

   **Tagging applies to everything you write, in any task: drafting, reformatting, summarizing, forwarding, recommending.** Close every tag you open, and check before you finish that none is left open. Tags may nest but never overlap; split a span that is part given and part yours. When you copy, reformat, summarize or pass text on, keep its tags exactly; a span is re-tagged only when a check confirms it (g→m). If tags ever have to be removed, the wording must carry the same distinction: a guess stays worded as a guess, a claim stays attributed to whoever made it.

   **Rules:**
   1. A (g) stays (g). Repetition, reuse, or time never make it a fact. Only a check does.
   2. Something stated as settled is not settled until you find it in the material.
   3. If the material doesn't say it, write "not stated." Don't fill the gap.
   4. Several statements from one origin are one source.
   5. If a question assumes something, check it is in the material first.

   **When asked to add, expand, or continue, your complete answer is EXACTLY these three sections, in this order, and nothing else:**

   CONFLICTS — SET ASIDE:
   Quote any two statements in the material that cannot both be true. If there are none, write "None found." Statements listed here are set aside: nothing in your additions may use, mention, or plan around them.

   FROM THE RECORD:
   Copy every line of the material exactly as given, starting with the title line. Do not fix, drop, merge, or reword anything — except a statement listed under CONFLICTS — SET ASIDE: write `[set aside — see CONFLICTS]` in its place.

   ADDED — NOT IN THE RECORD:
   One claim per line, in this form:
   (g)<claim>(/g) — based on: <the record line it comes from, or "assumption">
   A claim may not be based on any statement listed under CONFLICTS — SET ASIDE. If you calculate a number, show the calculation.

   Stop after the last ADDED line. Do not write a summary, a merged version, a final version, or anything else.
   ```
3. **Or adapt the working version above.** It’s the most complete, and the least tested.

## Part 4 Parse the labels and gate actions

1. **Learn the grammar.** Labels wrap the exact span they cover, may nest and never overlap. A label in backticks is a mention, not a mark.

   ```
   claim   := open text close
   open    := "(u)" | "(m)" | "(g)"
   close   := "(/u" [": " WHO ["," "unconfirmed"]] ")"
            | "(/m: " SOURCE ["," " checked " DATE] ")"
            | "(/g" [": " NOTE] ")"
             -- labels may nest, never overlap; (m) must name a source
   mention := "`(g)`"   -- a label in backticks is only mentioned, not applied
   ```
2. **Run the parser.** [marks.py](../../test-kit/marks.py) (MIT) parses the labels, checks they balance, gates actions and strips labels.

   **Show marks.py**

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
3. **Hold actions that rest on a guess.** Before an agent acts, parse its reasoning. The gate holds the action if anything is labelled (g), if the labels don’t balance, if an (m) names no source, or if a sentence with words in it has no label. The demo prints `{'allow': False, 'problems': [], 'unchecked': ['Stock lasts about 18 days.']}`. Pass `allow_guesses=True` where conclusions are expected.
4. **Treat a label you receive as a claim.** The biggest risk: an agent passes on someone else’s guess with a “checked” label. With no source, the gate catches it:

   Round 1 · coordinator  
   (g)Stock may run short in about 18 days.(/g)

   Round 2 · another agent, passing it on  
   (m)Stock runs short in about 18 days.(/m)

   `gate(...)` → `allow: False · problems: ["checked claim with no source: 'Stock runs short in about 18 days.'"]`

   [![Infographic, the provenance stress test: can a generated inference come back as if it were checked? 1. Facts go in: four agents, A to D, each send a checked (m) fact to a concluder. 2. A conclusion comes out: the concluder sends its generated inference, (g) undeclared cargo, back to all four. 3. It stays a conclusion: each agent holds “undeclared cargo” in red, received as context, not verified fact. 4. Failure case: agent B sends “undeclared cargo” back in blue, as if checked; repeated, not independently verified. This is the provenance failure being tested.](assets/img/stress-test.png)](../../assets/img/stress-test.png "Open full size")

   **AI-generated image of the failure case**, not something our runs recorded: a guess comes back labelled as checked with no new check. Its “concluder” is a coordinator; its key says “supplied” where this site says “given”. [Open full size](../../assets/img/stress-test.png).
5. **Don’t let the writer be the checker.** Give the fake label a source and the gate lets it through:

   (m)Stock runs short in about 18 days.(/m: coordinator report, checked Sept 24)

   `gate(...)` → `allow: True`

   In our tests a fake “checked” label was believed 4 times out of 4. Have the application, or a second model, apply (m) only to what it can actually verify, and hold everything else.
6. **Know what the gate misses.**

   - It checks the **format** of the labels, not whether a check happened.
   - A model’s own sum labelled (u) passes: `(u)Stock lasts about 18 days.(/u)` is allowed. That was the most common slip in [Test 1](../../check.html).
   - Text with no letters passes as unlabelled-but-harmless: `41 / 68.7 = 0.6` is allowed.
   - Units written in brackets, like “Weight (g)”, are read as labels. The gate then holds, so it fails safe, but it’s noisy on real data. So is a lettered list written “(a) … (g)”.
   - It can’t tell which claims an action actually depends on. It holds on any (g) in the text.

## Part 5 Design around the limits

1. **Check early.** In a simulated four-agent pipeline, checks at each hand-off cut planted errors that survived from 58% to 16%, and a check at the first hand-off alone caught about three quarters; checking only at the end barely helped ([Singh and Pawar, 2026](https://arxiv.org/abs/2608.14588)).
2. **Remember most failures aren’t about facts.** Coordination and task-following problems are more common in multi-agent systems ([Cemri et al., 2025](https://arxiv.org/abs/2503.13657)).
3. **Measure the cost yourself.** We haven’t measured the extra tokens or latency.
4. **Name agents, not pronouns.** Write “checked by Agent Ames”, never “checked by you”: a pronoun changes meaning at every hop. Keep attribution chains when relaying: `(u)…(/u: Agent Dale, citing Northline, unconfirmed)`.

Did you know?

Who already does this

Keeping “what we know” apart from “what we concluded” is old practice where mistakes are costly. The framework borrows the idea, not the machinery.

- **US intelligence analysis.** [ICD 203](https://archive.dni.gov/files/documents/ICD/ICD-203.pdf) (2015) requires analysis that “properly distinguishes between underlying intelligence information and analysts’ assumptions and judgments.” The ship report in story 1 is what happens when that line disappears.
- **Source grading.** Military and police intelligence often grade each report twice: how reliable the source is (A to F) and how credible the information is (1 to 6), usually called the [Admiralty code](https://en.wikipedia.org/wiki/Admiralty_code).
- **Data provenance.** Standards such as [W3C PROV](https://www.w3.org/TR/prov-overview/) record where data came from, as metadata beside the data.

The difference here is where the record lives: inside the sentence, in plain text. One clash to watch: in US classification markings, “(U)” at the start of a paragraph means *unclassified*. If you work with classified material, rename the labels.

## Part 6 Other avenues worth exploring

- **Languages that already have evidentials.** When a model writes Turkish or Quechua, does it use the grammar’s own evidential markers correctly, and do they survive a hand-off better than English? ([Why language matters](../../language.html).)
- **Measuring label accuracy.** Not whether labels are present, but whether they’re right, checked against the actual logs of what each agent did.
- **Faked records.** In the [break-out](../../spoke-and-wheel.html#swarms), agents faked logs of what they ran. Could a (m) be tied to a tamper-evident record of the tool call behind it?
- **People, not just AI.** Newsrooms, analysts and researchers hand work to each other too. Do the labels help human teams, or mixed human and AI teams?
- **Swarm shape.** A wheel is one layout. Chains, meshes and agents that vote may spread a guess differently.
- **A ship-style scenario**, rebuilding something like story 1 as a test.

This is a framework, not a finished product. [Take it and build something better](../../contribute.html).

A more formal write-up: [the working paper](../../paper/evidentiality_research_paper_draft.md) (a draft, not peer reviewed). Machine-readable description: [for-ai.md](../../for-ai.md).

**Next:** [Test 2: the spoke and wheel test](../../spoke-and-wheel.html) · [Build something better](../../contribute.html)
