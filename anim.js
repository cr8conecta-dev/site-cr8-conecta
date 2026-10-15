/* Animações leves — só transform/opacity + IntersectionObserver.
   Sem brilho. Feito pra não travar/engasgar. */
(function () {
  'use strict';

  /* ---------- 1) Reveal ao rolar (fade-up sutil) ---------- */
  var revealSelectors = [
    '#social-proof .section-header', '.proof-closing',
    '.posicionamento-col-left', '.diferencial-item',
    '.par360 .p360-heading', '.par360 .intro', '.par360 .card',
    '.method-par-header', '.method-par-pillar',
    '.viability-header-tag', '.viability-title-container', '.viability-card',
    '.crew-head',
    '#testimonials .section-header',
    '.faq-container'
  ];

  var els = [];
  revealSelectors.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (e) {
      if (!e.classList.contains('blur-in') && !e.classList.contains('reveal')) els.push(e);
    });
  });

  if (!('IntersectionObserver' in window)) {
    els.forEach(function (e) { e.classList.add('reveal', 'is-in'); });
  } else {
    els.forEach(function (e) {
      e.classList.add('reveal');
      var parent = e.parentNode;
      var idx = parent ? Array.prototype.indexOf.call(parent.children, e) : 0;
      e.style.transitionDelay = (Math.min(idx, 5) * 0.09) + 's';
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- 2) Count-up nos números de resultado ---------- */
  function countUp(el) {
    var raw = el.getAttribute('data-final') || el.textContent;
    el.setAttribute('data-final', raw);
    var num = parseInt(raw.replace(/[^\d]/g, ''), 10);
    if (!num || num < 10) return; // números muito pequenos não valem a pena
    var prefix = /R\$/.test(raw) ? 'R$' : '';
    var dur = 1300, start = null;
    var done = false;
    function finish() { if (!done) { done = true; el.textContent = raw; } } // valor final garantido
    function frame(t) {
      if (done) return;
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + Math.round(num * eased).toLocaleString('pt-BR');
      if (p < 1) requestAnimationFrame(frame);
      else finish(); // restaura o formato exato original
    }
    requestAnimationFrame(frame);
    setTimeout(finish, dur + 600); // fallback: se o rAF travar, mostra o valor final mesmo assim
  }

  var nums = document.querySelectorAll('.proof-card-value, .proof-card-fechados');
  if ('IntersectionObserver' in window && nums.length) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { countUp(en.target); io2.unobserve(en.target); }
      });
    }, { threshold: 0.4 });
    nums.forEach(function (e) { io2.observe(e); });
  }

  /* ---------- 3) Giro dos ícones "Não somos uma agência" (um por um, ao entrar) ---------- */
  var pos = document.querySelector('.posicionamento-section');
  if (pos && 'IntersectionObserver' in window) {
    var items = pos.querySelectorAll('.diferencial-item');
    var ioPos = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          items.forEach(function (it, i) {
            setTimeout(function () { it.classList.add('spin-in'); }, 200 + i * 380);
          });
          ioPos.disconnect();
        }
      });
    }, { threshold: 0.3 });
    ioPos.observe(pos);
  }
})();
