"""Build the Evidentiality framework for AI site.

Run from anywhere:  python3 src/build.py
Writes the HTML pages, assets/md/*.md page exports, sitemap.xml and COMPONENTS.md
into the repository root. Hand-written files (for-ai.md, instructions.md, llms.txt,
robots.txt, README.md, assets/css, assets/js, assets/visuals, test-kit/) are read, not written.
Needs: pip install markdown markdownify
MIT licence.
"""
import os, re, sys, json, hashlib, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
from markdownify import markdownify as _md

# ---- site settings: change BASE_URL once the repository name / domain is final ----
SITE_NAME = 'Evidentiality framework for AI'
BASE_URL  = 'https://jzesbaugh.github.io/evidentiality-framework/'
AUTHOR    = {'name': 'Jesse Zesbaugh', 'url': 'https://github.com/JZesbaugh'}
PUBLISHED = '2026-09-24'
UPDATED   = '2026-09-24'   # change by hand when page content changes (feeds dateModified and the sitemap)
STATUS    = 'Early findings, September 2026'

NAV = [('./','Home'),('spec.html','How it works'),('try.html','Try it'),('builders.html','For builders'),
       ('test.html','Test it'),('evidence.html','Evidence'),('for-ai.html','For AI models'),('contribute.html','Contribute')]

def md_path(fn):
    return 'for-ai.md' if fn == 'for-ai.html' else 'assets/md/' + fn.replace('.html', '.md')

def to_md(fn, title, desc, body):
    b = body.replace('</span><span class="m"><span class="tag">', '</span> · <span class="m"><span class="tag">') \
            .replace('</span><span class="g"><span class="tag">', '</span> · <span class="g"><span class="tag">')
    b = re.sub(r'<iframe[^>]*>.*?</iframe>', '', b, flags=re.S)
    b = re.sub(r'<noscript>.*?</noscript>', '', b, flags=re.S)
    b = re.sub(r'<(script|textarea)[^>]*>.*?</\1>', '', b, flags=re.S)
    b = re.sub(r'<summary>(.*?)</summary>', r'<p><b>\1</b></p>', b, flags=re.S)
    # links inside assets/md/ must point back up to the site root
    b = re.sub(r'href="(?!https?:|#|mailto:)([^"]+)"', r'href="../../\1"', b)
    text = _md(b, heading_style='ATX', bullets='-', strip=['span'])
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return f'> {title}: {desc}\n>\n> {SITE_NAME}. {STATUS}. Web version: {BASE_URL}{fn if fn != "index.html" else ""}. Text CC BY 4.0.\n\n{text}\n'

def jsonld(fn, title, desc):
    url = BASE_URL + ('' if fn == 'index.html' else fn)
    person = {'@type': 'Person', '@id': AUTHOR['url'] + '#person', 'name': AUTHOR['name'], 'url': AUTHOR['url'], 'sameAs': [AUTHOR['url']]}
    site = {'@type': 'WebSite', '@id': BASE_URL + '#website', 'url': BASE_URL, 'name': SITE_NAME, 'inLanguage': 'en',
            'publisher': {'@id': person['@id']}}
    page = {'@type': 'WebPage', '@id': url + '#page', 'url': url, 'name': title, 'description': desc,
            'isPartOf': {'@id': site['@id']}, 'author': {'@id': person['@id']}, 'inLanguage': 'en',
            'datePublished': PUBLISHED, 'dateModified': UPDATED,
            'license': 'https://creativecommons.org/licenses/by/4.0/'}
    graph = [site, person, page]
    if fn == 'index.html':
        graph.append({'@type': ['CreativeWork', 'LearningResource'], '@id': BASE_URL + '#framework',
                      'name': SITE_NAME, 'description': desc, 'author': {'@id': person['@id']},
                      'creativeWorkStatus': 'Early findings', 'datePublished': PUBLISHED,
                      'license': 'https://creativecommons.org/licenses/by/4.0/', 'isAccessibleForFree': True,
                      'learningResourceType': 'Framework',
                      'keywords': 'evidentiality, AI hallucination, provenance, multi-agent systems, AI agents, source tracking, LLM',
                      'about': ['Evidentiality', 'Provenance', 'Multi-agent systems', 'Hallucination (artificial intelligence)']})
    if fn == 'builders.html':
        graph.append({'@type': 'SoftwareSourceCode', 'name': 'marks.py', 'programmingLanguage': 'Python',
                      'codeRepository': BASE_URL + 'test-kit/', 'license': 'https://opensource.org/licenses/MIT',
                      'author': {'@id': person['@id']}})
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False) + '</script>'

SOCIAL_IMAGE = 'assets/img/social-card.png'   # 1200x630; source: src/social-card.html
SOCIAL_ALT = 'Three sentences from an AI summary, each labelled: (u) The launch is on track, from meeting notes; (m) Two bugs are still open, checked in the issue tracker; (g) Neither bug blocks the release. Ship Friday, a guess by the AI.'

def social(fn, title, desc, url):
    img = BASE_URL + SOCIAL_IMAGE
    esc = lambda x: x.replace('"', '&quot;')
    return (f'<meta property="og:type" content="{"website" if fn == "index.html" else "article"}">'
            f'<meta property="og:site_name" content="{SITE_NAME}"><meta property="og:title" content="{esc(title)}">'
            f'<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:image:alt" content="{esc(SOCIAL_ALT)}">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">'
            f'<meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{img}"><meta name="twitter:image:alt" content="{esc(SOCIAL_ALT)}">')

def page(fn, title, desc, body):
    mdfile = md_path(fn)
    if fn not in ('for-ai.html', '404.html'):
        open(mdfile, 'w').write(to_md(fn, title, desc, body))
    is404 = fn == '404.html'
    tools = (f'<div class="tools" role="group" aria-label="Page tools">'
             f'<button type="button" class="js-only" id="t-theme">Theme: auto</button>'
             + ('' if is404 else f'<a href="{mdfile}" download>Download .md</a>'
             f'<button type="button" class="js-only" id="t-copy" data-md="{mdfile}">Copy as Markdown</button>') +
             f'<button type="button" class="js-only" id="t-ai">Copy an AI summary prompt</button>'
             f'<button type="button" class="js-only" id="t-print" title="Print, or choose Save as PDF in the print dialog">Print / PDF</button>'
             f'<span class="status" id="t-status" aria-live="polite"></span></div>')
    nav = ''.join(f'<a href="{h}"' + (' aria-current="page"' if (h == fn or (h == './' and fn == 'index.html')) else '') + f'>{t}</a>' for h, t in NAV)
    canonical = BASE_URL + ('' if fn == 'index.html' else fn)
    full_title = f'{title} · {SITE_NAME}'
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{'<base href="' + BASE_URL + '"><meta name="robots" content="noindex">' if fn == '404.html' else ''}
<title>{full_title}</title><meta name="description" content="{desc}">
{'' if is404 else f'<link rel="canonical" href="{canonical}">'}<meta name="author" content="{AUTHOR['name']}">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
{'' if is404 else social(fn, full_title, desc, canonical)}
<link rel="alternate" type="text/markdown" href="for-ai.md" title="Process description for language models">
{'' if (is404 or fn == 'for-ai.html') else f'<link rel="alternate" type="text/markdown" href="{mdfile}" title="This page as Markdown">'}
<script src="assets/js/controls.js"></script>
{jsonld(fn, full_title, desc)}</head>
<body><a class="skip" href="#main">Skip to content</a><header class="site"><div class="in"><a class="name" href="./">{SITE_NAME}</a><nav aria-label="Site">{nav}</nav></div></header>
{tools}
<main id="main">{body}</main>
<footer><div class="in">Too long? Ask your AI assistant to summarise any page here. Written for AI readers: <a href="for-ai.md">for-ai.md</a> · <a href="llms.txt">llms.txt</a><br>{STATUS} · By <a href="{AUTHOR['url']}">{AUTHOR['name']}</a> · Text CC BY 4.0 · Scripts MIT</div></footer></body></html>'''
    open(fn, 'w').write(html)

def sitemap(files):
    urls = ''.join(f'<url><loc>{BASE_URL}{"" if f == "index.html" else f}</loc><lastmod>{UPDATED}</lastmod></url>' for f in files)
    extra = ''  # for-ai.md, instructions.md, llms.txt stay linked but are left out of the sitemap (duplicates of HTML pages)
    if os.path.exists('robots.txt'):  # keep the Sitemap line in step with BASE_URL
        r = re.sub(r'(?m)^Sitemap: .*$', f'Sitemap: {BASE_URL}sitemap.xml', open('robots.txt').read())
        open('robots.txt', 'w').write(r)
    open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + extra + '</urlset>\n')

ROLE = {  # what each component is for; COMPONENTS.md is generated from this plus the files on disk
 'index.html': 'Home: the stories, the idea, limits', 'spec.html': 'How it works: marks, rules, full instructions',
 'try.html': 'Try it: five-minute walkthrough for chat-assistant users', 'builders.html': 'For builders: notation, parser, gating, prior art',
 'test.html': 'Test it: the five-agent test and kit', 'evidence.html': 'Evidence and limits', 'for-ai.html': 'For AI models (HTML render of for-ai.md)',
 'contribute.html': 'Contribute: report results, open problems', '404.html': 'Not-found page',
 'for-ai.md': 'Process description for language models (hand-written)', 'instructions.md': 'The instructions: current version (hand-written; tested as v0.5b)',
 'llms.txt': 'Index for AI tools (hand-written)', 'robots.txt': 'Crawler rules (hand-written; see README note on project sites)',
 'sitemap.xml': 'Sitemap (generated)', 'README.md': 'Repository readme', 'CHANGELOG.md': 'Change log', 'COMPONENTS.md': 'This inventory (generated)',
 'CONTRIBUTING.md': 'How to contribute', 'CITATION.cff': 'How to cite', 'assets/img/social-card.png': 'Social preview image, 1200×630', 'assets/img/favicon.svg': 'Favicon (red (g))', 'assets/img/favicon-32.png': 'Favicon, 32px PNG', 'assets/img/apple-touch-icon.png': 'Home-screen icon, 180px', 'src/social-card.html': 'Source for the social preview image', 'LICENSE': 'CC BY 4.0 for text and site content', 'LICENSE-CODE': 'MIT for scripts (src/, assets/js/, test-kit/)', '.nojekyll': 'Tells GitHub Pages to serve files as-is',
 '.gitignore': 'Files git should ignore', 'src/build.py': 'Site generator', 'src/pages.py': 'Page content (edit this, then rebuild)',
 'assets/css/style.css': 'Styles, light and dark', 'assets/js/controls.js': 'Page controls: theme, copy, AI prompt, print',
 'assets/visuals/snowball.html': 'Graphic: food bank, six rounds, with and without marks', 'assets/visuals/color-concept.html': 'Graphic: invented ship report, unmarked vs marked',
 'test-kit/mini_swarm.py': 'Five-agent test runner', 'test-kit/marks.py': 'Parser, balance check, gate, strip', 'test-kit/score_mini.py': 'Keyword flags for hand review',
 'test-kit/ANSWER_KEY.md': 'Answer key for the five-agent test', 'test-kit/README.md': 'Test kit readme', 'test-kit/LICENSE': 'MIT licence for scripts',
 'test-kit/logs/five-agent-six-rounds-2026-09-24.zip': 'Raw logs of the six-round run (zip)', 'test-kit/logs/five-agent-six-rounds-2026-09-24/': 'Raw logs, unzipped (inputs, outputs, prompts, runner)',
}

def components():
    rows = []
    for dirpath, dirs, files in os.walk('.'):
        dirs[:] = sorted(d for d in dirs if d not in ('.git', '__pycache__'))
        rel = os.path.relpath(dirpath, '.')
        if rel.startswith('test-kit/logs/five-agent'):
            continue
        for f in sorted(files):
            p = os.path.normpath(os.path.join(rel, f))
            if p == 'COMPONENTS.md':
                continue
            if p.startswith('assets/md/'):
                role = 'Markdown export of ' + os.path.basename(p).replace('.md', '.html') + ' (generated)'
            else:
                role = ROLE.get(p, '')
            h = hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]
            rows.append(f'| `{p}` | {role} | {os.path.getsize(p):,} | `{h}` |')
    logdir = 'test-kit/logs/five-agent-six-rounds-2026-09-24'
    n = sum(len(fs) for _, _, fs in os.walk(logdir)) if os.path.isdir(logdir) else 0
    rows.append(f'| `{logdir}/` | {ROLE[logdir + "/"]} | {n} files | |')
    open('COMPONENTS.md', 'w').write(
        f'# Components\n\nGenerated by `src/build.py` on {UPDATED}. Every file in the repository, what it is for, its size in bytes, '
        f'and the first 12 characters of its SHA-256, so a change to any file shows up here on the next build.\n\n'
        f'Site settings: base URL `{BASE_URL}` · status "{STATUS}".\n\n| File | Role | Bytes | SHA-256 |\n|---|---|---|---|\n' + '\n'.join(rows) + '\n')

if __name__ == '__main__':
    import pages
    for p in pages.PAGES:
        page(*p)
    page('404.html', 'Page not found', 'This page does not exist on the Evidentiality framework for AI site.',
         '<h1>Page not found</h1><p>That page doesn’t exist. Try the <a href="./">home page</a> or the <a href="llms.txt">site index</a>.</p>')
    sitemap([p[0] for p in pages.PAGES])
    components()
    print('built', len(pages.PAGES) + 1, 'pages; sitemap.xml; COMPONENTS.md')
