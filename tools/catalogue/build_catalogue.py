"""Builds product-catalogue.html (A4 pages, no prices) for TGV TRADLINK.
Product list and specs come from price-list-nov-2026.pdf only.

Usage (from the repo root):
  python3 tools/catalogue/build_catalogue.py product-catalogue.html tools/catalogue/catalogue.css
Then re-export images/product-catalogue-nov-2026.pdf by printing the page to PDF
(A4, no margins, background graphics on)."""
import sys, html

OUT = sys.argv[1]
E = html.escape

IN = {'1/2': '½″', '3/4': '¾″', '1': '1″', '1.1/4': '1¼″', '1.1/2': '1½″', '2': '2″', '2.1/2': '2½″',
      '3': '3″', '4': '4″', '5': '5″', '6': '6″', '8': '8″', '10': '10″', '12': '12″'}

def series(prefix, start, rows):
    return [dict(code=f'{prefix}-{start + i}', **r) for i, r in enumerate(rows)]

sizes11 = ['1/2', '3/4', '1', '1.1/4', '1.1/2', '2', '2.1/2', '3', '4', '6', '8']
packs11 = [550, 500, 450, 350, 300, 285, 250, 215, 150, 100, 80]

P = {}
P['split'] = dict(
    cat='01', catname='Pipe clamps', name='Split Clamp', sub='with EPDM rubber lining', series='SC-100',
    img='split-clamp.jpg', badges=['Bestseller'],
    tagline='Grip that stays put.',
    desc='Two-piece split clamp lined with EPDM rubber. The lining grips the pipe firmly, absorbs vibration and noise, and protects the pipe surface. Closed with screws and hung from a threaded boss.',
    specs=[('Type', 'Two-piece split clamp'), ('Lining', 'EPDM rubber'), ('Strip', '2.0 × 20 mm'),
           ('Size range', '½″ – 8″ (11 sizes)'), ('Packing', '80 – 550 nos per box')],
    apps=['Plumbing', 'HVAC', 'Fire-fighting', 'Drainage'],
    variants=series('SC', 101, [dict(size=IN[s], spec='2.0 × 20 mm strip', pack=f'{p} nos') for s, p in zip(sizes11, packs11)]))

P['ubolt'] = dict(
    cat='01', catname='Pipe clamps', name='U-Bolt Clamp', sub='with EPDM rubber, washer & nut', series='UB-200',
    img='u-bolt-clamp.jpg', badges=['Bestseller'],
    tagline='The everyday workhorse.',
    desc='U-bolt formed from 8 mm rod and sleeved in ribbed EPDM rubber for a secure, quiet grip that will not scratch the pipe. Supplied with washers and nuts, ready to fix.',
    specs=[('Type', 'U-bolt with washer & nut'), ('Rod', '8 mm'), ('Sleeve', 'Ribbed EPDM rubber'),
           ('Size range', '½″ – 8″ (11 sizes)'), ('Packing', '80 – 550 nos per box')],
    apps=['Plumbing', 'HVAC', 'Solar lines', 'Industrial piping'],
    variants=series('UB', 201, [dict(size=IN[s], spec='8 mm rod', pack=f'{p} nos') for s, p in zip(sizes11, packs11)]))

leaf = [('1.5', '1/2', 75), ('1.5', '1', 80), ('1.5', '1.1/4', 85), ('1.5', '1.1/2', 90), ('1.5', '2', 95),
        ('1.5', '2.1/2', 110), ('1.5', '3', 125), ('2', '4', 150), ('2', '5', 175), ('2', '6', 200),
        ('2', '8', 260), ('2', '10', 320), ('2', '12', 380)]
P['leaf'] = dict(
    cat='01', catname='Pipe clamps', name='Leaf Clamp', sub='heavy-duty strip clamp', series='LC-300',
    img='leaf-clamp.jpg', badges=['Bestseller'],
    tagline='Built for the big lines.',
    desc='Heavy-duty clamp formed from 32 mm wide strip with a bolted closure, for firm holding of larger pipes. 1.5 mm strip up to 3″ and 2 mm strip from 4″ upward.',
    specs=[('Type', 'Bolted leaf clamp'), ('Strip width', '32 mm'), ('Thickness', '1.5 mm (½″–3″) · 2 mm (4″–12″)'),
           ('Size range', '½″ – 12″ (13 sizes)'), ('Length', '75 – 380 mm')],
    apps=['Mains & risers', 'Fire-fighting', 'Industrial piping'],
    variants=series('LC', 301, [dict(size=IN[s], spec=f'{t} × 32 mm strip', pack=f'Length {l} mm') for t, s, l in leaf]))

spr = [('1', 32, 450), ('1.1/4', 40, 350), ('1.1/2', 50, 300), ('2', 63, 285), ('2.1/2', 75, 250),
       ('3', 90, 215), ('4', 110, 150), ('6', 160, 100), ('8', 200, 80)]
P['sprinkler'] = dict(
    cat='01', catname='Pipe clamps', name='Sprinkler Hanging Clamp', sub='band hanger for fire lines', series='SH-400',
    img='sprinkler-clamp.jpg', badges=[],
    tagline='Made for fire safety lines.',
    desc='Teardrop-style band hanger that carries sprinkler pipes from a threaded drop rod. Quick to install and adjust. Available in two gauges for light and heavy runs.',
    specs=[('Type', 'Band hanger'), ('Gauge', '2 mm (14G) · 1.5 mm (16G)'), ('Pipe size', '1″ – 8″ (Ø 32 – 200 mm)'),
           ('Mounting', 'Threaded drop rod'), ('Packing', '80 – 450 nos per box')],
    apps=['Fire sprinkler', 'Fire hydrant', 'Plumbing'],
    variants=series('SH', 401, [dict(size=IN[s], spec=f'Ø {mm} mm · 14G / 16G', pack=f'{p} nos') for s, mm, p in spr]))

gi = [('1/2', 15), ('3/4', 20), ('1', 25), ('1.1/4', 32), ('1.1/2', 40), ('2', 50), ('2.1/2', 65), ('3', 80), ('4', 100), ('6', 150)]
P['gi'] = dict(
    cat='01', catname='Pipe clamps', name='G.I. & S.S. Clamp', sub='saddle pipe clamps', series='GC-500',
    img='gi-ss-clamp.jpg', badges=[],
    tagline='Clean fixing, wall to wall.',
    desc='Saddle-type clamps for fixing pipes to walls and ceilings. Galvanised iron in two thicknesses for general use, and stainless steel for corrosive or exposed locations.',
    specs=[('Type', 'Saddle clamp'), ('Material', 'G.I. 1.2 mm · G.I. 1.5 mm · S.S. 1.0 mm'),
           ('Size range', '½″ – 6″ (15 – 150 mm)'), ('Finish', 'Galvanised / stainless'), ('Sizes', '10')],
    apps=['Plumbing', 'Electrical conduit', 'Gas lines'],
    variants=series('GC', 501, [dict(size=IN[s], spec=f'{mm} mm pipe', pack='GI 1.2 · GI 1.5 · SS 1.0') for s, mm in gi]))

P['cantilever'] = dict(
    cat='02', catname='Support systems', name='Cantilever', sub='channel arm with base plate', series='CL-700',
    img='cantilever.jpg', badges=['Bestseller'],
    tagline='Reach out. Hold firm.',
    desc='41 × 41 mm slotted channel arm welded to a base plate, for mounting pipes, cable trays and services off walls and columns. Slotted face accepts standard channel fittings.',
    specs=[('Profile', '41 × 41 mm slotted channel'), ('Thickness', '2 mm'), ('Length', '150 – 750 mm (7 sizes)'),
           ('Mounting', 'Welded base plate'), ('Use with', 'Channel nuts, clamps & brackets')],
    apps=['Pipe racks', 'Cable trays', 'HVAC', 'MEP services'],
    variants=series('CL', 701, [dict(size=f'{l} mm', spec='41 × 41 mm · 2 mm', pack='Arm length') for l in [150, 200, 250, 300, 450, 600, 750]]))

P['baseplate'] = dict(
    cat='02', catname='Support systems', name='Base Plate', sub='channel base', series='BP-600',
    img='base-plate.jpg', badges=['Bestseller'],
    desc='Heavy-duty 4 mm plate with channel socket for stable floor or ceiling anchoring of channel supports.',
    specs=[('Plate', '150 × 150 mm'), ('Thickness', '4 mm'), ('Fixing', 'Anchor bolts (4 holes)')],
    variants=[dict(code='BP-601', size='150 × 150', spec='4 mm plate', pack='Per piece')])

P['channel'] = dict(
    cat='02', catname='Support systems', name='Slotted Channel', sub='strut channel', series='CH-800',
    img='slotted-channel.jpg', badges=['Bestseller'],
    desc='41 × 41 mm slotted strut channel for building modular support frames — cut to length and bolt together on site.',
    specs=[('Profile', '41 × 41 mm'), ('Thickness', '2 mm'), ('Face', 'Slotted for channel fittings')],
    variants=[dict(code='CH-801', size='41 × 41', spec='2 mm', pack='Per length')])

P['bullet'] = dict(
    cat='03', catname='Anchor fasteners', name='Bullet Anchor', sub='expansion anchor', series='BA-900',
    img='bullet-anchor.jpg', badges=[],
    desc='Compact expansion anchor for dependable fixing of rods and bolts in solid concrete.',
    specs=[('Sizes', '8 · 10 · 12 mm'), ('Base material', 'Solid concrete'), ('Packing', '100 nos per box')],
    variants=series('BA', 901, [dict(size=f'{d} mm', spec='Bullet anchor', pack='100 nos') for d in (8, 10, 12)]))

P['pin'] = dict(
    cat='03', catname='Anchor fasteners', name='Pin Type Anchor', sub='quick-set anchor', series='PA-910',
    img='pin-anchor.jpg', badges=[],
    desc='Quick-set anchor that expands as the pin is driven home — fast, secure fixing with excellent holding strength.',
    specs=[('Sizes', '10 × 60 · 10 × 75 mm'), ('Base material', 'Concrete'), ('Packing', '100 nos per box')],
    variants=series('PA', 911, [dict(size=s, spec='Pin type', pack='100 nos') for s in ('10 × 60', '10 × 75')]))

wedge = [('10 × 75', 125), ('10 × 100', 125), ('10 × 125', 125), ('12 × 75', 125), ('12 × 100', 150),
         ('12 × 125', 150), ('12 × 150', 150), ('12 × 200', 150)]
P['wedge'] = dict(
    cat='03', catname='Anchor fasteners', name='Wedge Anchor', sub='through-bolt anchor', series='WA-920',
    img='wedge-anchor.jpg', badges=[],
    tagline='Set once. Holds for good.',
    desc='High-strength through-bolt anchor. The wedge clip expands as the nut is tightened, giving a permanent, heavy-duty fixing in concrete for structural supports and machinery.',
    specs=[('Type', 'Through-bolt wedge anchor'), ('Diameter', '10 mm · 12 mm'), ('Length', '75 – 200 mm'),
           ('Supplied with', 'Nut & washer'), ('Packing', '125 – 150 nos per box')],
    apps=['Pipe supports', 'Channel frames', 'Machinery', 'Structural'],
    variants=series('WA', 921, [dict(size=f'{s} mm', spec='Wedge anchor', pack=f'{p} nos') for s, p in wedge]))

P['butterfly'] = dict(
    cat='04', catname='Valves', name='C.I. Body Butterfly Valve', sub='with S.S. 304 disc', series='BV-1000',
    img='butterfly-valve.jpg', badges=['ISI marked'],
    tagline='Flow control you can certify.',
    desc='Cast iron body butterfly valve with a stainless steel 304 disc for strength and corrosion resistance. ISI marked, and offered in Poline and Meet brands.',
    specs=[('Body', 'Cast iron (C.I.)'), ('Disc', 'Stainless steel 304'), ('Certification', 'ISI marked'),
           ('Brands', 'Poline · Meet'), ('Size range', '1½″ – 8″ (8 sizes)')],
    apps=['Fire-fighting', 'Water supply', 'HVAC', 'Industrial'],
    variants=series('BV', 1001, [dict(size=IN[s], spec='C.I. body · S.S. 304', pack='Poline · Meet') for s in ['1.1/2', '2', '2.1/2', '3', '4', '5', '6', '8']]))

ball = [('1/2', 'PPR · UPVC'), ('3/4', 'PPR · CPVC · UPVC'), ('1', 'PPR · CPVC · UPVC'), ('1.1/4', 'CPVC · UPVC'),
        ('1.1/2', 'PPR · CPVC · UPVC'), ('2', 'CPVC · UPVC')]
P['ballvalve'] = dict(
    cat='04', catname='Valves', name='Double Union Ball Valve', sub='brass ball, union ends', series='UV-1100',
    img='union-ball-valve.jpg', badges=[],
    tagline='Fit it. Service it. Easily.',
    desc='Ball valve with double union ends that lets the valve be removed for service without cutting the line. Available for PPR, CPVC and UPVC pipe systems.',
    specs=[('Type', 'Double union ball valve'), ('Ball', 'Brass'), ('Pipe systems', 'PPR · CPVC · UPVC'),
           ('Size range', '½″ – 2″ (6 sizes)'), ('Operation', 'Quarter-turn lever')],
    apps=['Plumbing', 'Water supply', 'Chemical lines'],
    variants=series('UV', 1101, [dict(size=IN[s], spec='Brass ball valve', pack=v) for s, v in ball]))

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import C
from pages import head, foot, feature_page, detail_page, single_page, guide_page, reference_page

CATS = [('01', 'Pipe clamps', ['split', 'ubolt', 'leaf', 'sprinkler', 'gi']),
        ('02', 'Support systems', ['cantilever', 'baseplate', 'channel']),
        ('03', 'Anchor fasteners', ['bullet', 'pin', 'wedge']),
        ('04', 'Valves', ['butterfly', 'ballvalve'])]
SINGLE = {'baseplate', 'channel', 'bullet', 'pin'}
ORDER = [k for _, _, ks in CATS for k in ks]

# 1 cover, 2 about, 3 contents, 4 system guide, 5 size reference, then products
GUIDE_PAGE, REF_PAGE = 4, 5
page_of, n = {}, 6
for k in ORDER:
    page_of[k] = n
    n += 1 if k in SINGLE else 2
TERMS_PAGE = n
TOTAL = TERMS_PAGE + 1

cover = '''<section class="sheet cover">
  <div class="cv-grid"></div>
  <div class="cv-top">
    <img class="cv-logo" src="images/web/logo-600.png" alt="TGV TRADLINK — The Plumbing House">
    <div class="cv-ed"><span>Edition</span><b>Nov 2026</b></div>
  </div>
  <div class="cv-title">
    <span class="eyebrow">Product specifications &amp; technical data</span>
    <h1>Product<br>Catalogue</h1>
    <p>Pipe clamps, support systems, anchor fasteners &amp; valves — engineered to hold, built to last.</p>
  </div>
  <div class="cv-mosaic">
    <div><img src="images/web/split-clamp.jpg" alt=""></div>
    <div><img src="images/web/cantilever.jpg" alt=""></div>
    <div><img src="images/web/u-bolt-clamp.jpg" alt=""></div>
  </div>
  <div class="cv-foot">
    <span><i>Products</i>13 products · 90 items</span>
    <span><i>Supply</i>Pan-India from Rajkot</span>
    <span><i>Enquiries</i>+91 82002 98971</span>
  </div>
</section>'''

about = f'''<section class="sheet about">
{head('00', 'About us')}
<div class="ab-body">
  <span class="eyebrow dark">Our story</span>
  <h2>Hardware you can<br>build on.</h2>
  <div class="ab-cols">
    <div>
      <p class="lead">TGV TRADLINK is a manufacturer and wholesale distributor of industrial plumbing support hardware — clamps, U-bolts, EPDM rubber products, channel supports, anchor fasteners and valves.</p>
      <p>We supply contractors, engineers and industrial procurement teams across India. By keeping control of quality at every stage — from raw material to finished product — we cut out middlemen and pass the cost advantage straight to our buyers.</p>
      <p>Whether you need standard bulk orders or custom hardware made to your drawings, we deliver with precision, accountability and speed.</p>
    </div>
    <figure><img src="images/web/facility.jpg" alt="TGV TRADLINK facility"><figcaption>Rajkot, Gujarat — warehouse &amp; dispatch</figcaption></figure>
  </div>
  <div class="ab-stats">
    <div><b>10+</b><span>Years experience</span></div>
    <div><b>200+</b><span>Clients served</span></div>
    <div><b>90</b><span>Catalogue items</span></div>
    <div><b>PAN</b><span>India delivery</span></div>
  </div>
  <div class="ab-pillars">
    <div><b>Certified quality</b><span>Products conform to IS, DIN and ASTM standards.</span></div>
    <div><b>Factory direct</b><span>No middlemen — competitive, transparent pricing.</span></div>
    <div><b>Custom orders</b><span>Non-standard sizes fabricated on request.</span></div>
    <div><b>Every batch checked</b><span>Inspected before it leaves our warehouse.</span></div>
  </div>
</div>
{foot(2)}
</section>'''

toc_rows = [f'<div class="toc-cat"><span>00</span>Planning</div>',
            f'<a class="toc-item" href="#system-guide"><span class="t-name">System guide<i>how our parts work together</i></span><span class="t-code"></span><span class="t-dots"></span><b>{GUIDE_PAGE:02d}</b></a>',
            f'<a class="toc-item" href="#size-reference"><span class="t-name">Pipe size reference<i>sizes, outside diameters, availability</i></span><span class="t-code"></span><span class="t-dots"></span><b>{REF_PAGE:02d}</b></a>']
for c, cname, keys in CATS:
    toc_rows.append(f'<div class="toc-cat"><span>{c}</span>{E(cname)}</div>')
    for k in keys:
        p = P[k]
        toc_rows.append(f'<a class="toc-item" href="#{k}"><span class="t-name">{E(p["name"])}<i>{E(p["sub"])}</i></span>'
                        f'<span class="t-code">{E(p["series"])}</span><span class="t-dots"></span><b>{page_of[k]:02d}</b></a>')
toc_rows.append(f'<div class="toc-cat"><span>05</span>Ordering</div><a class="toc-item" href="#terms"><span class="t-name">Terms &amp; conditions<i>quotations, payment, delivery, returns</i></span><span class="t-code"></span><span class="t-dots"></span><b>{TERMS_PAGE:02d}</b></a>')

contents = f'''<section class="sheet contents">
{head('00', 'Contents')}
<div class="toc-wrap">
  <div class="toc-side"><span class="toc-word">Contents</span></div>
  <div class="toc-list">{''.join(toc_rows)}</div>
</div>
<p class="toc-note">How to order: quote the <b>item code</b> printed with each size (for example <b>SC-106</b> = Split Clamp 2″). Current rates are in our separate price list.</p>
{foot(3)}
</section>'''

terms = f'''<section class="sheet terms" id="terms">
{head('05', 'Ordering')}
<div class="tm-body">
  <span class="eyebrow dark">Effective April 2026</span>
  <h2>Terms &amp; conditions<br>of sale.</h2>
  <p class="lead">These terms govern all transactions between TGV TRADLINK (“Seller”) and the Buyer. By placing an order, the Buyer accepts them in full.</p>
  <div class="tm-grid">
    <div><span>01</span><h3>Quotations &amp; orders</h3><ul><li>Quotations are valid for 7 calendar days from issue unless otherwise stated.</li><li>Orders are confirmed only on receipt of a written purchase order and advance payment.</li><li>Formal quotations reflect GST, freight and current material costs.</li></ul></div>
    <div><span>02</span><h3>Payment terms</h3><ul><li>50% advance with order; balance before dispatch, unless credit terms are pre-agreed in writing.</li><li>Approved accounts may receive 30-day credit, subject to management approval.</li><li>Payment in Indian Rupees by NEFT / RTGS / cheque in favour of TGV TRADLINK.</li></ul></div>
    <div><span>03</span><h3>Delivery &amp; freight</h3><ul><li>Ex-warehouse (Rajkot) unless otherwise stated. Freight is borne by the Buyer.</li><li>Delivery timelines are estimates; the Seller is not liable for delays caused by logistics or force majeure.</li><li>Risk and title pass to the Buyer on dispatch from our warehouse.</li></ul></div>
    <div><span>04</span><h3>Returns &amp; claims</h3><ul><li>Returns accepted within 7 days of delivery for manufacturing defects only, with prior written authorisation.</li><li>No returns on custom-fabricated, non-standard or specially ordered products.</li></ul></div>
    <div><span>05</span><h3>Quality &amp; warranty</h3><ul><li>Products conform to specified IS / DIN / ASTM standards unless otherwise agreed.</li><li>Warranty is limited to replacement or credit for manufacturing defects notified within 30 days.</li></ul></div>
    <div class="tm-note"><span>i</span><h3>Specifications</h3><ul><li>Dimensions are nominal. Images are representative.</li><li>Custom sizes, materials and coatings available on request.</li><li>Specifications may change without notice as we improve our range.</li></ul></div>
  </div>
</div>
{foot(TERMS_PAGE)}
</section>'''

back = '''<section class="sheet back">
  <div class="cv-grid"></div>
  <div class="bk-main">
    <img class="bk-logo" src="images/web/logo-600.png" alt="TGV TRADLINK">
    <h2>Let's talk<br><span>business.</span></h2>
    <dl class="bk-contact">
      <div><dt>Phone</dt><dd>+91 82002 98971<br>+91 81603 09471</dd></div>
      <div><dt>Email</dt><dd>info.tgvtradlink@gmail.com</dd></div>
      <div><dt>Address</dt><dd>Arihant Avenue, Near Nageshwar Jain Temple,<br>Rajkot, Gujarat 360006, India</dd></div>
      <div><dt>Hours</dt><dd>Mon – Sat, 9:00 AM – 8:30 PM</dd></div>
      <div><dt>Web</dt><dd>tgv-tradlink.github.io</dd></div>
    </dl>
  </div>
  <div class="bk-foot"><span>Your dealer stamp</span><span>Product Catalogue · Nov 2026</span></div>
</section>'''

product_pages = [guide_page(P, GUIDE_PAGE), reference_page(P, REF_PAGE)]
for k in ORDER:
    if k in SINGLE:
        product_pages.append(single_page(k, P[k], C[k], page_of[k], P))
    else:
        product_pages.append(feature_page(k, P[k], C[k], page_of[k]))
        product_pages.append(detail_page(k, P[k], C[k], page_of[k] + 1, P))

CSS = open(sys.argv[2]).read()

doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Product Catalogue | TGV TRADLINK — Clamps, Supports, Anchors &amp; Valves</title>
<meta name="description" content="TGV TRADLINK product catalogue: detailed specifications, sizes, item codes and packing for split clamps, U-bolt clamps, leaf clamps, sprinkler clamps, G.I. & S.S. clamps, cantilevers, channels, anchors and valves.">
<meta name="theme-color" content="#0d0e0b">
<link rel="canonical" href="https://tgv-tradlink.github.io/product-catalogue.html">
<link rel="icon" type="image/png" href="images/web/logo-200.png">
<meta property="og:title" content="TGV TRADLINK | Product Catalogue">
<meta property="og:description" content="Specifications, sizes and item codes for industrial clamps, supports, anchors and valves.">
<meta property="og:image" content="https://tgv-tradlink.github.io/images/TGV_logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<nav class="viewer-bar">
  <a href="index.html" class="vb-back"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 18l-6-6 6-6"/></svg><span>Back to site</span></a>
  <span class="vb-title">Product Catalogue · Nov 2026 · {TOTAL} pages</span>
  <div class="vb-actions">
    <a href="catalogue.html" class="vb-btn ghost">Price list</a>
    <a href="images/product-catalogue-nov-2026.pdf" download class="vb-btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>Download PDF</a>
  </div>
</nav>
<main class="book">
{cover}
{about}
{contents}
{''.join(product_pages)}
{terms}
{back}
</main>
<script>
(function () {{
  var fit = function () {{
    var w = Math.min(1, (window.innerWidth - 24) / 794);
    document.documentElement.style.setProperty('--z', w.toFixed(4));
  }};
  fit(); window.addEventListener('resize', fit);
}})();
</script>
</body>
</html>'''

open(OUT, 'w').write(doc)
print('pages', TOTAL, 'items', sum(len(p['variants']) for p in P.values()))
