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
  const navLinks = document.querySelectorAll('.nav-links a');

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

  /* ── 6. Contact form validation + Google Sheets submission ── */
  const SHEET_URL = "https://script.google.com/macros/s/AKfycbx-tGGsHu95bfoj8U9zwp307TfJZJuCrl9M-QxV-6lUUz3cnsUpdF5BD7RlUel7yrKKSQ/exec";

  const form = document.getElementById('inquiryForm');
  const successBox = document.getElementById('formSuccess');
  const submitBtn = form ? form.querySelector('button[type="submit"]') : null;

  if (form) {
    form.addEventListener('submit', async e => {
      e.preventDefault();
      let valid = true;

      const fields = [
        { id: 'fname', label: 'Name', min: 2 },
        { id: 'fphone', label: 'Phone', min: 7 },
        { id: 'fmessage', label: 'Message', min: 10 }
      ];

      fields.forEach(({ id, label, min }) => {
        const group = document.getElementById(id).closest('.form-group');
        const val = document.getElementById(id).value.trim();
        const err = group.querySelector('.form-error-msg');
        if (val.length < min) {
          group.classList.add('error');
          err.textContent = `${label} must be at least ${min} characters.`;
          valid = false;
        } else {
          group.classList.remove('error');
          if (err) err.textContent = '';
        }
      });

      // Email field optional but validate format if filled
      const emailEl = document.getElementById('femail');
      if (emailEl && emailEl.value.trim()) {
        const emailGroup = emailEl.closest('.form-group');
        const emailErr = emailGroup.querySelector('.form-error-msg');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailEl.value.trim())) {
          emailGroup.classList.add('error');
          emailErr.textContent = 'Please enter a valid email address.';
          valid = false;
        } else {
          emailGroup.classList.remove('error');
          if (emailErr) emailErr.textContent = '';
        }
      }

      if (!valid) return;

      // ── Loading state ──
      const originalLabel = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '⏳ Sending…';

      const formData = new FormData(form);
      const payload = {
        name: formData.get('name'),
        phone: formData.get('phone'),
        email: formData.get('email'),
        product: formData.get('product'),
        message: formData.get('message')
      };

      try {
        // Google Apps Script returns a 302 redirect on POST requests.
        // Using mode:'no-cors' + URLSearchParams lets the data reach the sheet,
        // but the response is opaque (unreadable) — so we show success optimistically.
        await fetch(SHEET_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams(payload)
        });

        // Data sent successfully — show success state
        form.reset();
        form.style.display = 'none';
        successBox.style.display = 'flex';

        // Auto-hide after 6 seconds and restore form
        setTimeout(() => {
          successBox.style.display = 'none';
          form.style.display = 'block';
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalLabel;
        }, 6000);

      } catch (error) {
        console.error('Form submission error:', error);
        alert('Submission failed. Please check your connection and try again.');
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalLabel;
      }
    });

    // Clear error styling on input
    form.querySelectorAll('input, textarea').forEach(input => {
      input.addEventListener('input', () => {
        const group = input.closest('.form-group');
        if (group) {
          group.classList.remove('error');
          const err = group.querySelector('.form-error-msg');
          if (err) err.textContent = '';
        }
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
