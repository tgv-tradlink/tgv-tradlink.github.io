/* ============================================================
   TGV TRADLINK — script.js
   Features:
   - Sticky header with scroll class
   - Mobile hamburger menu
   - Smooth scroll
   - Active nav link on scroll (Intersection Observer)
   - Scroll-reveal animations
   - Contact form validation
============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. Sticky header ─────────────────────────────────── */
  const header = document.getElementById('header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  });

  /* ── 2. Hamburger / mobile nav ────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');

  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileNav.classList.toggle('open');
  });

  // Close on link click
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      hamburger.classList.remove('open');
      mobileNav.classList.remove('open');
    });
  });

  /* ── 3. Active nav link on scroll ────────────────────── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks  = document.querySelectorAll('.nav-links a');

  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          link.classList.toggle(
            'active',
            link.getAttribute('href') === '#' + entry.target.id
          );
        });
      }
    });
  }, { threshold: 0.35 });

  sections.forEach(sec => sectionObserver.observe(sec));

  /* ── 4. Scroll-reveal ─────────────────────────────────── */
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  /* ── 5. Animated stat counters (hero) ─────────────────── */
  function animateCounter(el, target, suffix = '') {
    let current = 0;
    const step = Math.ceil(target / 60);
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = current + suffix;
      if (current >= target) clearInterval(timer);
    }, 24);
  }

  const heroSection = document.getElementById('hero');
  let countersStarted = false;
  const heroObserver = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting && !countersStarted) {
      countersStarted = true;
      document.querySelectorAll('.hero-stat[data-count]').forEach(stat => {
        const target = parseInt(stat.dataset.count);
        const suffix = stat.dataset.suffix || '';
        animateCounter(stat.querySelector('strong'), target, suffix);
      });
    }
  }, { threshold: 0.4 });
  heroObserver.observe(heroSection);

  /* ── 6. Contact form validation ───────────────────────── */
  const form = document.getElementById('inquiryForm');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      let valid = true;

      const fields = [
        { id: 'fname',   label: 'Name',    min: 2 },
        { id: 'fphone',  label: 'Phone',   min: 7 },
        { id: 'fmessage',label: 'Message', min: 10 }
      ];

      fields.forEach(({ id, label, min }) => {
        const group = document.getElementById(id).closest('.form-group');
        const val   = document.getElementById(id).value.trim();
        const err   = group.querySelector('.form-error-msg');
        if (val.length < min) {
          group.classList.add('error');
          err.textContent = `${label} must be at least ${min} characters.`;
          valid = false;
        } else {
          group.classList.remove('error');
        }
      });

      // Email field optional but validate format if filled
      const emailEl = document.getElementById('femail');
      if (emailEl && emailEl.value.trim()) {
        const emailGroup = emailEl.closest('.form-group');
        const emailErr   = emailGroup.querySelector('.form-error-msg');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailEl.value.trim())) {
          emailGroup.classList.add('error');
          emailErr.textContent = 'Please enter a valid email address.';
          valid = false;
        } else {
          emailGroup.classList.remove('error');
        }
      }

      if (valid) {
        form.style.display = 'none';
        document.getElementById('formSuccess').style.display = 'block';
      }
    });

    // Clear error on input
    form.querySelectorAll('input, textarea').forEach(input => {
      input.addEventListener('input', () => {
        input.closest('.form-group').classList.remove('error');
      });
    });
  }

  /* ── 7. Smooth scroll for all anchor links ─────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = header.offsetHeight + 8;
        window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
      }
    });
  });

});
