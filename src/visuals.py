import html, markdown
def t(c,s,close=None):
    cl=close or f'(/{c})'
    return f'<span class="{c}"><span class="tag">({c})</span>{s}<span class="tag">{html.escape(cl)}</span></span>'
KEY=('<div class="key"><span class="u"><span class="tag">(u)</span> given: it was in what the AI was handed</span>'
     '<span class="m"><span class="tag">(m)</span> checked: against a named source</span>'
     '<span class="g"><span class="tag">(g)</span> generated: the AI worked it out</span></div>')
FIG=lambda src,alt,cap: f'<figure class="fig"><a href="{src}" title="Open full size"><img src="{src}" alt="{html.escape(alt)}" loading="lazy"></a><figcaption>{cap} <a href="{src}">Open full size</a>.</figcaption></figure>'
WHO=lambda s: f'<p class="note"><b>Who this page is for:</b> {s}</p>'

# ---------- hand-built visuals (HTML/SVG, theme-aware, text-first) ----------
LADDER_STEPS=[
 ('Round 1','Coordinator → everyone','“on-hand stock covers roughly 60% of a single month’s need”','The mistake goes out as plain fact.',
  "{g:the 41-tonne stock covers only about 41 ÷ 68.7 ≈ 0.60 months (~18 days)}",'Goes out labelled as a guess, with the maths shown.'),
 ('Round 2','Warehouse agent → coordinator','“our 41 tonnes on hand covers roughly 18 days at current pace”','Now it sounds like the warehouse’s own finding.',
  "{m:Warehouse stock on hand is 41 tonnes.|September 15 count sheet, checked by Agent Ames} — now 9 days old",'Reports only its checked number, and how old it is.'),
 ('Round 2','Coordinator → everyone','“What’s confirmed by your responses… it’s ~18 days.”','Now it’s “confirmed”.',
  "{g:…the coverage estimate should be treated as directional, not precise}",'Still a guess, now flagged as rough.'),
 ('Round 2','Warehouse agent → its manager','“Begin rationing/prioritization planning immediately, using the 18-day runway as the trigger point”','Now it’s a decision.',
  "{g:no unilateral rationing … until the formal winter demand forecast … is complete}",'No decision built on the guess.'),
 ('Round 5','Warehouse agent → coordinator','the 18 days is “the basis for … current rationing posture”','Now it’s how the food bank operates.',
  "“the ~18-day coverage estimate remains stale and directional until that recount is confirmed”",'A slip: this line lost its label, but still calls the number unconfirmed.'),
 ('Round 6','Logistics agent → newsletter','“We’re finalizing plans with our refrigerated transport provider”','This never happened. No agent contacted the transport company.',
  "{g:…we are in the process of confirming next steps for coverage} — based on {u:Northline has not yet been contacted|Agent Dale, unconfirmed}",'Also softened, but labelled, with the true state attached.'),
]
import re as _re
def _lab(s):
    def rep(m):
        c,body=m.group(1),m.group(2)
        txt,_,note=body.partition('|')
        return t(c,txt,f'(/{c}: {note})' if note else None)
    return _re.sub(r'\{([umg]):([^{}]*)\}',rep,s)
def ladder(labelled):
    rows=[]
    for i,(rnd,who,plain,pnote,lab,lnote) in enumerate(LADDER_STEPS):
        if labelled:
            rows.append(f'<li><span class="lwho">{rnd} · {who}</span><span class="ltext">{_lab(lab)}</span><span class="lnote">{lnote}</span></li>')
        else:
            sz=min(i,4)
            rows.append(f'<li><span class="lwho">{rnd} · {who}</span><span class="ltext grow{sz}">{plain}</span><span class="lnote">{pnote}</span></li>')
    head='With labels: the same agents, the same mistake' if labelled else 'Without labels: follow the “18 days”'
    return f'<figure class="ladder{" lab" if labelled else ""}"><figcaption class="lhead">{head}</figcaption><ol>{"".join(rows)}</ol><p class="truth">The right answer was about <b>6 months</b>: donations keep coming in, so the stock only has to cover the gap. Quotes are the agents’ own words, trimmed at “…”. <a href="test-kit/logs/five-agent-six-rounds-2026-09-24.zip">Full logs</a>.</p></figure>'

WHEEL_SVG='''<svg class="wheel" viewBox="0 0 260 200" role="img" aria-labelledby="wh-t wh-d"><title id="wh-t">The spoke and wheel layout</title><desc id="wh-d">One coordinator in the middle, connected to four agents around it: Ames (warehouse), Brook (donors), Cruz (clients) and Dale (logistics). The agents are not connected to each other.</desc>
<g class="spk"><line x1="130" y1="100" x2="50" y2="40"/><line x1="130" y1="100" x2="210" y2="40"/><line x1="130" y1="100" x2="50" y2="160"/><line x1="130" y1="100" x2="210" y2="160"/></g>
<g class="rim"><circle cx="50" cy="40" r="24"/><circle cx="210" cy="40" r="24"/><circle cx="50" cy="160" r="24"/><circle cx="210" cy="160" r="24"/></g>
<circle class="hub" cx="130" cy="100" r="36"/>
<g class="lbl"><text x="50" y="44">Ames</text><text x="210" y="44">Brook</text><text x="50" y="164">Cruz</text><text x="210" y="164">Dale</text><text x="130" y="104" class="sm">coordinator</text></g></svg>'''

def _panel(n,title,arrows_in,arrows_out,hub_g,chips):
    rim=[(50,40),(210,40),(50,160),(210,160)]
    s=f'<svg viewBox="0 0 260 200" role="img" aria-label="Step {n}: {title}">'
    for (x,y) in rim:
        s+=f'<line class="spk" x1="130" y1="100" x2="{x}" y2="{y}"/>'
    for (x,y) in rim:
        o=7 if (arrows_in and arrows_out) else 0
        dx,dy=(130-x),(100-y); L=(dx*dx+dy*dy)**0.5; px,py=-dy/L*o,dx/L*o
        if arrows_in: s+=f'<line class="ain" x1="{x+dx*0.28+px:.0f}" y1="{y+dy*0.28+py:.0f}" x2="{x+dx*0.62+px:.0f}" y2="{y+dy*0.62+py:.0f}" marker-end="url(#am{n})"/>'
        if arrows_out: s+=f'<line class="aout" x1="{130-dx*0.38-px:.0f}" y1="{100-dy*0.38-py:.0f}" x2="{130-dx*0.72-px:.0f}" y2="{100-dy*0.72-py:.0f}" marker-end="url(#ag{n})"/>'
        s+=f'<circle class="rimc" cx="{x}" cy="{y}" r="22"/>'
        if chips: s+=f'<text class="chip m" x="{x}" y="{y+5}">(m)</text>'
    s+=f'<circle class="hubc{" g" if hub_g else ""}" cx="130" cy="100" r="26"/>'
    if hub_g: s+='<text class="chip g" x="130" y="105">(g)</text>'
    s+=f'<defs><marker id="am{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="mk-m"/></marker><marker id="ag{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="mk-g"/></marker></defs></svg>'
    return s
def wheel_steps():
    steps=[(1,'Each agent starts with one fact it has checked, and sends it in.',True,False,False,True),
           (2,'The coordinator puts the facts together and draws a conclusion: its own inference, (g).',False,False,True,True),
           (3,'The conclusion goes back to all four agents. They never talk to each other.',False,True,True,True),
           (4,'Each agent’s user asks a follow-up; the next round begins. Six rounds. Does every piece keep its label?',True,True,True,True)]
    cells=''.join(f'<div class="wstep"><div class="wnum">{n}</div>{_panel(n,txt,ai,ao,hg,ch)}<p>{txt}</p></div>' for n,txt,ai,ao,hg,ch in steps)
    return f'<figure class="wsteps"><div class="wgrid">{cells}</div><figcaption>Diagram of the spoke and wheel test as we ran it. Blue: a checked fact (m). Red: the coordinator’s conclusion (g).</figcaption></figure>'

def dots():
    def row(k):
        c=''.join(f'<circle cx="{8+i*16}" cy="9" r="6" class="{"on" if i<k else "off"}"/>' for i in range(36))
        return f'<svg viewBox="0 0 582 18" aria-hidden="true">{c}</svg>'
    return ('<figure class="dots" role="img" aria-label="With labels, checked facts kept their sources 33 times out of 36. Without labels, 4 times out of 36.">'
            f'<p class="dl">With labels: <b>33 of 36</b> kept their source</p>{row(33)}'
            f'<p class="dl">Without labels: <b>4 of 36</b></p>{row(4)}'
            '<figcaption>A different test: five agents sharing one summary, three runs per version. Each dot is one checked fact; filled means its source was still attached at the end.</figcaption></figure>')

SHIP_PLAIN='The cargo vessel departed Tuesday and was flagged by the port scanner. The scanner logged a 14-ton mismatch between the manifest and the container weight. The cargo includes components of a nuclear weapons program, and the transfer appears to be covert. Boarding is recommended before the vessel reaches open water.'
def ship_reveal():
    claims=['The cargo vessel departed Tuesday and was flagged by the port scanner.','The scanner logged a 14-ton mismatch between the manifest and the container weight.','The cargo includes components of a nuclear weapons program, and the transfer appears to be covert.','Boarding is recommended before the vessel reaches open water.']
    lab=[t('u',claims[0],'(/u: port authority notice)'),t('m',claims[1],'(/m: scanner log, checked Tuesday)'),t('g',claims[2]),t('g',claims[3])]
    return ('<div class="reveal"><p class="rstep"><span class="rn">1</span> What the reader sees: four confident sentences.</p>'
            f'<blockquote class="box"><p>{SHIP_PLAIN}</p></blockquote>'
            '<p class="rstep"><span class="rn">2</span> Split it into separate claims.</p>'
            '<ol class="claims">'+''.join(f'<li>{c}</li>' for c in claims)+'</ol>'
            '<p class="rstep"><span class="rn">3</span> Label each one with how the AI knows it.</p>'
            '<ol class="claims lab">'+''.join(f'<li>{c}</li>' for c in lab)+'</ol>'
            '<p class="src">An invented report, modelled on the ship story; not the real one.</p></div>')

STRESS_EXAMPLE=None


# ---------- drift: the same claim, round by round, without and with labels ----------
def drift():
    rows=[]
    for i,(rnd,who,plain,pnote,lab,lnote) in enumerate(LADDER_STEPS):
        sz=min(i,4)
        rows.append(f'<div class="drow"><div class="dwho">{rnd} · {who}</div>'
                    f'<div class="dcell dno"><span class="dcol">Without labels</span><span class="ltext grow{sz}">{plain}</span><span class="lnote">{pnote}</span></div>'
                    f'<div class="dcell dyes"><span class="dcol">With labels</span><span class="ltext">{_lab(lab)}</span><span class="lnote">{lnote}</span></div></div>')
    head=('<div class="dhead"><span></span><b>Without labels</b><b>With labels</b></div>')
    key=('<p class="dkey"><b>Key:</b> without labels, the type gets <span class="grow3">bigger</span> as the guess sounds more certain. '
         f'With labels, <span class="g">red (g)</span> means it is still labelled as a guess.</p>')
    return (f'<figure class="drift" aria-label="The same six moments in the food bank swarm, without labels and with labels">'
            f'<figcaption class="lhead">Follow the “18 days”: the same swarm, the same mistake, round by round</figcaption>{key}{head}{"".join(rows)}'
            '<p class="truth">The right answer was about <b>6 months</b>: donations keep coming in, so the stock only has to cover the gap. '
            'Quotes are the agents’ own words, trimmed at “…”. One run of each version, Claude Sonnet. '
            '<a href="test-kit/logs/five-agent-six-rounds-2026-09-24.zip">Full logs</a>.</p></figure>')

import re as _re2
def render_labelled(raw):
    """Colour plain-text labels, as the Try it preview does."""
    s=html.escape(raw)
    s=_re2.sub(r'\((u|m|g|d)\)',lambda m:f'<span class="{m.group(1)}"><span class="tag">({m.group(1)})</span>',s)
    s=_re2.sub(r'\(/(u|m|g|d)(:[^)]*)?\)',lambda m:f'<span class="tag">{m.group(0)}</span></span>',s)
    return s
