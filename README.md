# Evidentiality Framework for AI

**When AI guesses look like facts.** A small, plain-text notation that labels where each claim in AI-written text comes from, so the difference between *given*, *checked* and *guessed* survives when text is copied, summarised or passed between AI agents.

```
(u)Warehouse stock is 41 tonnes.(/u: September 15 count sheet)
(m)August donations were 62 tonnes.(/m: donor ledger, checked Sept 20)
(g)At the current gap, stock lasts about six months.(/g)
```

- `(u)` **given**: it was in the material the AI was handed
- `(m)` **checked**: verified against a named source (the closing tag names it)
- `(g)` **generated**: the AI's own inference, estimate or conclusion

**Status: early findings, September 2026.** Small tests, mostly on one model family. Published so other people can test it, break it and make it better.

**Site:** https://jzesbaugh.github.io/Evidentiality_Framework/

## Start Here

| You are… | Go to |
|---|---|
| New to this | [Home](https://jzesbaugh.github.io/Evidentiality_Framework/): two stories, a ship and an AI swarm, then the fix; [the labels](https://jzesbaugh.github.io/Evidentiality_Framework/labels.html); [why language matters](https://jzesbaugh.github.io/Evidentiality_Framework/language.html) |
| Using ChatGPT, Claude or similar | [How to Get Your AI to Label Its Answers](https://jzesbaugh.github.io/Evidentiality_Framework/try.html): five minutes, no set-up |
| Testing one model | [Test 1: one chat, nine models](https://jzesbaugh.github.io/Evidentiality_Framework/check.html) |
| Testing hand-offs in an AI swarm | [Test 2: the spoke and wheel test](https://jzesbaugh.github.io/Evidentiality_Framework/spoke-and-wheel.html), [raw logs](test-kit/logs/) |
| Building AI pipelines or agents | [Building with the labels](https://jzesbaugh.github.io/Evidentiality_Framework/builders.html), [`instructions-working.md`](instructions-working.md) and [`test-kit/marks.py`](test-kit/marks.py) |
| Wanting the formal version | [Working paper draft](paper/evidentiality_research_paper_draft.md) (not peer reviewed) |
| Wanting to build on it | [Take this and build something better](https://jzesbaugh.github.io/Evidentiality_Framework/contribute.html) |
| An AI model reading for a user | [`for-ai.md`](for-ai.md) and [`llms.txt`](llms.txt) |

## The Instructions (Current Version)

[`instructions.md`](instructions.md) is the text you give an AI assistant to make it use the labels. It is the version that was tested (internally labelled v0.5b). Changes to it are recorded in [CHANGELOG.md](CHANGELOG.md).

## Repository Layout

```
index.html, labels.html, language.html,  the site (generated; edit src/pages.py instead)
try.html,
check.html, spoke-and-wheel.html,
builders.html, contribute.html, 404.html
spec.html, test.html, evidence.html     redirects from old addresses (generated)
for-ai.md, llms.txt                      for AI readers (hand-written)
instructions.md                          the instructions, current version (full)
instructions-chat.md                     the chat version, used on the Try it page
instructions-working.md                  the version used day to day (adds (d)); not the tested version
paper/                                   working paper draft (not peer reviewed)
robots.txt, sitemap.xml                  crawler rules, sitemap (sitemap generated)
assets/css, assets/js                    styles and page controls
assets/img/                              social card, icons, AI-generated posters and animations (captioned as such)
assets/img/steps/                        step pictures, one per step (AI-generated illustrations); see its README
assets/md/                               each page as Markdown (generated)
test-kit/                                spoke and wheel test, parser, answer key, raw logs
src/                                     build.py (generator), pages.py (page content), visuals.py (diagrams)
COMPONENTS.md                            every file, its role, size and hash (generated)
```

## Editing and Rebuilding

```bash
pip install markdown markdownify
# edit src/pages.py (page text), for-ai.md, instructions.md, llms.txt or assets/
python3 src/build.py
DRAFT=1 python3 src/build.py   # preview: shows a placeholder where a step picture is still missing
```

The build rewrites the HTML pages, `assets/md/`, `sitemap.xml`, the `Sitemap:` line in `robots.txt`, and `COMPONENTS.md`. The site address lives in one place: `BASE_URL` at the top of `src/build.py`. Record each change in `CHANGELOG.md`.

## Publishing (GitHub Pages)

1. This folder is the repository `jzesbaugh/Evidentiality_Framework`. If the name or domain changes, change `BASE_URL` in `src/build.py` and rebuild.
2. Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`.
3. Optional custom domain: set it in Settings → Pages (this writes a `CNAME` file), point DNS at GitHub (subdomain: CNAME to `jzesbaugh.github.io`; apex: GitHub's A/AAAA records), turn on Enforce HTTPS once the certificate is issued, verify the domain in your GitHub account settings, then change `BASE_URL` in `src/build.py` and rebuild.
4. Check the live site with JavaScript off, and fetch it with a tool that doesn't run JavaScript.

## Search and AI Discovery

- Every page has a description, a canonical link and structured data (schema.org JSON-LD). `sitemap.xml` lists every page.
- `llms.txt` and `for-ai.md` give AI tools a map and a plain-language process description. Each page also links its Markdown version.
- **robots.txt on a project site:** crawlers only read `robots.txt` at the root of a host. At `jzesbaugh.github.io/Evidentiality_Framework/` this file is not read; a copy has to live in the `jzesbaugh.github.io` user-site repository, or the site needs its own domain. Until then, submit `sitemap.xml` directly in Google Search Console and Bing Webmaster Tools.
- Each article also carries schema.org `HowTo` data built from its parts and steps.

## Licence

Text, site content and illustrations: [CC BY 4.0](LICENSE). Scripts (`test-kit/`, `src/`, `assets/js/`): [MIT](LICENSE-CODE). Please credit *Evidentiality Framework for AI, Jesse Zesbaugh*; see [CITATION.cff](CITATION.cff).

## Author

[Jesse Zesbaugh](https://github.com/JZesbaugh). Results, criticism and failed replications are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).
