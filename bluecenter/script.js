(function () {
  var NUM = '5567999693397';
  var DEFAULT_MSG = 'Olá! Vim pelo site da Blue Car Auto Center e gostaria de um orçamento.';

  // WhatsApp links
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    var msg = a.getAttribute('data-msg') || DEFAULT_MSG;
    a.href = 'https://wa.me/' + NUM + '?text=' + encodeURIComponent(msg);
    a.target = '_blank';
    a.rel = 'noopener';
  });

  // header shadow
  var top = document.getElementById('top');
  function onScroll() { top.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // mobile menu
  var burger = document.getElementById('burger');
  var drawer = document.getElementById('drawer');
  function setMenu(open) {
    document.body.classList.toggle('menu-open', open);
    document.body.style.overflow = open ? 'hidden' : '';
    burger.setAttribute('aria-expanded', open);
    burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  }
  burger.addEventListener('click', function () { setMenu(!document.body.classList.contains('menu-open')); });
  drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });

  // reveal on scroll
  var pending = Array.prototype.slice.call(document.querySelectorAll('.rv'));
  function reveal() {
    var vh = window.innerHeight || document.documentElement.clientHeight;
    pending = pending.filter(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh - 40 && r.bottom > 0) { el.classList.add('in'); return false; }
      return true;
    });
    if (!pending.length) {
      window.removeEventListener('scroll', reveal);
      window.removeEventListener('resize', reveal);
    }
  }
  window.addEventListener('scroll', reveal, { passive: true });
  window.addEventListener('resize', reveal);
  reveal();
  window.addEventListener('load', reveal);

  // open now (America/Campo_Grande)
  var HOURS = { 0: null, 1: [450, 1080], 2: [450, 1080], 3: [450, 1080], 4: [450, 1080], 5: [450, 1080], 6: [450, 720] };
  function nowCG() {
    var p = {};
    new Intl.DateTimeFormat('en-US', { timeZone: 'America/Campo_Grande', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false })
      .formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
    var map = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return { d: map[p.weekday], m: (parseInt(p.hour, 10) % 24) * 60 + parseInt(p.minute, 10) };
  }
  try {
    var n = nowCG();
    var h = HOURS[n.d];
    var open = h && n.m >= h[0] && n.m < h[1];
    var pill = document.getElementById('openPill');
    var txt = document.getElementById('openTxt');
    if (open) { pill.classList.add('open'); txt.textContent = 'Aberto agora · até ' + (h[1] === 720 ? '12h' : '18h'); }
    else { txt.textContent = 'Fechado agora · Campo Grande/MS'; }
    var row = document.querySelector('#hours tr[data-d="' + n.d + '"]');
    if (row) row.classList.add('today');
  } catch (e) {}

  // barra de progresso
  var prog = document.getElementById('progress');
  function progress() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    prog.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
  }
  progress();
  window.addEventListener('scroll', progress, { passive: true });

  // leitura do scanner (ilustrativa)
  var rd = {
    rpm: { el: document.querySelector('[data-rd=rpm]'), base: 842, amp: 28, dec: 0, max: 4000 },
    temp: { el: document.querySelector('[data-rd=temp]'), base: 92, amp: 2, dec: 0, max: 130 },
    bat: { el: document.querySelector('[data-rd=bat]'), base: 13.8, amp: .25, dec: 1, max: 16 },
    map: { el: document.querySelector('[data-rd=map]'), base: 32, amp: 3, dec: 0, max: 100 }
  };
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    setInterval(function () {
      Object.keys(rd).forEach(function (k) {
        var o = rd[k]; if (!o.el) return;
        var v = o.base + (Math.random() * 2 - 1) * o.amp;
        o.el.textContent = v.toFixed(o.dec);
        var bar = o.el.closest('.rd').querySelector('i');
        if (bar) bar.style.setProperty('--v', Math.min(1, v / o.max).toFixed(3));
      });
    }, 900);
  }

  document.getElementById('yr').textContent = new Date().getFullYear();
})();
