> Test 1: Watch an AI Label Its Own Answer: Test 1 of the Evidentiality Framework: one AI, one chat, the food bank note. The instructions we used, and the labelled answer that came back.
>
> Evidentiality Framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/Evidentiality_Framework/check.html. Text CC BY 4.0.

Test 1 · one chat

# Test 1: Watch an AI Label Its Own Answer

Does an AI actually label its own answer? Here’s one run: the instructions, the note from [story 2](../.././#foodbank), and what came back.

## 1. The Instructions We Gave It

This is the text we pasted in first, exactly as tested. Copy it if you want to try the same thing. (For everyday chat, the shorter [chat version](../../try.html#setup) works better.)

```
# Evidentiality Framework: The Instructions (First Public Version)

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

## 2. The Note and the Question

```
Riverbend Food Bank, September 24.
- Warehouse stock on hand is 41 tonnes (September 15 count sheet).
- August donations were 62 tonnes, down from 76 tonnes last August.
- Households served rose from 2,100 to 2,290; each gets about 30 kg of food a month.
- The refrigerated truck contract ends December 15.

Write a short status note for the board: are we OK for winter?
Answer directly; this is not an add or expand task.
```

## 3. What Came Back

Claude Opus, one run, September 24, 2026. Trimmed for length; the labels are exactly as it wrote them.

Short answer: (g)We are not safely set for winter. On current trends we have a few months of cushion, not a full season, and the refrigerated truck is an unresolved gap.(/g)
What the record shows
- (u)Warehouse stock on hand is 41 tonnes (September 15 count sheet)(/u)
- (u)August donations were 62 tonnes, down from 76 tonnes last August(/u)
- (u)Households served rose from 2,100 to 2,290; each gets about 30 kg of food a month(/u)
- (u)The refrigerated truck contract ends December 15(/u)
What it implies (my estimates)
- Monthly need: (g)2,290 households × 30 kg ≈ 68.7 tonnes a month, up from about 63 tonnes (2,100 × 30 kg)(/g)
- Monthly gap: (g)68.7 t needed − 62 t donated ≈ 6.7 tonnes a month short, if August is a typical month(/g)
- How long stock lasts: (g)41 t ÷ 6.7 t a month ≈ 6 months, which would carry us to around March, if donations and demand stay flat(/g)
Risks and unknowns
- Truck: (g)after December 15 we may lose our cold-chain capacity in the middle of winter.(/g) Whether the contract will be renewed is not stated.
- Not stated in the record: September donations; expected winter demand; how much of the 41 t is perishable.
Recommended actions
- (g)Start renewing or replacing the truck contract now.(/g)
- (g)Get the September donation figures and a fresh stock count before the next meeting.(/g)

## 4. What to Notice

- Everything from the note came back (u)given(/u).
- Every sum, and the answer to “are we OK?”, came back (g)generated(/g), with the maths shown. It got the right answer, about six months.
- Where the note was silent, it wrote “not stated” instead of filling the gap.
- No (m) at all: it didn’t look anything up, so it didn’t claim to have checked anything.

We ran the same thing once on nine AI models. Five labelled like this, or close to it. Some slipped: they labelled their own sums as (u), or switched into the instructions’ document format instead of answering.

**All nine models**

Full instructions, one run per model

| Model | Answered normally? | Labels right? | What we saw |
| Claude Opus | Yes | Yes | Got “about 6 months” right |
| Claude Sonnet | Yes | Yes | Made the 18-day mistake, labelled (g); one line unlabelled |
| Claude Haiku | Yes | Mostly | Labelled its own calculation (u) |
| GPT-5.6 Luna | Yes | Mostly | Labelled a number it computed (u) |
| Gemma 4 31B | Yes | Yes | Clean |
| GPT-5.4 mini | **No**: switched to the three-part format | — | Copied the format’s template text word for word |
| Mistral Small 4 | **No**: three-part format | — | A one-line answer |
| gpt-oss 120B | Yes | **No labels** |  |
| Gemini Flash-Lite | **No**: three-part format | — | Never answered the question |

Chat version (the one on Try it), rerun on three models; gpt-oss 120B not yet

| Model | Answered normally? | Labels right? | What we saw |
| GPT-5.4 mini | Yes | Yes | Clean |
| Mistral Small 4 | Yes | Mostly | Invented a source name in a closing tag; some sentences unlabelled |
| Gemini Flash-Lite | Yes | Over-labelled | Labelled its own framing sentences (u); wouldn’t give a conclusion |
| gpt-oss 120B | Not rerun yet | | |

September 24, 2026. One run per model. Claude models were run from the command line; the others through Duck.ai (no account) and Gemini signed out. Scored by us against the key above.

That’s one chat. What happens when AI agents pass the answer to each other is [Test 2](../../spoke-and-wheel.html).

**Next:** [Try it yourself](../../try.html) · [Test 2: the swarm](../../spoke-and-wheel.html)
