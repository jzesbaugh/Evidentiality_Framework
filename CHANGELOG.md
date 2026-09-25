# Changelog

Newest first. Record every change to the site, the instructions or the test kit here.

## 0.1.7 — 2026-09-24 — click-through fixes

- Home: page-links paragraph removed (the "In short" box and section 8 link to the pages); "In short" box adds the 33/36 vs 4/36 result with a link to the evidence.
- Food bank text version rewritten as two lists, "Without labels" then "With labels"; "ignore the right column" replaced with wording that works with or without the graphic.
- Social card key now matches the page key: given to the AI · measured / checked · generated / guessed by the AI.

## 0.1.6 — 2026-09-24 — social card, favicon, first screen

- Social preview card (`assets/img/social-card.png`, 1200×630; source `src/social-card.html`): an AI summary with one line of each label, the guess stated as fact and leading to action ("Neither bug blocks the release. Ship Friday."), key below, footer "See which parts your AI checked, and which it guessed." Tested on blind readers (all understood it, all would click).
- Open Graph and Twitter card tags on every page (built from `BASE_URL`), favicon (red "(g)", SVG + 32px PNG) and home-screen icon.
- Home: an "In short" box under the headline with the card's example, the key, and links to Try it and For builders; the stories follow unchanged. Blind click-through readers (3 of 3) found the card's payoff too far down the page.

## 0.1.5 — 2026-09-24 — full-site consistency pass

- Fixed: break-out count in the intro ("hundreds of them got into" the servers; about 700 per METR); duplicated ship lines trimmed; one of three repeats of the plain-words result removed; "A (g) label" instead of "A red label"; Try-it no longer says the instructions only change labelling; evidence page names the source of its 33/36 result and points to "the six-round result"; for-ai.md wording matches the evidence page ("about as well", "on single questions"); grammar line in For builders; notes that the tested instructions and `marks.py` keep the older word "marks".

## 0.1.4 — 2026-09-24 — one word: "labels"

- "Marks" replaced by "labels" across the site, both graphics, for-ai.md, llms.txt and README ("hard markers" kept in section 5 as the concept; `marks.py` keeps its file name; `instructions.md` unchanged, as tested).
- test-kit/ANSWER_KEY.md: internal word "Module" replaced by "With labels".

## 0.1.3 — 2026-09-24 — audit framing

- Home section 1: one line spelling out the stakes (the report looked like every trusted report; nothing on it said "guess"; nothing to audit).
- Home section 7 reframed: "What the labels can't do alone, and what closes the gap": labels as an audit trail, each limit paired with what closes it (a checker that isn't the writer; incoming "checked" treated as a claim).
- Framework introduction ends "so the text can be audited later."

## 0.1.2 — 2026-09-24 — plain-reader changes

- Home section 6: an everyday example (bakery holiday post with one made-up detail), with and without labels, placed before the ship example.
- Home section 5 rewritten: "Some languages build it in. English doesn't." English hedges drop out when text is rewritten, AI writes English, so the fix needs hard markers that work like a metadata field: present or absent, fixed in meaning, auditable.

## 0.1.1 — 2026-09-24 — expert-review fixes (before launch)

**Search wording:** page titles, H1s and descriptions now use the words people search for (AI hallucination, AI assistant, AI agents, provenance, multi-agent, human-in-the-loop); the site name moves to the end of every title.
**Search hygiene:** for-ai.md, instructions.md and llms.txt removed from sitemap.xml (they stay linked); the two graphics are marked `noindex, indexifembedded`; 404 page has no canonical and no Markdown links; nav and logo link to `./`; duplicate alternate link on for-ai.html removed; `dateModified` is set by hand (`UPDATED` in src/build.py).
**Accessibility:** (u)/(m)/(g) tags and faint text now pass WCAG AA contrast in both themes (measured: light 4.8–6.6, dark 6.6–8.1; faint 4.7 / 4.6); skip-to-content link; nav labelled "Site"; toolbar role corrected; graphics resize to their content (no inner scroll on phones).

## 0.1 — 2026-09-24 — first public version (early findings)

**Site**
- Home page built around the stories: the CNN-reported ship close call (Sept 18, 2026), AI agents working together (DeepMind fake proofs, the OpenAI / Hugging Face break-out, Anthropic's Project Vend), people doing the same (banana parable, Sandy Island, citogenesis), evidentiality in languages, the fix, limits.
- Pages: How it works, Try it, For builders (with "Who already does this": ICD 203, Admiralty code, W3C PROV), Test it, Evidence, For AI models, Contribute, 404.
- Two graphics (food bank six rounds; invented ship report), each with a text version.
- Page controls: theme (auto/light/dark), Download .md, Copy as Markdown, Copy an AI summary prompt, Print / PDF. Script-only controls are hidden when JavaScript is off.
- Search and AI discovery: descriptions, canonical links, schema.org JSON-LD, sitemap.xml, robots.txt, llms.txt, for-ai.md, per-page Markdown.
- Social preview tags: not yet (need an image).

**Instructions**
- `instructions.md`: first public version. Tested internally as v0.5b. Heading renamed from the internal test label.

**Test kit**
- `mini_swarm.py`: path to the instructions works from any folder; retries with backoff; stops on an empty reply; exact hand-off check rebuilt from saved outputs.
- `marks.py`: list numbers, bullets, headings and table pipes no longer count as unmarked text; words in backticks count as claims; `allow_guesses` option.
- `score_mini.py` added. `ANSWER_KEY.md`: timing stated plainly.
- Raw logs of the six-round run published (`test-kit/logs/`).
