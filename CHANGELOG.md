# Changelog

Newest first. Record every change to the site, the instructions or the test kit here.

## 0.7.1 — 2026-09-26 — pre-upload SEO/LLM check

The PUBLIC_LAUNCH_CHECKLIST was run against the local build. Sections 1–4 were checked before upload; section 0 and the live fetch follow after it.
- **Passed:** every page except 404 has a title, a description, a canonical on the domain, Open Graph and Twitter tags with an absolute image URL, and one h1; `lang="en"` and the viewport tag are set.
  - JSON-LD parses on every page: WebSite, Person, WebPage, CreativeWork on Home, HowTo on the step articles, SoftwareSourceCode on For builders.
  - The sitemap lists the 9 real pages on the domain, with no redirect stubs, and robots.txt points to it and names the search, AI-search, assistant and training crawlers.
  - Nothing loads from a third party; there are no TODO or placeholder strings.
  - With JavaScript off, the full text is present (1,054–2,117 words per page), the JS-only buttons and the colour preview are hidden, and nothing is left stuck on screen.
- **Fixed:**
  - Meta descriptions on Home, Test 2 and For builders were 206–212 characters; they're now under 160, so search results don't cut them off.
  - The redirect stub `evidence.html` had a canonical with a `#fragment`; it now points at the page itself.
  - llms.txt links are now absolute URLs on the domain.
- **Known and left as is:** some page titles run past about 60 characters with the site-name suffix. The key words come first, so a cut-off costs little.

## 0.7 — 2026-09-26 — own domain

- **The site moves to https://evidentiality-framework.org/.** `BASE_URL` is set, and every canonical link, social tag, the sitemap, the JSON-LD, robots.txt's Sitemap line, the README and CITATION.cff now use it.
- **A new `CNAME` file** holds the domain, so later uploads keep GitHub Pages pointed at it.
- **robots.txt** is now read by crawlers, because the site sits at the root of its own domain. Its note and the README are updated. The README also records the Cloudflare set-up: DNS only (grey cloud), managed robots.txt off.
- **Home:** "What the Two Stories Have in Common" now defines provenance and ties the site together in four lines: the ship, the food bank, the framework, the swarm test. This came from an outside AI reviewer's note. for-ai.md §0 carries the same thesis.
- **Dividers:** a horizontal rule now sits before every major section on every page. It's added once, in `page()` in `src/build.py`.
- **Build on It:** a ready-to-copy citation replaces the link to the raw CITATION.cff, with a pointer to GitHub's "Cite this repository" button. CITATION.cff is now version 0.7, released 2026-09-26.
- **Spelling:** "maths" becomes "math" throughout the site (8 places). Other British spellings stay.

## 0.6.3 — 2026-09-26 — title case

- **Title case (AP style)** is now applied at build time to page titles, h1–h3 headings, navigation, article cards, sidebar headings and the "In This Article" boxes. The helper is `titlecase()` in `src/build.py`.
  - Short articles, conjunctions and prepositions stay lower case, unless they're first, last or right before a colon.
  - Label letters such as (g) are left alone, and code is skipped.
  - Examples: "Test 1: One Chat", "Build on It", "Part 3: Pass It On".
- The site name is now "Evidentiality Framework for AI" everywhere, including the README, CITATION.cff, llms.txt, robots.txt and for-ai.md.
- Markdown headings in the README, for-ai.md, the instructions files, the test kit, CONTRIBUTING and the steps readme are title-cased too; code blocks are skipped.
  - The heading line of `instructions.md` changed case only; the tested body text is unchanged.
- The Test 1 card now matches its page: "Watch an AI Label Its Own Answer".

## 0.6.2 — 2026-09-26 — swarm social card

- `assets/img/social-card.png` now uses the swarm card from the handoff packet: "What happens when AI builds on its own guesses?". It's AI-generated, and resized from 1400×732 to 1200×630.
- It replaces the meeting-example card, so the open social-card item is closed, and it matches the site's swarm anchor.
- The social alt text is updated on every page.
- `src/social-card.html` stays in the repo as the source of the old card.
- Known differences from the site: the card says (u) is "From you", and it shows agents investigating each round. The owner chose to swap it in without the blind check.

## 0.6.1 — 2026-09-26 — For builders closes out

- **For builders:**
  - The introduction is rewritten. It says where this is heading (scale) and lists what hasn't been tried because of token limits: 20+ blind-scored runs, a no-labels-instructions arm, agents that investigate, the working version under test, and non-Claude models at volume.
  - The introduction is followed by the working version, then **Questions and answers**.
  - (d) gets a full answer, with a real decision from building this site as the example.
  - New answers: "Can I add my own labels?" (with ideas) and "Does this have to live in the prompt?" (the application, structured output, a second model, orchestration, training, the interface).
  - It closes with **Other avenues worth exploring**: languages with evidentials, label accuracy against logs, tamper-evident (m), human teams, swarm shape, and a ship-style scenario.
- **for-ai.md:** adds the optional (d) extension to the notation section, and a new section 9, "Untested directions". Resources are now section 10.

## 0.6 — 2026-09-26 — drift up front, Test 1 made simple

- **Drift is now the centrepiece.** A new comparison, `drift()` in `src/visuals.py`, follows the "18 days" side by side, round by round. Without labels, the type grows as the guess hardens; with labels, the same round keeps its red (g). There's a key on top, and it stacks on phones. It appears:
  - on Home, under story 2, replacing the one-sided list and the separate "with labels" paragraph;
  - at the top of Test 2, as Part 1 "What happened", merging the old without-labels and with-labels parts.
- **Home order:**
  1. the ship poster, as an invented example, with a caption covering its satellite/scanner and cargo-wording differences;
  2. the key and the punch line;
  3. "the real one almost started a war";
  4. story 1;
  5. story 2 with the drift comparison;
  6. what the stories have in common;
  7. limits;
  8. the cards.
- The home page now says the swarm result is one run and that an earlier result of the same kind didn't replicate.
- **Test 2 is results first:** what happened, how far we got, how it was set up (the poster moves here), why swarms, then run it yourself.
- **Test 1 is one simple page:**
  - the instructions we used, in a copy block;
  - the note;
  - Claude Opus's labelled answer (one run, trimmed), coloured;
  - what to notice;
  - the nine-model table, folded away.
- **For builders:** the working version is shown in a copy block, not folded away.

## 0.5.1 — 2026-09-26 — stress-test infographic

- `assets/img/stress-test.png`, the four-panel “Provenance Stress Test” infographic, replaces the planted-failure animation `stress-test.gif` on For builders (Part 4, “Treat a label you receive as a claim”). It's reduced to 256 colours for size. Alt text and caption are rewritten, and the caption notes that the image says “supplied” where the site says “given”. On GitHub, delete `assets/img/stress-test.gif` by hand.

## 0.5 — 2026-09-26 — two anchor stories, reports first

- **Two anchor stories.** The CNN ship story and our own food bank swarm now open the home page, told in full, and every example on the site comes from one of them.
  - The ship story is used to explain the idea and is described as CNN reported it.
  - The home page then shows the fix on the same two stories: the ship poster with the labelled report, and the labelled swarm run.
  - The bakery and meeting-summary examples are gone from the pages.
- **New page, `language.html`, "Why Language Matters".**
  - It covers evidentiality (Turkish, Quechua, WALS ch. 77: 237 of 418 languages).
  - The banana, Sandy Island and citogenesis stories live here as human examples.
  - It explains why AI slips and why the fix is hard markers.
  - Other pages link back to it.
  - The witness parable and the separate sidebars are gone.
- **The labels page reordered.** It now opens with the two stories, and its examples come from them. A sidebar points to the optional fourth label, (d).
- **Test 1 and Test 2 are now report first, how-to after.** Each covers what we ran, what happened, how far we got and what's still open.
  - Test 1 now states the "Answer directly" line and the full-then-chat order.
  - Test 2 is retitled "How a Guess Spreads Through an AI Swarm". It defines a swarm and covers the swarm incidents and research with sources.
  - Test 2 names the model (Claude Sonnet via the Claude command-line tool) and the full set-up, then tells the run round by round without and with labels.
- **For builders is rewritten as "Building With the Labels".**
  - A first-person introduction.
  - The working version: `instructions-working.md`, the author's own Part III with the personal rules removed; it adds (d); not the tested version.
  - Design questions.
  - The prompt and the gate, with its known gaps stated: a model's own sum labelled (u) passes; text with no letters passes; units like "(g)" are read as labels; the gate can't tell what an action depends on.
  - The grammar is aligned with for-ai.md.
- **Contribute becomes "How to Take This and Build Something Better".** It covers ideas, good first projects, and how to tell us what you made.
- **New in the repo:**
  - `paper/evidentiality_research_paper_draft.md`, a working paper draft, not peer reviewed. It is linked from Home, For builders, Build on it, llms.txt, for-ai.md and the README. Its references still point to the old `evidence.html` and `test.html`, which redirect.
- **for-ai.md:**
  - The labelled run's one slip is now stated.
  - The imperatives are reworded as descriptions.
  - The two anchors and the new pages are added.
- **test-kit/README:** now notes the zip README's stale "home page" pointer and the log file names.
- **Open: the social card** still uses the meeting-summary example, the only thing outside the two stories. It's kept for now; revisit with a ship or food bank version.

## 0.4.1 — 2026-09-26 — new loop animation

- `assets/img/spoke-and-wheel-loop.gif` replaced with “The evidence loop” (60 frames, 1080×760): facts in, (g) conclusion out, new facts in while earlier inferences stay red. It replaces the older “growing puzzle” animation. Alt text and caption rewritten to match (Test 2, Part 2, step 1).

## 0.4 — 2026-09-25 — rebuilt as how-to guides

The site is rebuilt from scratch in a wikiHow style: a home hub and six "How to…" articles. Each article is made of Parts; each Part has numbered steps, and each step has one bold sentence, a short explanation and a picture. The stories now appear as sidebars beside the steps.
- New pages:
  - `labels.html`, How to Tell What an AI Actually Knows (replaces How it works and most of the old home page).
  - `check.html`, Test 1: whether one AI labels its own answer correctly, with the nine-model results.
  - `spoke-and-wheel.html`, Test 2: whether labels survive hand-offs. It replaces Test it and Evidence, and all hand-off results and limits are now here.
- Rewritten as articles: `try.html`, `builders.html`, `contribute.html`.
- Evidence and limits now sit inside each article's Warnings and Q&A instead of on a separate page.
- The old addresses `spec.html`, `test.html` and `evidence.html` redirect to the new pages.
- The labels are now worded as given / checked / generated.
- Step pictures:
  - 16 AI-generated illustrations are commissioned for `assets/img/steps/`; the file names and descriptions are in `src/pages.py`.
  - A missing picture is left out; build with `DRAFT=1` to see placeholders.
  - Pictures are captioned as AI-generated illustrations.
- Each article now carries schema.org `HowTo` data.
- The diagrams moved to `src/visuals.py`.
- Wording fixed after a blind read:
  - The round-1 figure is now given as "about 60% of a month, roughly 18 days".
  - The chat version hasn't been through the spoke and wheel test.
  - Test 1's first run used the full instructions.
  - Removed the claim that labelling quality follows model size.

## 0.3.1 — 2026-09-25 — animations back

- The packet animations return, each captioned as AI-generated: the ship animation on Home §6 (the still three-step version sits under it as text), the spoke and wheel poster and loop animation on Test it (the still diagram sits under them), the food bank animation on Test it, and the planted-failure animation on For builders. 0.3 had removed them over paraphrase and naming; the owner had already accepted those, so they are back.

## 0.3 — 2026-09-25 — redesign around the visuals

Prompted by a handoff packet of visuals and a three-reviewer redesign pass (information architect, visual-explainer designer, reader-journey advocate). The packet's ideas shape the site; the site shows only our own wording and data.
- Home: three reader doors under "In short". The food bank run is told once, in two halves: section 2 shows the guess hardening without labels (growing type, a spoke and wheel diagram); section 6 shows the same rounds with labels. No more "scroll back".
- Home section 6: the ship example is now a three-step reveal (plain report → split into claims → labelled), built from our text. A dot chart shows 33 of 36 vs 4 of 36.
- Test it: a four-step diagram of the spoke and wheel test as we ran it (coordinator, agents starting with one checked fact).
- For builders: the chat-version prompt on the page; "A label you receive is a claim" with a planted example and the checker's real output.
- Contribute and Test it no longer repeat the open-problems list; Try it keeps one line on model differences (details on Evidence); the research paragraph left Home section 2 (it's on Evidence and For builders).
- Removed: the two iframe graphics (replaced by the new in-page versions), the packet's spoke and wheel poster and both animations (duplicates; the food bank animation used colour for good/bad and paraphrased quotes). The ship poster stays on How it works, captioned.
- Diagrams are HTML/SVG in the page: sharp on phones, theme-aware, readable as text.

## 0.2 — 2026-09-25 — chat version, spoke and wheel test, visuals

- Try it now uses a **chat version** of the instructions (`instructions-chat.md`: the labels and rules without the add/expand document format), shown on the page itself. Reason: in a nine-model check (one run each), the full instructions made three models switch to the document format instead of answering; the chat version fixed that on the three we reran. The page says results vary by model.
- The four-agents-plus-coordinator test is named the **spoke and wheel test** throughout.
- How it works: "Cases people ask about" (split mixed claims; repeating isn't checking; given then checked; lost origin; what a label is not).
- Visuals from a handoff packet, each captioned as AI-generated: ship poster (dramatization, with its scanner/satellite slip noted) on How it works; spoke and wheel poster and loop animation, and the six-round animation, on Test it.
- Evidence page: the Try-it cross-model result.
- The unzipped logs folder (235 files) is removed; the zip stays, described as working logs. **Delete `test-kit/logs/five-agent-six-rounds-2026-09-24/` from the repository by hand**; uploading doesn't remove it.

## 0.1.8 — 2026-09-25 — live address

- Site address set to the live GitHub Pages URL, https://jzesbaugh.github.io/Evidentiality_Framework/ (canonical links, social preview image, sitemap, robots.txt, structured data, README, CITATION). The earlier assumed address returned 404.
- Repository and issues links point to github.com/jzesbaugh/Evidentiality_Framework.

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
