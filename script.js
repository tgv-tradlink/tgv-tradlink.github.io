/* ============================================================
   TGV TRADLINK — script.js (shared by index.html & catalogue.html)
============================================================ */
document.documentElement.classList.remove('no-js');

document.addEventListener('DOMContentLoaded', () => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Header state ─────────────────────────────────── */
  const header = $('#header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── Mobile menu ──────────────────────────────────── */
  const menuBtn = $('#hamburger');
  const mobileNav = $('#mobileNav');
  const setMenu = open => {
    if (!menuBtn || !mobileNav) return;
    menuBtn.setAttribute('aria-expanded', String(open));
    mobileNav.classList.toggle('open', open);
    document.body.classList.toggle('nav-open', open);
  };
  if (menuBtn) {
    menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
    $$('a', mobileNav).forEach(a => a.addEventListener('click', () => setMenu(false)));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', () => { if (window.innerWidth > 1080) setMenu(false); });
  }

  /* ── Active nav link ──────────────────────────────── */
  const navLinks = $$('.nav a[href^="#"]');
  if (navLinks.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + entry.target.id));
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    $$('section[id]').forEach(s => io.observe(s));
  }

  /* ── Smooth anchor scroll with header offset ──────── */
  $$('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href');
      if (id.length < 2) return;
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      const offset = (header ? header.offsetHeight : 0) + (a.dataset.offset ? +a.dataset.offset : 0);
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - offset, behavior: reduceMotion ? 'auto' : 'smooth' });
      history.replaceState(null, '', id);
    });
  });

  /* ── Reveal on scroll ─────────────────────────────── */
  const revealIO = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); revealIO.unobserve(entry.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal').forEach(el => revealIO.observe(el));

  /* ── Stat counters ────────────────────────────────── */
  const counters = $$('[data-count]');
  if (counters.length) {
    const run = el => {
      const target = +el.dataset.count;
      if (reduceMotion) { el.textContent = target; return; }
      const start = performance.now(), dur = 1300;
      const tick = now => {
        const p = Math.min((now - start) / dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    const cIO = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { run(e.target); cIO.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(c => cIO.observe(c));
  }

  /* ── Hero spec card rotator ───────────────────────── */
  const spec = $('#specCard');
  if (spec) {
    const slides = JSON.parse(spec.dataset.slides);
    const imgs = $$('.spec-stage img', spec);
    const dots = $$('.spec-dots button', spec);
    const name = $('[data-spec="name"]', spec);
    const specs = $('[data-spec="specs"]', spec);
    const price = $('[data-spec="price"]', spec);
    const code = $('[data-spec="code"]', spec);
    let i = 0, timer;
    const show = n => {
      i = (n + slides.length) % slides.length;
      imgs.forEach((im, k) => im.classList.toggle('on', k === i));
      dots.forEach((d, k) => { d.classList.toggle('on', k === i); d.setAttribute('aria-pressed', k === i); });
      name.textContent = slides[i].name;
      specs.textContent = slides[i].specs;
      price.textContent = slides[i].price;
      code.textContent = slides[i].code;
    };
    const play = () => { if (!reduceMotion) { clearInterval(timer); timer = setInterval(() => show(i + 1), 3800); } };
    dots.forEach((d, k) => d.addEventListener('click', () => { show(k); play(); }));
    spec.addEventListener('mouseenter', () => clearInterval(timer));
    spec.addEventListener('mouseleave', play);
    show(0); play();
  }

  /* ── Product filter (home) ────────────────────────── */
  const filterBar = $('#productFilters');
  if (filterBar) {
    const cards = $$('#productGrid .p-card');
    filterBar.addEventListener('click', e => {
      const chip = e.target.closest('.chip');
      if (!chip) return;
      $$('.chip', filterBar).forEach(c => { c.classList.toggle('on', c === chip); c.setAttribute('aria-pressed', c === chip); });
      const f = chip.dataset.filter;
      cards.forEach(card => { card.hidden = f !== 'all' && card.dataset.cat !== f; });
    });
  }

  /* ── Price list: category jump + search ───────────── */
  const plFilters = $('#plFilters');
  const plSearch = $('#plSearch');
  if (plFilters || plSearch) {
    const sections = $$('.cat-section');
    const items = $$('.pl-item');
    const empty = $('#plEmpty');
    let cat = 'all';
    const apply = () => {
      const q = (plSearch ? plSearch.value : '').trim().toLowerCase();
      let shown = 0;
      sections.forEach(sec => {
        const catOk = cat === 'all' || sec.dataset.cat === cat;
        let visible = 0;
        $$('.pl-item', sec).forEach(it => {
          const ok = catOk && (!q || it.dataset.search.includes(q));
          it.hidden = !ok;
          if (ok) visible++;
        });
        sec.hidden = visible === 0;
        shown += visible;
      });
      if (empty) empty.classList.toggle('show', shown === 0);
    };
    items.forEach(it => { it.dataset.search = it.textContent.replace(/\s+/g, ' ').toLowerCase(); });
    if (plFilters) plFilters.addEventListener('click', e => {
      const chip = e.target.closest('.chip');
      if (!chip) return;
      cat = chip.dataset.filter;
      $$('.chip', plFilters).forEach(c => { c.classList.toggle('on', c === chip); c.setAttribute('aria-pressed', c === chip); });
      apply();
      const anchor = $('#pricelist');
      if (anchor && anchor.getBoundingClientRect().top < 0) {
        window.scrollTo({ top: anchor.getBoundingClientRect().top + window.scrollY - (header ? header.offsetHeight : 0), behavior: reduceMotion ? 'auto' : 'smooth' });
      }
    });
    if (plSearch) plSearch.addEventListener('input', apply);
  }

  /* ── Pre-fill enquiry product from links (?product=) ─ */
  const productSelect = $('#fproduct');
  $$('[data-enquire]').forEach(a => a.addEventListener('click', () => {
    if (productSelect) productSelect.value = a.dataset.enquire;
  }));
  const qp = new URLSearchParams(location.search).get('product');
  if (qp && productSelect) productSelect.value = qp;

  /* ── Enquiry form → Google Sheets ─────────────────── */
  const SHEET_URL = 'https://script.google.com/macros/s/AKfycbwfnvO2rkMcCZu308u44b2YkR6YFYwG59AnvW_S1jmooQb9PrPFXtmbCE7lR04-yX1sCA/exec';
  const form = $('#inquiryForm');
  const successBox = $('#formSuccess');
  if (form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const setErr = (el, msg) => {
      const group = el.closest('.form-group');
      group.classList.toggle('error', !!msg);
      group.querySelector('.form-error-msg').textContent = msg || '';
    };

    form.addEventListener('submit', async e => {
      e.preventDefault();
      let valid = true;
      [
        { id: 'fname', label: 'Name', min: 2 },
        { id: 'fphone', label: 'Phone', min: 7 },
        { id: 'fmessage', label: 'Message', min: 10 }
      ].forEach(({ id, label, min }) => {
        const el = document.getElementById(id);
        if (el.value.trim().length < min) { setErr(el, `${label} must be at least ${min} characters.`); valid = false; }
        else setErr(el, '');
      });
      const email = $('#femail');
      if (email && email.value.trim()) {
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) { setErr(email, 'Please enter a valid email address.'); valid = false; }
        else setErr(email, '');
      }
      if (!valid) { const first = $('.form-group.error input, .form-group.error textarea', form); if (first) first.focus(); return; }

      const original = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending…';
      const fd = new FormData(form);
      const payload = {
        name: fd.get('name'), phone: fd.get('phone'), email: fd.get('email'),
        product: fd.get('product'), message: fd.get('message')
      };

      try {
        // Apps Script answers POST with a redirect; no-cors lets the data through
        // but the response is opaque, so success is shown optimistically.
        await fetch(SHEET_URL, {
          method: 'POST', mode: 'no-cors',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams(payload)
        });
        form.reset();
        form.style.display = 'none';
        successBox.style.display = 'flex';
        setTimeout(() => {
          successBox.style.display = 'none';
          form.style.display = 'block';
          submitBtn.disabled = false;
          submitBtn.innerHTML = original;
        }, 7000);
      } catch (err) {
        console.error('Form submission error:', err);
        alert('Submission failed. Please check your connection and try again, or call us directly.');
        submitBtn.disabled = false;
        submitBtn.innerHTML = original;
      }
    });

    $$('input, textarea', form).forEach(el => el.addEventListener('input', () => {
      const g = el.closest('.form-group');
      if (g && g.classList.contains('error')) setErr(el, '');
    }));
  }

  /* ── Footer year ──────────────────────────────────── */
  $$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
});
