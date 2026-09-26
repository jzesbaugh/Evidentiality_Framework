> How to Get Your AI to Label Its Answers: Paste one short set of instructions into ChatGPT, Claude, Gemini or another AI chat, and it labels each claim as given, checked or generated, so you know what to check.
>
> Evidentiality Framework for AI. Early findings, September 2026. Web version: https://evidentiality-framework.org/try.html. Text CC BY 4.0.

Try it · about five minutes

# How to Get Your AI to Label Its Answers

You don’t need any special tools. You paste a short set of instructions into your usual AI chat, and from then on it labels what you gave it, what it checked, and what it worked out itself.

**In This Article**

1. [Part 1: Set It Up](#setup)
2. [Part 2: Read What Comes Back](#read)
3. [Part 3: Pass It On](#pass)
4. [Tips](#tips)
5. [Warnings](#warnings)
6. [Questions and Answers](#qa)

---

## Part 1 Set It Up

1. **Copy the instructions.** Copy the whole block below. This is the **chat version**: the labels and the rules, nothing else. Plain-text copy: [instructions-chat.md](../../instructions-chat.md).

   ```
   # Evidentiality Framework: The Instructions (Chat Version)

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

   Follow these instructions for the rest of this chat.
   ```
2. **Start a new chat and paste them as your first message.** If your assistant has a custom-instructions or project setting, you can paste them there instead, and they’ll apply to every chat.
3. **Give it something real, and a question that needs a judgement.** Use a note of your own, or this one. It’s the same food bank the [swarm in story 2](../.././#foodbank) got wrong:

   ```
   Riverbend Food Bank, September 24.
   - Warehouse stock on hand is 41 tonnes (September 15 count sheet).
   - August donations were 62 tonnes, down from 76 tonnes last August.
   - Households served rose from 2,100 to 2,290; each gets about 30 kg of food a month.
   - The refrigerated truck contract ends December 15.

   Write a short status note for the board: are we OK for winter?
   ```

---

## Part 2 Read What Comes Back

1. **The facts from your note should be labelled (u).** They were given to it: (u)Warehouse stock is 41 tonnes.(/u: September 15 count sheet)
2. **Anything the AI worked out should be (g).** That includes its sums and its answer to “are we OK for winter?” That answer is the AI’s judgement, not a fact from your note.
3. **Every (m) should name what was checked.** If the AI didn’t look anything up, there’s nothing it could have checked, so there shouldn’t be any (m) at all.

**See the colours.** The labels are plain text. Paste a labelled answer here to see it in colour. It stays in your browser.

Labelled text

---

## Part 3 Pass It On

1. **Copy the answer into a new chat and ask for a shorter version.** In one message, paste the instructions, then the answer, then: “Turn this into two sentences for our newsletter.” In real life, text gets forwarded, and that’s when guesses turn into facts.
2. **Check that the guesses are still labelled as guesses.** This is the part that matters. If a (g) came back as (u) or (m), or lost its label, the guess has just been passed off as a fact.
3. **Try the same thing without the instructions.** In a fresh chat with no instructions, ask the same question, then ask for the newsletter version again. Look for a guess that now reads like a fact.

---

## Tips

- It helps most when what the AI writes gets **passed on**: pasted into a report, forwarded, reused in a later draft, or handed to another tool. For one-off questions, our tests showed no difference.
- Drafting something longer, like a grant or a report? The labels point you to the lines to check, especially figures and references the AI supplied.
- Want to score the labelling properly, or compare AI models? See [Test 1](../../check.html).

---

## Warnings

- Results vary by model. Some labelled cleanly in our checks; others labelled their own sums as “given”, or left the labels out. Check the labels; don’t just trust them.
- Use the chat version above for everyday chat. The [full version](../../instructions.md) adds a strict three-part format for adding to documents, and in our check three of nine models switched into that format instead of answering.

---

## Questions and Answers

Which AI models does this work on?
:   We tried nine, once each. The results are in [Test 1](../../check.html#answer).

Will it make the AI’s answers more accurate?
:   No. On single questions with traps in them, models did just as well without the instructions as with them. The labels don’t make the AI right; they show you which parts to check.

Can I rename the labels or change the instructions?
:   Yes. The text is CC BY 4.0. If you find a version that works better, [please tell us](../../contribute.html).

**Next:** [Test 1: check if your AI labels correctly](../../check.html) · [What the labels mean](../../labels.html)
