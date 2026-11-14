"""Page templates for the product catalogue. Imported by build_catalogue.py."""
import html
E = html.escape

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def head(cat, catname, extra=''):
    tail = f'<em>{E(extra)}</em>' if extra else ''
    return f'''<header class="sh-head">
  <div class="sh-brand"><img src="images/web/logo-200.png" alt=""><span><b>TGV TRADLINK</b><i>The Plumbing House</i></span></div>
  <div class="sh-cat"><span>{cat}</span>{E(catname)}{tail}</div>
</header>'''


def foot(n):
    return f'<footer class="sh-foot"><span>TGV TRADLINK · Product Catalogue · Nov 2026</span><span>+91 82002 98971 · info.tgvtradlink@gmail.com</span><b>{n:02d}</b></footer>'


def spec_dl(specs):
    return '<dl class="specs">' + ''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in specs) + '</dl>'


def badges(b):
    if not b:
        return ''
    return '<div class="shot-badges">' + ''.join(f'<span class="badge{" ink" if x.startswith("ISI") else ""}">{E(x)}</span>' for x in b) + '</div>'


def shot(p):
    return f'<div class="shot"><img src="images/web/{p["img"]}" alt="{E(p["name"])}"><span class="tick tl"></span><span class="tick br"></span>{badges(p["badges"])}</div>'


def cards(vs, cols):
    out = [f'<div class="cards c{cols}">']
    for v in vs:
        out.append(f'<div class="card"><span class="code">{E(v["code"])}</span><b>{E(v["size"])}</b>'
                   f'<span class="spec">{E(v["spec"])}</span><span class="pack">{E(v["pack"])}</span></div>')
    out.append('</div>')
    return ''.join(out)


def features(fs, cols=2):
    return f'<ul class="feats c{cols}">' + ''.join(
        f'<li><i>{CHECK}</i><div><b>{E(t)}</b><span>{E(d)}</span></div></li>' for t, d in fs) + '</ul>'


def steps(st):
    return '<ol class="steps">' + ''.join(
        f'<li><i>{n:02d}</i><div><b>{E(t)}</b><span>{E(d)}</span></div></li>' for n, (t, d) in enumerate(st, 1)) + '</ol>'


def variants_block(vs, cols=None):
    cols = cols or (4 if len(vs) > 9 else 3)
    return f'''<div class="variants">
  <div class="v-head"><h3>Available sizes</h3><span>{len(vs)} item{'s' if len(vs) > 1 else ''} · Order by item code</span></div>
  {cards(vs, cols)}
</div>'''


def feature_page(k, p, c, n):
    apps = ''.join(f'<span>{E(a)}</span>' for a in p['apps'])
    return f'''<section class="sheet product feature" id="{k}">
{head(p['cat'], p['catname'])}
<div class="f-shot">{shot(p)}</div>
<div class="f-info">
  <div class="info">
    <span class="series">Series {E(p['series'])}</span>
    <h2>{E(p['name'])}</h2>
    <p class="sub">{E(p['sub'])}</p>
    <p class="tagline">{E(p['tagline'])}</p>
    <p class="desc">{E(p['desc'])}</p>
    <div class="apps"><span class="lbl">Applications</span>{apps}</div>
  </div>
  {spec_dl(p['specs'])}
</div>
<div class="block">
  <div class="b-head"><h3>Key features</h3><span>Why buyers choose it</span></div>
  {features(c['features'])}
</div>
{foot(n)}
</section>'''


PAIRS = {
    'split': ['bullet', 'channel', 'cantilever'], 'ubolt': ['channel', 'cantilever', 'wedge'],
    'sprinkler': ['bullet', 'butterfly', 'split'], 'gi': ['split', 'ubolt', 'ballvalve'],
    'cantilever': ['wedge', 'leaf', 'ubolt'], 'wedge': ['baseplate', 'cantilever', 'channel'],
    'butterfly': ['sprinkler', 'ballvalve', 'wedge'], 'ballvalve': ['gi', 'split', 'butterfly'],
    'baseplate': ['wedge', 'channel', 'leaf'], 'channel': ['baseplate', 'cantilever', 'leaf'],
    'bullet': ['sprinkler', 'split', 'ubolt'], 'pin': ['baseplate', 'cantilever', 'gi'],
}


def pairs_block(k, P):
    keys = PAIRS.get(k)
    if not keys or len(P[k]['variants']) > 11:
        return ''
    items = ''.join(
        f'<a class="pair" href="#{q}"><span class="g-img"><img src="images/web/{P[q]["img"]}" alt=""></span>'
        f'<span><b>{E(P[q]["name"])}</b><i>Series {E(P[q]["series"])}</i></span></a>' for q in keys)
    return f'''<div class="block pairs-block">
  <div class="b-head"><h3>Pairs well with</h3><span>Order together for a complete set</span></div>
  <div class="pairs">{items}</div>
</div>'''


def detail_page(k, p, c, n, P=None):
    tips = ''.join(f'<li>{E(t)}</li>' for t in c['tips'])
    return f'''<section class="sheet product detail" id="{k}-install">
{head(p['cat'], p['catname'], ' · ' + p['name'])}
<div class="d-title"><span class="series">Series {E(p['series'])}</span><h2>{E(p['name'])} <em>— installation &amp; ordering</em></h2></div>
<div class="d-grid">
  <div class="block">
    <div class="b-head"><h3>How to install</h3><span>{len(c['install'])} steps</span></div>
    {steps(c['install'])}
  </div>
  <aside class="tips">
    <h3>Buyer tips</h3>
    <ul>{tips}</ul>
  </aside>
</div>
{pairs_block(k, P) if P else ''}
{variants_block(p['variants'])}
{foot(n)}
</section>'''


def single_page(k, p, c, n, P=None):
    return f'''<section class="sheet product single" id="{k}">
{head(p['cat'], p['catname'])}
<div class="hero">
  {shot(p)}
  <div class="info">
    <span class="series">Series {E(p['series'])}</span>
    <h2>{E(p['name'])}</h2>
    <p class="sub">{E(p['sub'])}</p>
    <p class="desc">{E(p['desc'])}</p>
    {spec_dl(p['specs'])}
  </div>
</div>
<div class="s-grid">
  <div class="block">
    <div class="b-head"><h3>Key features</h3></div>
    {features(c['features'], 1)}
  </div>
  <div class="block">
    <div class="b-head"><h3>How to install</h3><span>{len(c['install'])} steps</span></div>
    {steps(c['install'])}
  </div>
</div>
{pairs_block(k, P) if P else ''}
{variants_block(p['variants'], 3)}
{foot(n)}
</section>'''


def guide_page(P, n):
    def comp(key, label=None):
        p = P[key]
        return (f'<div class="g-part"><div class="g-img"><img src="images/web/{p["img"]}" alt=""></div>'
                f'<b>{E(label or p["name"])}</b><span>{E(p["series"])}</span></div>')
    rod = '<div class="g-part"><div class="g-img g-rod"><span></span></div><b>Threaded rod</b><span>site supplied</span></div>'
    plug = '<div class="g-part"><div class="g-img g-rod g-plug"><span></span></div><b>Wall plug &amp; screw</b><span>site supplied</span></div>'
    sep = f'<i class="g-arrow">{ARROW}</i>'
    systems = [
        ('A', 'Ceiling-hung pipes', 'Pipes run below a concrete slab — plumbing, HVAC and fire sprinkler lines.',
         [comp('bullet'), rod, comp('split')], 'For sprinkler lines, use the Sprinkler Hanging Clamp (SH) in place of the split clamp.'),
        ('B', 'Wall-mounted racks', 'One or more pipes carried off a wall or column.',
         [comp('wedge'), comp('cantilever'), comp('leaf')], 'U-Bolt Clamps (UB) can be used on the arm instead of leaf clamps.'),
        ('C', 'Floor-standing frames', 'Posts and frames on a floor or roof slab — pump rooms, terraces, plant areas.',
         [comp('wedge'), comp('baseplate'), comp('channel'), comp('ubolt')], 'Leaf Clamps (LC) also lock directly into the channel.'),
        ('D', 'Surface-run pipes', 'Pipes fixed flat along walls and ceilings.',
         [comp('gi'), plug], 'Choose stainless steel clamps for wet or outdoor areas.'),
    ]
    blocks = []
    for code, title, desc, parts, note in systems:
        blocks.append(f'''<div class="g-sys">
  <div class="g-head"><span>{code}</span><div><h3>{E(title)}</h3><p>{E(desc)}</p></div></div>
  <div class="g-chain">{sep.join(parts)}</div>
  <p class="g-note">{E(note)}</p>
</div>''')
    return f'''<section class="sheet guide" id="system-guide">
{head('00', 'System guide')}
<div class="pg-intro">
  <span class="eyebrow dark">Planning a support system</span>
  <h2>How our parts<br>work together.</h2>
  <p class="lead">Most installations combine an anchor, a support and a clamp. These are the four set-ups our buyers use most — order the parts together and everything fits.</p>
</div>
<div class="g-list">{''.join(blocks)}</div>
{foot(n)}
</section>'''


SIZES = ['½″', '¾″', '1″', '1¼″', '1½″', '2″', '2½″', '3″', '4″', '5″', '6″', '8″', '10″', '12″']
NB = [15, 20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300]
STEEL = ['21.3', '26.9', '33.7', '42.4', '48.3', '60.3', '76.1', '88.9', '114.3', '139.7', '165.1', '219.1', '273.0', '323.9']
PPR = ['20', '25', '32', '40', '50', '63', '75', '90', '110', '—', '160', '200', '—', '—']
CPVC = ['15.9', '22.2', '28.6', '34.9', '41.3', '54.0', '—', '—', '—', '—', '—', '—', '—', '—']


def reference_page(P, n):
    cols = [('split', 'SC'), ('ubolt', 'UB'), ('leaf', 'LC'), ('sprinkler', 'SH'), ('gi', 'GC'), ('butterfly', 'BV'), ('ballvalve', 'UV')]
    avail = {k: {v['size'] for v in P[k]['variants']} for k, _ in cols}
    head_row = ''.join(f'<th class="dot-col">{E(code)}</th>' for _, code in cols)
    rows = []
    for i, s in enumerate(SIZES):
        dots = ''.join(f'<td class="dot-col">{"<i></i>" if s in avail[k] else ""}</td>' for k, _ in cols)
        rows.append(f'<tr><td class="sz">{s}</td><td>{NB[i]}</td><td>{STEEL[i]}</td><td>{PPR[i]}</td><td>{CPVC[i]}</td>{dots}</tr>')
    legend = ' · '.join(f'<b>{c}</b> {E(P[k]["name"])}' for k, c in cols)
    return f'''<section class="sheet reference" id="size-reference">
{head('00', 'Size reference')}
<div class="pg-intro">
  <span class="eyebrow dark">Choosing the right size</span>
  <h2>Pipe size<br>reference.</h2>
  <p class="lead">Clamps and valves are ordered by nominal pipe size. Use this chart to match a pipe's outside diameter to its size, and to see which products come in that size.</p>
</div>
<table class="ref-table">
  <thead>
    <tr><th colspan="5" class="grp">Pipe size &amp; outside diameter (mm)</th><th colspan="7" class="grp lime">Available in our range</th></tr>
    <tr><th>Size</th><th>NB (mm)</th><th>Steel / G.I.</th><th>PPR</th><th>CPVC</th>{head_row}</tr>
  </thead>
  <tbody>{''.join(rows)}</tbody>
</table>
<p class="ref-legend">{legend}</p>
<p class="ref-note"><b>Typical values.</b> Steel OD as per IS 1239 / ISO 65 medium series; PPR as per common metric sizing; CPVC as per CTS (ASTM D2846). Always confirm with your pipe supplier.</p>
{foot(n)}
</section>'''
