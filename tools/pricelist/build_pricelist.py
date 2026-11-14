"""Builds price-list-print.html (A4, catalogue styling) from the tables in catalogue.html,
so the PDF price list always matches the website price list.

Usage (from the repo root):
  python3 tools/pricelist/build_pricelist.py
Then print price-list-print.html to images/price-list-nov-2026.pdf
(A4, no margins, background graphics on) and delete price-list-print.html."""
import os, re, sys, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'catalogue'))
from pages import head, foot  # noqa: E402

E = html.escape
EDITION = 'Nov 2026'
src = open(os.path.join(ROOT, 'catalogue.html')).read()

# ---- read categories and products from the web price list
cats = []
for sec in re.finditer(r'<section class="cat-section" id="(\w+)" data-cat="\w+">(.*?)</section>', src, re.S):
    body = sec.group(2)
    num = re.search(r'<span class="num">(\d+)</span>', body).group(1)
    title = html.unescape(re.search(r'<h2>(.*?)</h2>', body).group(1))
    items = []
    for art in re.finditer(r'<article class="pl-item" id="([\w-]+)">(.*?)</article>', body, re.S):
        a = art.group(2)
        items.append(dict(
            id=art.group(1),
            code=re.search(r'<span class="p-code">(.*?)</span>', a).group(1),
            img=re.search(r'<img src="([^"]+)"', a).group(1),
            name=html.unescape(re.search(r'<h3>(.*?)</h3>', a).group(1)),
            desc=html.unescape(re.search(r'<p>(.*?)</p>', a).group(1)),
            tags=[html.unescape(t) for t in re.findall(r'<span(?: class="ink")?>([^<]+)</span>', re.search(r'<div class="pl-tags">(.*?)</div>', a).group(1))] if '<div class="pl-tags">' in a else [],
            table=re.search(r'(<table class="price-table">.*?</table>)', a, re.S).group(1),
            rows=len(re.findall(r'<tr>', re.search(r'<tbody>(.*?)</tbody>', a, re.S).group(1))),
        ))
    cats.append(dict(id=sec.group(1), num=num, title=title, items=items))

# ---- paginate (estimated heights in px on a 794 x 1123 sheet)
# measured in the browser: block = 76 + 26.4 px per row (min 144); category header ~62 px
CAP = 960
CAT_H, BLOCK_BASE, ROW_H = 62, 76, 26.4
def block_h(it):
    return max(BLOCK_BASE + it['rows'] * ROW_H, 144)

pages, cur, used = [], [], 0
for c in cats:
    for i, it in enumerate(c['items']):
        need = block_h(it)
        header_needed = i == 0 or not cur
        if header_needed:
            need += CAT_H
        if cur and used + need > CAP:
            pages.append(cur); cur, used = [], 0
            header_needed, need = True, block_h(it) + CAT_H
        if header_needed:
            cur.append(('cat', c, i > 0))
        cur.append(('item', it))
        used += need
pages.append(cur)

def item_html(it):
    tags = ''.join(f'<span class="badge{" ink" if t.startswith(("ISI", "Pin")) else ""}">{E(t)}</span>' for t in it['tags'])
    return f'''<div class="pl-block">
  <div class="pl-photo"><img src="{it['img']}" alt=""><span class="tick tl"></span><span class="tick br"></span></div>
  <div class="pl-main">
    <div class="pl-title"><span class="code">{E(it['code'])}</span><h3>{E(it['name'])}</h3>{tags}</div>
    {it['table']}
  </div>
</div>'''

def cat_html(c, cont):
    return f'<div class="pl-cat"><span>{c["num"]}</span><h2>{E(c["title"])}</h2>{"<em>continued</em>" if cont else ""}</div>'

body_pages = []
n = 2
for pg in pages:
    parts = []
    first_cat = next(e[1] for e in pg if e[0] == 'cat')
    for entry in pg:
        if entry[0] == 'cat':
            parts.append(cat_html(entry[1], entry[2]))
        else:
            parts.append(item_html(entry[1]))
    body_pages.append(f'''<section class="sheet pl-page">
{head(first_cat['num'], 'Price list · ' + EDITION)}
<div class="pl-body">{''.join(parts)}</div>
{foot(n).replace('Product Catalogue', 'Price List')}
</section>''')
    n += 1

last_n = n
cover = f'''<section class="sheet cover">
  <div class="cv-grid"></div>
  <div class="cv-top">
    <img class="cv-logo" src="images/web/logo-600.png" alt="TGV TRADLINK — The Plumbing House">
    <div class="cv-ed"><span>Rates effective</span><b>{EDITION}</b></div>
  </div>
  <div class="cv-title">
    <span class="eyebrow">Unit prices · sizes · packing</span>
    <h1>Price<br>List</h1>
    <p>Pipe clamps, support systems, anchor fasteners &amp; valves. Ex-warehouse Rajkot. GST extra.</p>
  </div>
  <div class="pl-index">
    {''.join(f'<div><span>{c["num"]}</span><b>{E(c["title"])}</b><i>{len(c["items"])} product{"s" if len(c["items"]) > 1 else ""}</i></div>' for c in cats)}
  </div>
  <div class="cv-foot">
    <span><i>Enquiries</i>+91 82002 98971</span>
    <span><i>Email</i>info.tgvtradlink@gmail.com</span>
    <span><i>Specifications</i>See our Product Catalogue</span>
  </div>
</section>'''

NOTE = '''  <div class="pl-note">
    <h3>Price notes</h3>
    <ul>
      <li>Prices are indicative, ex-warehouse (Rajkot), for standard quantities.</li>
      <li>Bulk discounts apply on orders above ₹25,000.</li>
      <li>GST extra as per prevailing rates. Freight extra.</li>
      <li>“—” means the size is not available in that variant.</li>
      <li>Custom specifications, alternate materials and special coatings available on request.</li>
    </ul>
  </div>
'''
body_pages[-1] = body_pages[-1].replace('</div>\n<footer', NOTE + '</div>\n<footer', 1)

terms = f'''<section class="sheet terms pl-terms">
{head('05', 'Notes & terms')}
<div class="tm-body">
  <span class="eyebrow dark">Effective April 2026</span>
  <h2>Terms &amp; conditions<br>of sale.</h2>
  <div class="tm-grid">
    <div><span>01</span><h3>Quotations &amp; orders</h3><ul><li>Quotations are valid for 7 calendar days from issue unless otherwise stated.</li><li>Orders are confirmed only on receipt of a written purchase order and advance payment.</li><li>Formal quotations reflect GST, freight and current material costs.</li></ul></div>
    <div><span>02</span><h3>Payment terms</h3><ul><li>50% advance with order; balance before dispatch, unless credit terms are pre-agreed in writing.</li><li>Approved accounts may receive 30-day credit, subject to management approval.</li><li>Payment in Indian Rupees by NEFT / RTGS / cheque in favour of TGV TRADLINK.</li></ul></div>
    <div><span>03</span><h3>Delivery &amp; freight</h3><ul><li>Ex-warehouse (Rajkot) unless otherwise stated. Freight is borne by the Buyer.</li><li>Delivery timelines are estimates; the Seller is not liable for delays caused by logistics or force majeure.</li><li>Risk and title pass to the Buyer on dispatch from our warehouse.</li></ul></div>
    <div><span>04</span><h3>Returns &amp; claims</h3><ul><li>Returns accepted within 7 days of delivery for manufacturing defects only, with prior written authorisation.</li><li>No returns on custom-fabricated, non-standard or specially ordered products.</li></ul></div>
    <div><span>05</span><h3>Quality &amp; warranty</h3><ul><li>Products conform to specified IS / DIN / ASTM standards unless otherwise agreed.</li><li>Warranty is limited to replacement or credit for manufacturing defects notified within 30 days.</li></ul></div>
    <div class="tm-note"><span>☎</span><h3>Formal quotation</h3><ul><li>+91 82002 98971 / 81603 09471</li><li>info.tgvtradlink@gmail.com</li><li>Arihant Avenue, Near Nageshwar Jain Temple, Rajkot 360006</li></ul></div>
  </div>
</div>
{foot(last_n).replace('Product Catalogue', 'Price List')}
</section>'''

CSS = open(os.path.join(ROOT, 'tools', 'catalogue', 'catalogue.css')).read() + '''
/* ── Price list sheets ── */
.pl-body { padding-top: 6px; }
.pl-cat { display: flex; align-items: center; gap: 10px; margin: 18px 0 10px; padding-bottom: 8px; border-bottom: 1.5px solid var(--ink); }
.pl-cat span { font-family: var(--mono); font-size: 11px; font-weight: 700; background: var(--lime); padding: 2px 7px; border-radius: 2px; }
.pl-cat h2 { font-size: 24px; font-weight: 900; font-stretch: 76%; text-transform: uppercase; line-height: 1; }
.pl-cat em { font-style: normal; font-family: var(--mono); font-size: 9px; color: var(--muted); margin-left: auto; }
.pl-block { display: grid; grid-template-columns: 120px 1fr; gap: 16px; padding: 10px 0 14px; border-bottom: 1px dashed var(--line); break-inside: avoid; }
.pl-block:last-child { border-bottom: 0; }
.pl-photo { position: relative; width: 120px; height: 120px; background: var(--photo); border-radius: 3px; overflow: hidden; }
.pl-photo img { width: 100%; height: 100%; object-fit: cover; mix-blend-mode: multiply; }
.pl-photo .tick { width: 10px; height: 10px; }
.pl-photo .tick.tl { top: 6px; left: 6px; } .pl-photo .tick.br { bottom: 6px; right: 6px; }
.pl-title { display: flex; align-items: center; gap: 8px; margin-bottom: 7px; }
.pl-title .code { font-family: var(--mono); font-size: 9.5px; font-weight: 700; color: var(--muted); }
.pl-title h3 { font-size: 17px; font-weight: 900; font-stretch: 80%; text-transform: uppercase; line-height: 1; }
.price-table { width: 100%; border-collapse: collapse; font-size: 11px; font-variant-numeric: tabular-nums; }
.price-table th { background: var(--ink); color: var(--paper); font-family: var(--mono); font-size: 8.5px; font-weight: 500; letter-spacing: .05em; text-transform: uppercase; text-align: left; padding: 7px 9px; white-space: nowrap; }
.price-table th:first-child { border-radius: 3px 0 0 0; } .price-table th:last-child { border-radius: 0 3px 0 0; }
.price-table td { padding: 5.5px 9px; border-bottom: 1px solid var(--line); white-space: nowrap; }
.price-table tbody tr:nth-child(even) td { background: var(--paper); }
.price-table td:first-child { font-weight: 600; }
.price-table td.price-cell { font-family: var(--mono); font-weight: 700; }
.price-table td.na { color: #b4b6ab; }
.pl-index { position: relative; margin-top: 44px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.pl-index div { border: 1px solid var(--line-d); border-radius: 4px; padding: 16px 18px; display: grid; grid-template-columns: auto 1fr; column-gap: 12px; }
.pl-index span { grid-row: span 2; font-family: var(--mono); font-weight: 700; font-size: 12px; background: var(--lime); color: var(--ink); padding: 3px 7px; border-radius: 2px; align-self: start; }
.pl-index b { font-size: 17px; font-weight: 900; font-stretch: 80%; text-transform: uppercase; }
.pl-index i { font-style: normal; font-family: var(--mono); font-size: 9.5px; color: var(--muted-d); }
.pl-note { background: var(--ink); color: var(--paper); border-radius: 4px; padding: 16px 20px 18px; margin-bottom: 26px; }
.pl-note h3 { font-size: 18px; font-weight: 900; font-stretch: 78%; text-transform: uppercase; color: var(--lime); margin-bottom: 6px; }
.pl-note li { position: relative; padding: 4px 0 4px 14px; font-size: 11.5px; color: #d6d8cc; }
.pl-note li::before { content: ''; position: absolute; left: 0; top: 10px; width: 5px; height: 5px; background: var(--lime); }
.pl-terms h2 { font-size: 40px; }
.pl-body .pl-note { margin: 22px 0 0; }
'''

doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Price List {EDITION} | TGV TRADLINK</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head>
<body><main class="book">
{cover}
{''.join(body_pages)}
{terms}
</main></body></html>'''
open(os.path.join(ROOT, 'price-list-print.html'), 'w').write(doc)
print('pages', 2 + len(body_pages), 'products', sum(len(c['items']) for c in cats))
