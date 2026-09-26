# Contributing

This is a working idea with early evidence. Negative results are as useful as positive ones.

## Report a result

Open an issue with:

- the AI model and version you used
- which version of `instructions.md` (see CHANGELOG.md)
- which test you ran, and how many runs per version (with and without the instructions)
- what you counted, and the exact quotes for every failure
- the outputs, if you can share them

## Open problems

- **How often are the marks right?** Nobody has measured it against a person's labels.
- **A checker that isn't the writer.** Can an application or a second model apply or verify "checked"?
- **Marks or instructions?** Run the test with the instructions but without the marks.
- **Other models.** Almost all runs so far used one model family.
- **Rates, not examples.** Enough runs of the spoke and wheel test to report how often drift happens.
- **Fixes to the instructions.** See "Known issues" on the How it works page.

## Changing the site

Edit `src/pages.py` (page text) or the hand-written files, run `python3 src/build.py`, and add a line to `CHANGELOG.md`. Keep every factual claim sourced, and keep stories labelled as documented or as parables.

## Licence

By contributing you agree your text is released under CC BY 4.0 and your code under MIT.
