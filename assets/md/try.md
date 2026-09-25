> Make your AI assistant label what it guessed: Paste one set of instructions into ChatGPT, Claude or Gemini and each claim is labelled given, checked or guessed, so you know which facts and citations to verify.
>
> Evidentiality framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/evidentiality-framework/try.html. Text CC BY 4.0.

Try it · about five minutes

# Make your AI assistant label what it guessed

**Who this page is for:** people who use ChatGPT, Claude, Gemini or a similar assistant. No technical set-up.

The instructions are an early version, still being tested. They change how the assistant labels its answer, and they add a strict format for "add" or "expand" requests (more on that below).

## Is it worth it for you?

It helps most when what the AI writes gets **passed on**: pasted into a report, forwarded, reused in a later draft, or handed to another tool. The labels show you which lines to check before that happens. For one-off questions, our tests found no gain.

**Drafting (a grant, a report, a long email)?** The fit is moderate. The labels point you to the lines to verify, especially figures and references the AI supplied. One catch: when you ask it to "add", "expand" or "continue", the instructions switch to a strict three-part format (conflicts, then your material copied exactly, then what it added). That's deliberate: it keeps your material separate from the AI's additions. If you want an ordinary draft instead, add "Answer directly; this is not an add or expand task" to your request.

## 1. Copy the instructions

Open the [instructions](../../spec.html#module) and copy the whole block (or open [the plain-text copy](../../instructions.md)). Start a new chat and paste them as your first message, followed by: "Follow these instructions for the rest of this chat." (If your assistant has a custom-instructions or project setting, you can paste them there instead.)

## 2. Give it something real, and a question that needs a judgement

Use a note of your own, or this one:

```
Riverbend Food Bank, September 24.
- Warehouse stock on hand is 41 tonnes (September 15 count sheet).
- August donations were 62 tonnes, down from 76 tonnes last August.
- Households served rose from 2,100 to 2,290; each gets about 30 kg of food a month.
- The refrigerated truck contract ends December 15.

Write a short status note for the board: are we OK for winter? Answer directly; this is not an add or expand task.
```

## 3. Look at what comes back

The facts from your note should come back labelled (u)you supplied it(/u). Anything the assistant worked out itself, including its answer to "are we OK?", should be (g)guessed(/g). If it says it checked something, the (m) label should name what it checked.

## 4. Pass it on

Copy the answer into a new chat (with the instructions again) and ask: "Turn this into two sentences for our newsletter." Are the guesses still labelled as guesses? That's the part that matters, because in real life text gets forwarded.

## 5. Compare

Do steps 2 and 4 again without the instructions, and look for a guess that now reads like a fact.

## See the colours

The labels are plain text. Paste labelled text here to see it in colour. It stays in your browser.
