> How to Take This and Build Something Better: The Evidentiality Framework is a starting point. Take it, rename it, build on it: ideas, good first projects, and how to tell us what you made.
>
> Evidentiality Framework for AI. Early findings, September 2026. Web version: https://jzesbaugh.github.io/Evidentiality_Framework/contribute.html. Text CC BY 4.0.

Build on it

# How to Take This and Build Something Better

This is a framework, not a finished product. The idea is for people to take it and make something much better with it.

**In This Article**

1. [Part 1: Build on It](#build)
2. [Part 2: Good First Projects](#open)
3. [Part 3: Tell Us What You Made](#tell)

## Part 1 Build on It

1. **Take it.** Text is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); scripts are MIT. Rename the labels, change the instructions, build tools on it, ship it. Credit *Evidentiality Framework for AI, Jesse Zesbaugh* ([CITATION.cff](../../CITATION.cff)).
2. **Pick something to build.** Some ideas we haven’t built:

   - A browser extension that colours the labels in any AI chat.
   - A chat interface that shows each label as a badge you can click to see its source.
   - A gate for a real agent pipeline, with a checker that isn’t the writer.
   - A swarm dashboard that follows one claim from agent to agent.
   - Versions of the labels for other languages, or for fields like medicine, law or journalism.
3. **Start from the working version.** The [version we use every day](../../builders.html#working) is the most complete. The [tested version](../../instructions.md) is the one with evidence behind it.

## Part 2 Good First Projects

1. **Measure how often the labels are right, at scale.** Our checks are one run per model, or a few runs per condition. Nobody has a rate yet.
2. **Build a checker that isn’t the writer.** An application or a second model that applies or verifies “checked”.
3. **Separate the labels from the instructions.** Run the spoke and wheel test with the instructions but without the labels.
4. **Turn examples into rates.** Twenty or more runs per version, other model families, scored by someone who doesn’t know which is which.
5. **Fix the known issues.** Models label their own sums as (u); a conclusion’s closing tag doesn’t say whose conclusion it is; plans drift into reports of progress over several rounds; a received (m) is passed on as checked; the full version’s document format sometimes appears on other tasks; [the gate’s gaps](../../builders.html#gate).

## Part 3 Tell Us What You Made

1. **Show us.** Open an issue in [the repository](https://github.com/jzesbaugh/Evidentiality_Framework/issues) with a link to what you built.
2. **Report a result.** Model and version, which instructions, which test, how many runs, what you counted, and quotes for every failure. A result that shows it failing is as useful as one that shows it working.

A more formal write-up: [the working paper](../../paper/evidentiality_research_paper_draft.md) (a draft, not peer reviewed). Thank you. Source and updates: [the GitHub repository](https://github.com/jzesbaugh/Evidentiality_Framework).
