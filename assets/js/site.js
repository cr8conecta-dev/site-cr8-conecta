/* CR8 Conecta · comportamentos do site (sem dependências) */
(function () {
  "use strict";
  var dl = (window.dataLayer = window.dataLayer || []);

  function track(name, data) {
    var payload = { event: name };
    for (var k in data) { if (Object.prototype.hasOwnProperty.call(data, k)) payload[k] = data[k]; }
    dl.push(payload);
  }

  // Aviso de cookies: o Google Tag Manager só carrega depois do "Aceitar"
  (function () {
    var bar = document.getElementById("cookie-bar");
    if (!bar) return;
    var KEY = "cr8-cookies";
    function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
    function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
    function show() { bar.hidden = false; }
    if (!get()) show();
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("[data-cookie]");
      if (!b) return;
      var v = b.getAttribute("data-cookie");
      set(v);
      bar.hidden = true;
      if (v === "aceito" && window.cr8LoadGTM) window.cr8LoadGTM();
    });
    document.addEventListener("click", function (e) {
      if (e.target.closest("[data-cookie-open]")) show();
    });
  })();

  // Menu mobile
  var header = document.querySelector(".site-header");
  var navButton = document.querySelector(".nav-button");
  if (header && navButton) {
    navButton.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      navButton.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Menu "Soluções" no desktop
  var menus = document.querySelectorAll(".has-menu");
  function closeMenus(except) {
    menus.forEach(function (m) {
      if (m !== except) {
        m.classList.remove("is-open");
        var b = m.querySelector(".menu-toggle");
        if (b) b.setAttribute("aria-expanded", "false");
      }
    });
  }
  menus.forEach(function (m) {
    var btn = m.querySelector(".menu-toggle");
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = m.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      closeMenus(m);
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-menu")) closeMenus(null);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenus(null);
  });

  // Depoimentos em vídeo: o player do YouTube só carrega no clique
  document.querySelectorAll(".video[data-yt]").forEach(function (el) {
    el.addEventListener("click", function () {
      var id = el.getAttribute("data-yt");
      var name = el.getAttribute("data-name") || "Depoimento";
      var iframe = document.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0";
      iframe.title = "Depoimento de " + name;
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      el.innerHTML = "";
      el.appendChild(iframe);
      track("video_play", { video_name: name });
    });
  });

  // Rastreamento de cliques nos botões de contato (Google Tag Manager)
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-cta]");
    if (!a) return;
    track("cta_click", {
      cta_type: a.getAttribute("data-cta"),
      cta_text: (a.textContent || "").trim().slice(0, 80),
      cta_url: a.getAttribute("href")
    });
  });

  // Formulário de contato: monta a mensagem e abre o WhatsApp
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var lines = ["Olá, vim do site e gostaria do diagnóstico gratuito."];
      [["nome", "Nome"], ["empresa", "Empresa"], ["segmento", "Segmento"], ["cidade", "Cidade e região"], ["interesse", "Quero melhorar"]].forEach(function (p) {
        var v = (f.get(p[0]) || "").toString().trim();
        if (v) lines.push(p[1] + ": " + v);
      });
      var number = form.getAttribute("data-whatsapp");
      var url = "https://wa.me/" + number + "?text=" + encodeURIComponent(lines.join("\n"));
      track("generate_lead", { form_id: "contact-form" });
      window.open(url, "_blank", "noopener");
    });
  }

  // ---- Movimento e vida (respeita "reduzir movimento") ----
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Sombra do cabeçalho ao rolar + barra de progresso + parallax leve (um único rAF)
  var bar = null;
  if (!reduce) {
    bar = document.createElement("div");
    bar.className = "progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);
  }
  var ticking = false;
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    if (header) header.classList.toggle("scrolled", y > 8);
    if (!reduce) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if (bar) bar.style.transform = "scaleX(" + (max > 0 ? Math.min(1, y / max) : 0) + ")";
      var hero = document.querySelector(".hero-grid, .page-hero-grid");
      if (hero && y < 1400) hero.style.setProperty("--py", String(Math.round(y)));
    }
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  // Luz que acompanha o mouse nos cartões (só com mouse de verdade)
  if (!reduce && window.matchMedia && window.matchMedia("(hover: hover)").matches) {
    document.addEventListener("pointermove", function (e) {
      var card = e.target.closest && e.target.closest(".pillar, .index a, .deliver > div, .faq details");
      if (!card) return;
      var r = card.getBoundingClientRect();
      card.style.setProperty("--mx", (e.clientX - r.left) + "px");
      card.style.setProperty("--my", (e.clientY - r.top) + "px");
    }, { passive: true });
  }

  // Contador nos números de resultado (o texto final continua no HTML)
  function countUp(el) {
    var node = el.firstChild;
    if (!node || node.nodeType !== 3) return;
    var text = node.nodeValue;
    var m = text.match(/(\d[\d.]*)/);
    if (!m) return;
    var target = parseInt(m[1].replace(/\./g, ""), 10);
    if (!target || target < 20) return;
    var pre = text.slice(0, m.index), post = text.slice(m.index + m[1].length);
    var start = null, dur = 1400;
    function step(t) {
      if (start === null) start = t;
      var p = Math.min(1, (t - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      node.nodeValue = pre + Math.round(target * eased).toLocaleString("pt-BR") + post;
      if (p < 1) window.requestAnimationFrame(step); else node.nodeValue = text;
    }
    node.nodeValue = pre + "0" + post;
    window.requestAnimationFrame(step);
  }


  // Ilustração da busca (home): toca quando aparece na tela e volta a tocar de tempos em tempos
  var serp = document.querySelector(".serp");
  if (serp && !reduce && "IntersectionObserver" in window) {
    serp.classList.add("pre");
    var serpTimer = null;
    var replay = function () {
      serp.classList.add("rs");
      void serp.offsetWidth;
      serp.classList.remove("rs");
    };
    new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          if (serp.classList.contains("pre")) { serp.classList.remove("pre"); } else { replay(); }
          if (serpTimer) clearInterval(serpTimer);
          serpTimer = setInterval(replay, 9000);
        } else if (serpTimer) {
          clearInterval(serpTimer); serpTimer = null;
        }
      });
    }, { threshold: 0.35 }).observe(serp);
  }

  // Revelar ao rolar, com escalonamento entre irmãos
  if (!reduce && "IntersectionObserver" in window) {
    var groups = [
      ".ledger-head", ".pillars > *", ".index li", ".deliver > div", ".faq details", ".steps li",
      ".videos > .video", ".cases tbody tr", ".cta-box", ".facts", ".contact-list", ".map", ".two-col > *",
      ".team > *", ".stack-fig > .fig", ".checks li", ".prose", ".note", ".ledger > div:not(.ledger-head) > .fig", ".form",
      ".caps li", ".autos li", ".steps"
    ];
    var seen = [];
    groups.forEach(function (sel) {
      document.querySelectorAll("main " + sel).forEach(function (el) {
        if (seen.indexOf(el) !== -1 || el.closest(".hero, .page-hero")) return;
        seen.push(el);
        var sibs = el.parentNode ? Array.prototype.filter.call(el.parentNode.children, function (c) { return c.tagName === el.tagName; }) : [el];
        var idx = Math.max(0, sibs.indexOf(el));
        el.style.setProperty("--d", (Math.min(idx, 6) * 0.09).toFixed(2) + "s");
        el.classList.add("reveal");
      });
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        el.classList.add("in");
        io.unobserve(el);
        el.querySelectorAll(".n").forEach(countUp);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    seen.forEach(function (el) { io.observe(el); });

    // A luz de fundo de cada seção só se move enquanto a seção está na tela (poupa o celular)
    var live = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.target.classList.toggle("is-live", en.isIntersecting); });
    }, { threshold: 0.05 });
    document.querySelectorAll("main > .section").forEach(function (s) { live.observe(s); });
  }

})();
