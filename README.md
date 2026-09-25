# Evidentiality framework for AI

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

**Site:** https://jzesbaugh.github.io/Evidentiality-Framework/

## Start here

| You are… | Go to |
|---|---|
| Curious what problem this solves | [Home](https://jzesbaugh.github.io/evidentiality-framework/): the ship that nearly got boarded, AI agents copying each other's fake results |
| Using ChatGPT, Claude or similar | [Try it](https://jzesbaugh.github.io/evidentiality-framework/try.html): five minutes, no set-up |
| Building AI pipelines or agents | [For builders](https://jzesbaugh.github.io/evidentiality-framework/builders.html) and [`test-kit/marks.py`](test-kit/marks.py) |
| Wanting to check or extend the results | [Test it](https://jzesbaugh.github.io/evidentiality-framework/test.html), [Evidence](https://jzesbaugh.github.io/evidentiality-framework/evidence.html), [raw logs](test-kit/logs/) |
| An AI model reading for a user | [`for-ai.md`](for-ai.md) and [`llms.txt`](llms.txt) |

## The instructions (current version)

[`instructions.md`](instructions.md) is the text you give an AI assistant to make it use the labels. It is the version that was tested (internally labelled v0.5b). Changes to it are recorded in [CHANGELOG.md](CHANGELOG.md).

## Repository layout

```
index.html … contribute.html, 404.html   the site (generated; edit src/pages.py instead)
for-ai.md, llms.txt                      for AI readers (hand-written)
instructions.md                          the instructions, current version
robots.txt, sitemap.xml                  crawler rules, sitemap (sitemap generated)
assets/css, assets/js                    styles and page controls
assets/visuals/                          the two graphics
assets/md/                               each page as Markdown (generated)
test-kit/                                five-agent test, parser, answer key, raw logs
src/                                     build.py (generator) and pages.py (page content)
COMPONENTS.md                            every file, its role, size and hash (generated)
```

## Editing and rebuilding

```bash
pip install markdown markdownify
# edit src/pages.py (page text), for-ai.md, instructions.md, llms.txt or assets/
python3 src/build.py
```

The build rewrites the HTML pages, `assets/md/`, `sitemap.xml`, the `Sitemap:` line in `robots.txt`, and `COMPONENTS.md`. The site address lives in one place: `BASE_URL` at the top of `src/build.py`. Record each change in `CHANGELOG.md`.

## Publishing (GitHub Pages)

1. Push this folder to a repository named `evidentiality-framework` (or change `BASE_URL` and rebuild).
2. Settings → Pages → Deploy from a branch → `main`, folder `/ (root)`.
3. Optional custom domain: set it in Settings → Pages (this writes a `CNAME` file), point DNS at GitHub (subdomain: CNAME to `jzesbaugh.github.io`; apex: GitHub's A/AAAA records), turn on Enforce HTTPS once the certificate is issued, verify the domain in your GitHub account settings, then change `BASE_URL` in `src/build.py` and rebuild.
4. Check the live site with JavaScript off, and fetch it with a tool that doesn't run JavaScript.

## Search and AI discovery

- Every page has a description, a canonical link and structured data (schema.org JSON-LD). `sitemap.xml` lists every page.
- `llms.txt` and `for-ai.md` give AI tools a map and a plain-language process description. Each page also links its Markdown version.
- **robots.txt on a project site:** crawlers only read `robots.txt` at the root of a host. At `jzesbaugh.github.io/evidentiality-framework/` this file is not read; a copy has to live in the `jzesbaugh.github.io` user-site repository, or the site needs its own domain. Until then, submit `sitemap.xml` directly in Google Search Console and Bing Webmaster Tools.
- Social preview tags (Open Graph, Twitter card) are waiting on a preview image.

## Licence

Text, site content and illustrations: [CC BY 4.0](LICENSE). Scripts (`test-kit/`, `src/`, `assets/js/`): [MIT](LICENSE-CODE). Please credit *Evidentiality framework for AI, Jesse Zesbaugh*; see [CITATION.cff](CITATION.cff).

## Author

[Jesse Zesbaugh](https://github.com/JZesbaugh). Results, criticism and failed replications are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).
