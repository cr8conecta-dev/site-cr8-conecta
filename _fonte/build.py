# -*- coding: utf-8 -*-
"""Gera o site estático da CR8 Conecta.

Uso: python3 build.py SAIDA [--preview]
--preview gera links com index.html e sem GTM (para visualizar fora do servidor final).
"""
import art
import html
import json
import os
import re
import sys
from urllib.parse import quote

import struct

sys.path.insert(0, os.path.dirname(__file__))
from data import *  # noqa

OUT = sys.argv[1]
PREVIEW = "--preview" in sys.argv

with open(os.path.join(OUT, "assets/logos/cr8-conecta-logo.png"), "rb") as _f:
    logo_w, logo_h = struct.unpack(">II", _f.read(24)[16:24])
MARK_W, MARK_H = 51, 42

WA_URL = "https://wa.me/%s?text=%s" % (WHATSAPP, quote(WA_TEXT))


def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def plain(s):
    return re.sub(r"<[^>]+>", "", s)



def _versao(p):
    """?v=<hash> em css/js: cada mudança do arquivo força navegador e CDN a baixar de novo."""
    import hashlib, os
    if not p.endswith((".css", ".js")):
        return ""
    f = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", p)
    try:
        return "?v=" + hashlib.md5(open(f, "rb").read().replace(b"\r\n", b"\n")).hexdigest()[:8]
    except OSError:
        return ""

class Ctx:
    def __init__(self, slug):
        self.slug = slug
        self.depth = 0 if slug == "" else 1

    @property
    def root(self):
        return "./" if self.depth == 0 else "../"

    def asset(self, p):
        return self.root + "assets/" + p + _versao(p)

    def link(self, slug):
        if slug == "":
            return self.root + ("index.html" if PREVIEW else "")
        return self.root + slug + "/" + ("index.html" if PREVIEW else "")

    def url(self):
        return SITE + "/" + (self.slug + "/" if self.slug else "")


# ---------------------------------------------------------------- componentes
def pillar_cls(key):
    return PILLARS[key]["cls"]


def header(c, current=None):
    items = "".join(
        '<a href="%s"><strong>%s</strong><span>Pilar %s</span></a>'
        % (c.link(s["slug"]), esc(s["nav"]), PILLARS[s["pillar"]]["name"])
        for s in SOLUTIONS
    )

    def cur(slug):
        return ' aria-current="page"' if current == slug else ""

    chevron = '<svg viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
    return f"""<header class="site-header">
<div class="wrap header-inner">
<a class="brand" href="{c.link('')}" aria-label="CR8 Conecta, página inicial"><img src="{c.asset('logos/cr8-mark.png')}" alt="" width="{MARK_W}" height="{MARK_H}"><span>CR8 Conecta</span></a>
<button class="nav-button" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="nav" id="site-nav" aria-label="Principal">
<div class="has-menu"><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu-solucoes">Soluções {chevron}</button>
<div class="menu" id="menu-solucoes">{items}</div></div>
<a href="{c.link(PAR['slug'])}"{cur(PAR['slug'])}>Método PAR 360</a>
<a href="{c.link('sobre')}"{cur('sobre')}>Sobre</a>
<a href="{c.link('contato')}"{cur('contato')}>Contato</a>
<a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Diagnóstico gratuito</a>
</nav>
</div>
</header>"""


def footer(c):
    sol = "".join('<li><a href="%s">%s</a></li>' % (c.link(s["slug"]), esc(s["nav"])) for s in SOLUTIONS)
    return f"""<footer class="site-footer">
<div class="wrap">
<div class="footer-grid">
<div>
<a class="brand" href="{c.link('')}" aria-label="CR8 Conecta, página inicial"><img src="{c.asset('logos/cr8-mark.png')}" alt="" width="{MARK_W}" height="{MARK_H}"><span>CR8 Conecta</span></a>
<p class="about">Agência de marketing e vendas de Curitiba. Posicionamento, atração e retenção para empresas de serviços venderem de forma previsível.</p>
</div>
<div><h2>Soluções</h2><ul>{sol}</ul></div>
<div><h2>Empresa</h2><ul>
<li><a href="{c.link(PAR['slug'])}">Método PAR 360</a></li>
<li><a href="{c.link('sobre')}">Sobre a CR8 Conecta</a></li>
<li><a href="{c.link('contato')}">Contato</a></li>
</ul></div>
<div><h2>Fale com a gente</h2><ul>
<li><a href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">WhatsApp {PHONE}</a></li>
<li><a href="mailto:{EMAIL}" data-cta="email">{EMAIL}</a></li>
<li><a href="{INSTAGRAM}" rel="noopener" target="_blank">Instagram @cr8conecta</a></li>
<li>Curitiba, PR. Atendimento em Curitiba e região metropolitana, e também em outros estados.</li>
</ul></div>
</div>
<div class="footer-bottom"><span>© 2026 CR8 Conecta. Todos os direitos reservados.</span><span><a href="{c.link('politica-de-privacidade')}">Política de privacidade</a></span><span>Atualizado em {MODIFIED_HUMAN}</span></div>
</div>
</footer>
<a class="wa-float" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener" aria-label="Falar com a CR8 Conecta pelo WhatsApp"><svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16.04 3C9.4 3 4 8.33 4 14.9c0 2.1.56 4.15 1.62 5.95L4 27l6.3-1.6a12.1 12.1 0 0 0 5.74 1.46C22.68 26.86 28 21.5 28 14.9 28 8.33 22.68 3 16.04 3zm0 21.8c-1.8 0-3.55-.48-5.08-1.38l-.36-.21-3.74.95 1-3.6-.24-.37a9.7 9.7 0 0 1-1.5-5.2c0-5.4 4.4-9.8 9.92-9.8 5.4 0 9.8 4.4 9.8 9.8s-4.5 9.81-9.8 9.81zm5.4-7.3c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.47-.89-.78-1.48-1.75-1.66-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.57-.48-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5s1.07 2.9 1.22 3.1c.15.2 2.1 3.2 5.1 4.5.7.3 1.27.5 1.7.62.72.23 1.37.2 1.88.12.57-.08 1.75-.72 2-1.4.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35z"/></svg></a>"""


def crumbs(c, trail):
    lis = []
    for label, slug in trail:
        if slug is None:
            lis.append('<li aria-current="page">%s</li>' % esc(label))
        else:
            lis.append('<li><a href="%s">%s</a></li>' % (c.link(slug), esc(label)))
    return '<nav class="crumbs" aria-label="Você está em"><ol>%s</ol></nav>' % "".join(lis)


def checks(items, no=False):
    return '<ul class="checks%s">%s</ul>' % (" no" if no else "", "".join("<li>%s</li>" % esc(i) for i in items))


def deliver(items):
    return '<dl class="deliver">%s</dl>' % "".join(
        "<div><dt>%s</dt><dd>%s</dd></div>" % (esc(t), esc(d)) for t, d in items
    )


def steps(items):
    return '<ol class="steps">%s</ol>' % "".join(
        "<li><div><h3>%s</h3><p>%s</p></div></li>" % (esc(t), esc(d)) for t, d in items
    )


def faq(items):
    return '<div class="faq">%s</div>' % "".join(
        '<details><summary>%s</summary><div class="answer"><p>%s</p></div></details>' % (esc(q), esc(a))
        for q, a in items
    )


def index_list(c, slugs):
    rows = []
    for slug in slugs:
        if slug == PAR["slug"]:
            rows.append(
                '<li><a href="%s"><span class="name">Método PAR 360</span><span class="desc">O sistema completo: posicionamento, atração e retenção trabalhando juntos.</span><span class="tag t-p">Visão geral</span></a></li>'
                % c.link(slug)
            )
            continue
        s = SOL[slug]
        p = PILLARS[s["pillar"]]
        rows.append(
            '<li><a href="%s"><span class="name">%s</span><span class="desc">%s</span><span class="tag %s">%s</span></a></li>'
            % (c.link(slug), esc(s["nav"]), esc(s["index_desc"]), p["cls"], p["name"])
        )
    return '<ul class="index">%s</ul>' % "".join(rows)


def cases_table():
    rows = "".join(
        '<tr><td data-label="Segmento">%s</td><td data-label="Investimento em anúncios"><span class="n">%s</span></td>'
        '<td data-label="Resultado"><span class="n">%s<small>%s</small></span></td></tr>' % (esc(seg), inv, res, esc(sub))
        for seg, inv, res, sub in CASES
    )
    return (
        '<table class="cases"><caption>Três resultados de clientes da CR8 Conecta</caption>'
        '<thead><tr><th scope="col">Segmento</th><th scope="col">Investimento em anúncios</th><th scope="col">Resultado</th></tr></thead>'
        "<tbody>%s</tbody></table><p class=\"fine-print\">%s</p>" % (rows, esc(CASES_NOTE))
    )


def cta_band(c, title, text):
    return f"""<section class="cta-band" aria-labelledby="cta-title"><div class="wrap">
<div class="cta-box">
<div><h2 id="cta-title">{esc(title)}</h2><p>{esc(text)}</p></div>
<div class="btn-row"><a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Pedir diagnóstico gratuito</a><a class="btn btn-ghost" href="{c.link('contato')}">Outras formas de contato</a></div>
</div>
</div></section>"""


def ledger(title, body, sub=None, section_id=None, label_id=None):
    sub_html = "<p>%s</p>" % esc(sub) if sub else ""
    idattr = ' id="%s"' % section_id if section_id else ""
    return (
        f'<section class="section"{idattr}><div class="wrap ledger"><div class="ledger-head"><h2>{esc(title)}</h2>{sub_html}</div>'
        f"<div>{body}</div></div></section>"
    )


# ---------------------------------------------------------------- SEO / schema
ALT_NAMES_HOME = ["Cr8 Conecta", "Agência de Marketing Digital | Cr8 Conecta"]
SAMEAS_HOME = ["https://www.facebook.com/cr8conecta/", "https://www.google.com/maps?cid=13746290579143037967", "https://br.linkedin.com/company/cr8-conecta"]


def org_node(home=False):
    return {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": SITE + "/#organization",
        "name": NAME,
        **({"alternateName": ALT_NAMES_HOME} if home else {}),
        "url": SITE + "/",
        "hasMap": "https://www.google.com/maps?cid=13746290579143037967",
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/logos/cr8-conecta-logo.png", "width": logo_w, "height": logo_h},
        "image": SITE + OG_IMAGE,
        "description": "Agência de marketing e vendas de Curitiba que usa o Método PAR 360 (Posicionamento, Atração e Retenção) para empresas de serviços e comércio especializado venderem de forma previsível.",
        "slogan": "Quem aparece mais vende mais.",
        "telephone": PHONE_E164,
        "email": EMAIL,
        "foundingDate": "2021",
        "founder": {"@type": "Person", "name": "Carlos da Silva", "jobTitle": "CEO e sócio-fundador"},
        "address": {"@type": "PostalAddress", "addressLocality": "Curitiba", "addressRegion": "PR", "addressCountry": "BR"},
        "areaServed": [
            {"@type": "City", "name": "Curitiba"},
            {"@type": "AdministrativeArea", "name": "Região Metropolitana de Curitiba"},
            {"@type": "Country", "name": "Brasil"},
        ],
        "knowsAbout": [
            "Marketing digital", "Tráfego pago", "Google Ads", "Meta Ads", "Perfil da Empresa no Google", "Google Meu Negócio",
            "SEO local", "CRM", "Follow-up comercial", "Automação de atendimento", "Inteligência artificial no atendimento",
        ],
        "sameAs": [INSTAGRAM] + (SAMEAS_HOME if home else []),
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_E164, "email": EMAIL, "contactType": "customer service", "availableLanguage": "pt-BR", "areaServed": "BR"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Soluções da CR8 Conecta",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["service_type"], "url": "%s/%s/" % (SITE, s["slug"])}}
                for s in SOLUTIONS
            ],
        },
    }


def website_node():
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": NAME, "inLanguage": "pt-BR", "publisher": {"@id": SITE + "/#organization"}}


def breadcrumb_node(url, trail):
    items = []
    for i, (label, loc) in enumerate(trail, 1):
        items.append({"@type": "ListItem", "position": i, "name": label, "item": loc})
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items}


def faq_node(url, items):
    return {
        "@type": "FAQPage", "@id": url + "#faq", "inLanguage": "pt-BR",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }


def webpage_node(url, title, desc, page_type="WebPage", extra=None):
    n = {
        "@type": page_type, "@id": url + "#webpage", "url": url, "name": title, "description": desc,
        "inLanguage": "pt-BR", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#organization"},
        "dateModified": MODIFIED, "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + OG_IMAGE},
    }
    if extra:
        n.update(extra)
    return n


def head(c, title, desc, graph, noindex=False):
    url = c.url()
    gtm_head = ""
    gtm_body = ""
    if not PREVIEW:
        gtm_head = (
            "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
            "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;"
            "j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})"
            "(window,document,'script','dataLayer','%s');</script>" % GTM_ID
        )
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    canonical = "" if noindex else '<link rel="canonical" href="%s">\n' % url
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{attr(desc)}">
<meta name="robots" content="{robots}">
{canonical}<meta name="theme-color" content="#0A101A">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{attr(title)}">
<meta property="og:description" content="{attr(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{attr(title)}">
<meta name="twitter:description" content="{attr(desc)}">
<meta name="twitter:image" content="{SITE}{OG_IMAGE}">
<link rel="icon" href="{c.root}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" href="{c.asset('img/favicon-32.png')}" sizes="32x32">
<link rel="apple-touch-icon" href="{c.root}apple-touch-icon.png">
<link rel="preload" href="{c.asset('fonts/archivo-latin.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{c.asset('css/style.css')}">
<script type="application/ld+json">{ld}</script>
{gtm_head}
</head>
<body>
{('<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>' % GTM_ID) if not PREVIEW else ''}
<a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
"""


def tail(c):
    return f"""
<script src="{c.asset('js/site.js')}" defer></script>
</body>
</html>
"""


def destaque(html_text):
    """Títulos (h1/h2) com a parte final em gradiente azul: depois dos dois pontos, depois da última vírgula ou nas últimas palavras."""
    import re
    corpo, sep, resto = html_text.partition("<footer")

    def corta(m):
        abre, txt, fecha = m.group(1), m.group(2), m.group(3)
        if "<" in txt or "&" in txt and ";" not in txt:
            return m.group(0)
        for marca in (": ", ", "):
            i = txt.rfind(marca)
            if 0 < i < len(txt) - 3:
                return '%s%s%s<span class="grad">%s</span>%s' % (abre, txt[:i + len(marca)], "", txt[i + len(marca):], fecha)
        palavras = txt.split(" ")
        n = len(palavras)
        if n < 2:
            return m.group(0)
        k = max(1, round(n / 2.5))
        return '%s%s <span class="grad">%s</span>%s' % (abre, " ".join(palavras[:-k]), " ".join(palavras[-k:]), fecha)

    corpo = re.sub(r"(<h[12](?: [^>]*)?>)([^<]+)(</h[12]>)", corta, corpo)
    return corpo + sep + resto


def write_page(slug, html_text):
    html_text = destaque(html_text)
    folder = OUT if slug == "" else os.path.join(OUT, slug)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_text)


# ---------------------------------------------------------------- páginas
def serp_html():
    search = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M11 11l3.5 3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
    rows = (
        '<div class="serp-row is-us" style="--i:0"><span class="ico"></span><span class="t">Sua empresa</span><span class="serp-badge">1º</span><span class="bar"></span></div>'
        '<div class="serp-row" style="--i:1"><span class="ico"></span><span class="t">Concorrente A</span><span class="bar"></span></div>'
        '<div class="serp-row" style="--i:2"><span class="ico"></span><span class="t">Concorrente B</span><span class="bar"></span></div>'
        '<div class="serp-row" style="--i:3"><span class="ico"></span><span class="t">Concorrente C</span><span class="bar"></span></div>'
    )
    return f"""<div class="serp" role="img" aria-label="Ilustração: a sua empresa sobe para o primeiro resultado da busca no Google, recebe uma mensagem de um cliente no WhatsApp e responde na hora.">
<div class="serp-q">{search}<span>seu serviço em Curitiba</span></div>
<div class="serp-list">{rows}</div>
<div class="chat"><p class="bubble them">Olá, encontrei vocês no Google! Gostaria de fazer um orçamento!</p><p class="bubble us">Olá, seja bem-vindo(a) à CR8 Conecta!</p></div>
<p class="serp-note">Ilustração: ser encontrado primeiro e responder primeiro.</p>
</div>"""


def marquee_html():
    items = "".join(f"<li>{esc(x)}</li>" for x in SEGMENTOS)
    return ('<div class="marquee" role="group" aria-label="Segmentos que já atendemos"><div class="marquee-track">'
            f'<ul>{items}</ul><ul aria-hidden="true">{items}</ul></div></div>')


def trends_html():
    items = [
        ("Ser encontrado pela inteligência artificial", "Posicionamento",
         'Cada vez mais gente pergunta a ferramentas de IA qual empresa contratar. Nos EUA, 45% dos consumidores já usam IA para pedir recomendação de empresa local, contra 6% um ano antes (BrightLocal, 2026). A IA recomenda o que entende sem ambiguidade: informação clara, perfil completo no Google, avaliações reais, perguntas e respostas e dados iguais em todo lugar. Veja <a href="{g}">Perfil da Empresa no Google</a> e <a href="{s}">Criação de Sites</a>.'),
        ("Atendimento sem fricção", "Retenção",
         'Quem responde rápido e sem etapas inúteis fecha. O guia recomenda testar a jornada como se fosse o cliente. No diagnóstico gratuito, olhamos como sua empresa responde, quanto tempo leva e o que acontece depois do orçamento. Veja <a href="{a}">Automação e IA no Atendimento</a>.'),
        ("Processo antes da inteligência artificial", "Retenção",
         'A Gartner, citada no guia, prevê que mais de 40% dos projetos de IA agêntica devem ser cancelados até 2027, entre outros motivos por falta de processo reestruturado. Arrumar a casa vem primeiro: funil, CRM e follow-up. Veja <a href="{c}">CRM de Vendas</a>.'),
        ("A IA organiza, a pessoa fecha", "Retenção",
         'A inteligência artificial responde na hora, qualifica e registra tudo, e a conversa passa para uma pessoa da equipe quando o cliente está pronto. É rapidez sem perder a humanização.'),
    ]
    links = dict(g="google-meu-negocio", s="criacao-de-sites", a="automacao-ia-atendimento", c="crm-de-vendas")
    return links, items


def trends_section(c):
    links, items = trends_html()
    rows = "".join(
        f'<div><dt>{esc(t)} <span class="fine-tag">{esc(p)}</span></dt><dd>{txt.format(**{k: c.link(v) for k, v in links.items()})}</dd></div>'
        for t, p, txt in items
    )
    src = ('<p class="hint" style="margin-top:1.2rem">Fontes: Guia de Tendências 2026 do Sebrae/PR; Gartner, citada no guia; '
           'BrightLocal, Local Consumer Review Survey 2026 (consumidores dos EUA). Os dados são de pequenos negócios em geral, '
           'e a relação de cada tendência com o método é leitura da CR8 Conecta.</p>')
    return ledger("O que está mudando em 2026", f'<dl class="deliver">{rows}</dl>{src}',
                  "Tendências do momento que já fazem parte do Método PAR 360.", section_id="tendencias")


def faces_html(c):
    from data import TEAM
    li = "".join('<li><img src="%sassets/team/%s" alt="%s, %s" width="120" height="120" loading="lazy"><span>%s</span></li>' % (c.root, f, attr(n), attr(r), esc(n.split()[0])) for n, r, f, _ in TEAM)
    return '<ul class="faces">%s</ul>' % li

def build_home():
    c = Ctx("")
    title = "CR8 Conecta | Agência de marketing e vendas em Curitiba"
    desc = "Agência de marketing e vendas em Curitiba. Posicionamento, tráfego pago e CRM para empresas de serviços venderem todo mês, sem depender só de indicação."
    url = c.url()
    graph = [org_node(home=True), website_node(), webpage_node(url, title, desc, extra={"about": {"@id": SITE + "/#organization"}}), faq_node(url, HOME_FAQ)]

    pillars_html = ""
    for p in PAR["pillars"]:
        links = "".join('<a href="%s">%s</a>' % (c.link(s), esc(SOL[s]["nav"])) for s in p["links"])
        pillars_html += (
            f'<div class="pillar {p["cls"]}"><h3>{p["name"]}<small>{esc(p["tagline"])}</small></h3>'
            f'<div><p>{esc(p["text"])}</p><div class="links">{links}</div></div></div>'
        )

    videos = "".join(
        '<button class="video" type="button" data-yt="%s" data-name="%s" aria-label="Assistir ao depoimento de %s">'
        '<img src="https://i.ytimg.com/vi/%s/hqdefault.jpg" alt="" loading="lazy" width="480" height="360" onerror="this.remove()">'
        '<span class="play" aria-hidden="true"><svg viewBox="0 0 16 16"><path d="M3 1.5v13l11-6.5z"/></svg></span>'
        '<span class="who">%s<small>Depoimento em vídeo</small></span></button>' % (vid, attr(n), attr(n), vid, esc(n))
        for vid, n in VIDEOS
    )

    low = lambda x: x[0].lower() + x[1:]
    seg_text = ", ".join(low(x) for x in SEGMENTOS[:-1]) + " e " + low(SEGMENTOS[-1])

    body = f"""<main id="conteudo">
<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Agência de marketing e vendas em Curitiba: <span class="grad">quem aparece mais, vende mais</span></h1>
<p class="lead">Agência de marketing e vendas de Curitiba. Colocamos sua empresa na frente de quem já procura o que você faz e organizamos o comercial para fechar mais.</p>
<div class="btn-row"><a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Pedir diagnóstico gratuito</a><a class="btn btn-ghost" href="{c.link(PAR['slug'])}">Conhecer o Método PAR 360</a></div>
<p class="fine">Diagnóstico gratuito, sem compromisso. Retorno em até 24 horas.</p>
</div>
<div class="hero-stage"><span class="ghost g1" aria-hidden="true"></span><span class="ghost g2" aria-hidden="true"></span>{serp_html()}</div>
</div>
<div class="wrap hero-facts" aria-label="A CR8 Conecta em números">
<div><b>2021</b><span>fundada em Curitiba por Carlos da Silva</span></div>
<div><b>3</b><span>pilares no Método PAR 360</span></div>
<div><b>6</b><span>serviços, do Google ao CRM</span></div>
</div></section>

{marquee_html()}

{ledger("Resultados de clientes", cases_table(), "Números de empresas que já aplicaram o método, medidos em vendas fechadas.")}

<section class="section" id="depoimentos"><div class="wrap"><h2>Na voz de quem já vive o resultado</h2><div class="videos" style="margin-top:2rem">{videos}</div></div></section>

<section class="section" id="metodo"><div class="wrap ledger"><div class="ledger-head"><h2>Três pilares, um só sistema</h2><p>O Método PAR 360 junta posicionamento, atração e retenção em um gerador de vendas contínuo, para a empresa crescer de forma previsível.</p><p>Cada solução tem a sua página: escolha pelo pilar ou comece pelo diagnóstico gratuito.</p><p><a href="{c.link(PAR['slug'])}">Ver o método completo</a></p></div>
<div class="pillars">{pillars_html}</div></div></section>

<section class="section"><div class="wrap ledger"><div class="ledger-head"><h2>Para quem é o método</h2><p>O Método PAR 360 foi desenhado para empresas que já têm mercado e clientes.</p></div>
<div><div class="two-col"><div><h3>Faz sentido se</h3>{checks(FAZ_SENTIDO)}</div><div><h3>Talvez ainda não seja o momento se</h3>{checks(NAO_AINDA, no=True)}</div></div>
<div class="prose" style="margin-top:2.2rem"><h2 class="h3-look">Agência de marketing em Curitiba e região metropolitana</h2><p>Já aplicamos o método em {esc(seg_text)}. O encaixe é de empresas de serviços e comércio especializado com ticket médio alto e decisão de compra mais longa.</p><p>Com base em Curitiba, atendemos empresas da cidade e da região metropolitana, e também clientes de outros estados e dos Estados Unidos. Se o seu segmento não está na lista, o diagnóstico confirma o encaixe.</p></div></div></div></section>

{ledger("Quem está por trás", '<div class="prose"><p>A CR8 Conecta foi fundada em 2021 por Carlos da Silva. Começamos com tráfego pago e evoluímos para o Método PAR 360, porque gerar contatos deixou de bastar: o resultado depende do que acontece antes e depois do anúncio.</p><p>Hoje o time reúne estratégia, copywriting, tráfego pago, automações e social media. <a href="' + c.link("sobre") + '">Conheça a CR8 Conecta e o time</a>.</p></div>' + faces_html(c))}

{ledger("Perguntas frequentes", faq(HOME_FAQ), "Respostas diretas sobre o método, o diagnóstico e o investimento.", section_id="faq")}

{cta_band(c, "Vamos olhar sua empresa de fora.", "O diagnóstico gratuito mostra como sua empresa aparece, atrai e converte hoje, e onde estão as oportunidades. Sem compromisso, com retorno em até 24 horas.")}
</main>"""
    html_text = head(c, title, desc, graph) + header(c) + body + footer(c) + tail(c)
    write_page("", html_text)


def mid_cta(c):
    return ('<section class="section mid-cta" aria-label="Diagnóstico gratuito"><div class="wrap mid-cta-row">'
            '<p>Quer saber se isso serve para a sua empresa?</p>'
            f'<a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Pedir diagnóstico gratuito</a>'
            '</div></section>')


def crm_sections(c):
    # Ilustrações ficam só no desktop (classe only-desktop): no celular a página fica mais curta e direta.
    origem = ('<div class="prose"><p>Sem CRM, a plataforma de anúncios só sabe quantas pessoas clicaram ou chamaram. Ela não sabe quem virou cliente. Com o CRM CR8 Conecta, cada contato entra com a origem registrada (campanha, anúncio e público) e, quando a venda acontece, a informação volta para o Google Ads e para o Meta Ads.</p>'
              '<p>As plataformas passam a otimizar para quem compra, e não só para quem clica. Você enxerga quais criativos e quais públicos geram venda e investe neles. Com o tempo, a campanha fica mais inteligente e tende a reduzir o custo por contato qualificado e por venda.</p></div>'
              + '<div class="only-desktop" style="margin-top:1.6rem">' + art.crm_feedback() + '</div>'
              + '<p class="fine-print">Esse retorno usa a API de Conversões da Meta e a importação de conversões do Google Ads. O resultado depende do volume de dados, do mercado e da qualidade do atendimento, e não prometemos um percentual de redução.</p>')
    auto = ('<div class="prose"><p>O CRM trabalha entre uma conversa e outra. Cada contato novo entra no funil sozinho, recebe a primeira resposta em segundos e é acompanhado nos dias certos, sem depender da memória de ninguém.</p></div>'
            + art.crm_autos()
            + '<div class="only-desktop"><h3 style="margin-top:2.4rem;margin-bottom:1rem">Como um fluxo funciona por dentro</h3>'
            + '<p class="muted" style="margin-bottom:1.2rem">Exemplo de uma imobiliária: quando a IA pede ajuda humana, o CRM decide para quem a conversa vai e em que etapa o cartão fica.</p>'
            + art.crm_flow() + '</div>'
            + '<h3 style="margin-top:2.4rem;margin-bottom:1rem">Inteligência artificial dentro do CRM</h3>'
            + '<div class="prose"><p>O CRM pode contar com inteligência artificial. O agente de IA trabalha dentro do funil: atende o contato assim que ele chega, entende o que ele precisa e só chama a equipe quando faz sentido. Quem vende recebe a conversa pronta, com o histórico, em vez de começar do zero.</p></div>'
            + art.crm_ia()
            + '<p class="fine-print">O agente é configurado para o seu negócio, com o que ele pode e não pode responder. Veja os detalhes em <a href="' + c.link("automacao-ia-atendimento") + '">Automação e IA no atendimento</a>.</p>')
    vend = ('<div class="prose"><p>O CRM não serve só para negociações longas. Para quem tem volume, ele é o jeito de controlar a rotina da equipe sem depender de cobrança manual: cada vendedor sabe o que fazer no dia e o gestor enxerga o que está acontecendo, sem planilha e sem perguntar no grupo.</p></div>'
            + art.crm_vendedores())
    conv = ('<div class="stack-fig"><div class="prose"><p>WhatsApp, Instagram e Facebook chegam à mesma caixa de entrada, com o histórico de cada pessoa e a etapa do funil ao lado. A equipe responde de um lugar só, sem trocar de aplicativo, e o dono enxerga tudo o que está acontecendo.</p><p>Os canais disponíveis dependem da configuração da conta. No diagnóstico, definimos quais fazem sentido para a sua operação.</p></div>'
            + '<div class="only-desktop">' + art.crm_inbox() + '</div>'
            + '<div class="prose"><p>A equipe acompanha conversas, oportunidades e tarefas pelo celular e recebe avisos quando algo precisa de ação: contato novo, visita marcada, proposta sem resposta. Quem está na rua não perde o momento de retomar o cliente.</p></div>'
            + '<div class="only-desktop">' + art.crm_mobile() + '</div></div>')
    caps = ('<div class="prose" style="margin-bottom:1.4rem"><p>Em vez de uma ferramenta para o funil, outra para o WhatsApp, outra para os formulários e outra para os lembretes, o CRM CR8 Conecta reúne tudo em uma plataforma. Menos assinaturas para pagar e acompanhar, e um só lugar para a equipe aprender.</p></div>' + art.crm_caps())
    return (ledger("Do anúncio à venda, e da venda de volta ao anúncio", origem, "Por que o CRM faz as campanhas ficarem mais inteligentes.", section_id="origem-do-lead")
            + ledger("Automações e inteligência artificial", auto, "Resposta, follow-up, qualificação e agenda.", section_id="automacoes")
            + ledger("A rotina dos vendedores sob controle", vend, "Para quem tem volume e equipe.", section_id="rotina-dos-vendedores")
            + ledger("Todas as conversas, no computador e no celular", conv, "Uma caixa de entrada para cada canal.", section_id="conversas")
            + ledger("Uma plataforma no lugar de várias ferramentas", caps, "O que vem no CRM CR8 Conecta.", section_id="plataforma"))


def extra_sections(c, s):
    """Mockups e blocos de IA das páginas de Perfil da Empresa no Google e de Criação de Sites."""
    if s["slug"] == "google-meu-negocio":
        met = ('<div class="prose"><p>Depois da otimização, você acompanha o que o perfil gera: quantas pessoas viram a empresa na Busca e no Maps, quantas ligaram, pediram rota ou chamaram no WhatsApp. É a leitura que mostra o que está funcionando e o que ajustar.</p></div>'
               '<div class="stack-fig only-desktop">' + art.metricas() + '</div>')
        ia = ('<div class="prose"><p>Hoje muita gente pergunta a ferramentas de inteligência artificial qual empresa contratar. Essas ferramentas recomendam o que entendem sem ambiguidade. Por isso, além de aparecer no Google e no Maps, trabalhamos o perfil para a sua empresa também ser entendida e citada nas respostas de IA, de forma orgânica, sem anúncio pago.</p>'
              '<p>Na prática: descrição e serviços claros, categorias corretas, avaliações reais e recentes, perguntas e respostas e dados iguais aos do site e das redes sociais. Nenhuma ferramenta garante que vai recomendar uma empresa, e por isso fazemos tudo o que está ao alcance dela.</p></div>'
              '<div class="stack-fig only-desktop">' + art.ia_resposta() + '</div>')
        return (ledger("Acompanhe os números do perfil", met, "Visualizações, ligações, rotas e cliques.", section_id="numeros")
                + ledger("Também nas respostas de inteligência artificial", ia, "Aparecer no Google e ser recomendado pela IA.", section_id="inteligencia-artificial"))
    if s["slug"] == "criacao-de-sites":
        ia = ('<div class="prose"><p>Um site bom precisa ser encontrado por quem pesquisa no Google e também por quem pergunta a uma ferramenta de inteligência artificial. Trabalhamos para o seu site e a sua empresa aparecerem nas respostas de IA de forma orgânica, sem anúncio pago.</p>'
              '<p>Na prática: texto claro sobre o que a empresa faz, para quem, onde atende e quais são os diferenciais, perguntas frequentes escritas como o cliente pergunta, dados estruturados e informações iguais às do Perfil da Empresa no Google. Nenhuma ferramenta garante a recomendação, mas a empresa organizada tem mais chance de ser entendida.</p></div>'
              '<div class="stack-fig only-desktop">' + art.ia_resposta() + '</div>')
        return (ledger("Também nas respostas de inteligência artificial", ia, "Aparecer no Google e ser recomendado pela IA.", section_id="inteligencia-artificial"))
    return ""


def build_solution(s):
    c = Ctx(s["slug"])
    url = c.url()
    p = PILLARS[s["pillar"]]
    trail_schema = [("Início", SITE + "/"), (s["nav"], url)]
    service = {
        "@type": "Service", "@id": url + "#service", "name": s["service_type"], "serviceType": s["service_type"],
        "description": s["desc"], "url": url, "provider": {"@id": SITE + "/#organization"},
        "areaServed": [{"@type": "City", "name": "Curitiba"}, {"@type": "AdministrativeArea", "name": "Região Metropolitana de Curitiba"}, {"@type": "Country", "name": "Brasil"}],
        "audience": {"@type": "BusinessAudience", "audienceType": "Empresas de serviços e comércio especializado"},
    }
    graph = [
        org_node(), website_node(),
        webpage_node(url, s["title"], s["desc"], extra={"breadcrumb": {"@id": url + "#breadcrumb"}, "about": {"@id": url + "#service"}}),
        breadcrumb_node(url, trail_schema), service, faq_node(url, s["faq"]),
    ]
    what_html = '<div class="prose">%s</div><h3 style="margin-top:2rem;margin-bottom:1rem">Faz sentido para</h3>%s' % (
        "".join("<p>%s</p>" % esc(t) for t in s["what"]), checks(s["for_whom"])
    )
    steps_html = steps(s["steps"])
    if s.get("note"):
        steps_html += '<p class="note" style="margin-top:2.2rem">%s</p>' % esc(s["note"])
    cases_section = ""
    if s.get("show_cases"):
        cases_section = ledger("Resultados com tráfego pago", cases_table(), "Números de clientes que usaram o método.")
    related = index_list(c, s["related"])
    body = f"""<main id="conteudo">
<section class="page-hero"><div class="wrap">
{crumbs(c, [("Início", ""), (s["nav"], None)])}
<div class="page-hero-grid"><div>
<h1>{esc(s["h1"])}</h1>
<p class="lead">{esc(s["lead"])}</p>
<p class="pillar-flag {p['cls']}">Pilar {p['name']} do <a href="{c.link(PAR['slug'])}">Método PAR 360</a></p>
<div class="btn-row"><a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Pedir diagnóstico gratuito</a></div>
<p class="updated">Atualizado em <time datetime="{MODIFIED}">{MODIFIED_HUMAN}</time></p>
</div>{art.fig(s["slug"])}</div>
</div></section>
{ledger(s["what_title"], what_html)}
{ledger("O que entregamos", deliver(s["deliver"]))}
{mid_cta(c)}
{crm_sections(c) if s["slug"] == "crm-de-vendas" else ""}
{extra_sections(c, s)}
{ledger("Como funciona", steps_html)}
{cases_section}
{ledger("Perguntas frequentes", faq(s["faq"]))}
{ledger("Continue explorando", related, "Soluções que se conectam a esta dentro do Método PAR 360.")}
{cta_band(c, "Quer ver como isso funcionaria na sua empresa?", "O diagnóstico gratuito analisa sua empresa nos três pilares do método e mostra por onde começar. Sem compromisso.")}
</main>"""
    html_text = head(c, s["title"], s["desc"], graph) + header(c, current=None) + body + footer(c) + tail(c)
    write_page(s["slug"], html_text)


def build_par():
    c = Ctx(PAR["slug"])
    url = c.url()
    graph = [
        org_node(), website_node(),
        webpage_node(url, PAR["title"], PAR["desc"], extra={"breadcrumb": {"@id": url + "#breadcrumb"}}),
        breadcrumb_node(url, [("Início", SITE + "/"), ("Método PAR 360", url)]),
        faq_node(url, PAR["faq"]),
    ]
    sections = ""
    for p in PAR["pillars"]:
        links = [(s) for s in p["links"]]
        body = (
            '<div class="prose"><p>%s</p></div><h3 style="margin-top:2rem;margin-bottom:1rem">O que a empresa conquista</h3>%s'
            '<h3 style="margin-top:2.2rem;margin-bottom:1rem">Soluções deste pilar</h3>%s'
        ) % (esc(p["text"]), checks(p["gains"]), index_list(c, links))
        if p["extra"]:
            body += '<p class="fine-print">%s</p>' % esc(p["extra"])
        sections += ledger("Pilar " + p["name"], body, p["tagline"], section_id=p["name"].lower())
    why = '<div class="prose">%s</div>' % "".join("<p>%s</p>" % esc(t) for t in PAR["why"])
    html_body = f"""<main id="conteudo">
<section class="page-hero"><div class="wrap">
{crumbs(c, [("Início", ""), ("Método PAR 360", None)])}
<div class="page-hero-grid"><div>
<h1>{esc(PAR["h1"])}</h1>
<p class="lead">{esc(PAR["lead"])}</p>
<div class="btn-row"><a class="btn btn-primary" href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">Pedir diagnóstico gratuito</a></div>
<p class="updated">Atualizado em <time datetime="{MODIFIED}">{MODIFIED_HUMAN}</time></p>
</div>{art.fig(PAR["slug"])}</div>
</div></section>
{ledger("Por que três pilares", why)}
{sections}
{ledger("Como é a jornada", steps(PAR["steps"]))}
<section class="section"><div class="wrap ledger"><div class="ledger-head"><h2>Para quem é o método</h2><p>Desenhado para empresas que já têm mercado e clientes.</p></div>
<div class="two-col"><div><h3>Faz sentido se</h3>{checks(FAZ_SENTIDO)}</div><div><h3>Talvez ainda não seja o momento se</h3>{checks(NAO_AINDA, no=True)}</div></div></div></section>
{ledger("Perguntas frequentes", faq(PAR["faq"]))}
{cta_band(c, "Comece pelo diagnóstico gratuito.", "Olhamos sua empresa de fora, nos três pilares, e mostramos onde estão as oportunidades. Sem compromisso, com retorno em até 24 horas.")}
</main>"""
    write_page(PAR["slug"], head(c, PAR["title"], PAR["desc"], graph) + header(c, PAR["slug"]) + html_body + footer(c) + tail(c))


def build_about():
    c = Ctx("sobre")
    url = c.url()
    title = "Sobre a CR8 Conecta | Agência de marketing em Curitiba"
    desc = "Conheça a CR8 Conecta, agência de marketing e vendas de Curitiba no mercado desde 2021, e o time por trás do Método PAR 360."
    persons = [
        {"@type": "Person", "name": n, "jobTitle": r, "worksFor": {"@id": SITE + "/#organization"}}
        for n, r, _, _ in TEAM
    ]
    graph = [
        org_node(), website_node(),
        webpage_node(url, title, desc, page_type="AboutPage", extra={"breadcrumb": {"@id": url + "#breadcrumb"}}),
        breadcrumb_node(url, [("Início", SITE + "/"), ("Sobre", url)]),
    ] + persons
    team = ""
    for n, r, fn, bio in TEAM:
        initials = "".join(w[0] for w in n.split()[:2])
        team += (
            '<li><div class="avatar"><span aria-hidden="true">%s</span><img src="%s" alt="%s" width="400" height="400" loading="lazy" onerror="this.remove()"></div>'
            "<h3>%s</h3><p class=\"role\">%s</p><p>%s</p></li>"
            % (esc(initials), c.root + "assets/team/" + fn, attr(n), esc(n), esc(r), esc(bio))
        )
    principles = deliver([
        ("Resultado, não relatório", "Nosso trabalho é medido em clientes novos e faturamento, e não em curtidas, alcance ou impressões."),
        ("Estrutura completa, não serviço avulso", "Posicionamento, Atração e Retenção: três pilares integrados que trabalham juntos para gerar clientes de forma previsível."),
        ("Crescemos junto com você", "Quanto mais sua empresa cresce, mais investimos no seu resultado. O seu sucesso é o nosso sucesso."),
    ])
    facts = [
        ("Nome", "CR8 Conecta"),
        ("Tipo", "Agência de marketing e vendas"),
        ("Fundação", "2021"),
        ("Sede", "Curitiba, Paraná, Brasil"),
        ("Onde atua", "Curitiba e região metropolitana, outros estados do Brasil e Estados Unidos"),
        ("Fundador e CEO", "Carlos da Silva"),
        ("Método", "Método PAR 360: Posicionamento, Atração e Retenção"),
        ("Soluções", ", ".join(s["nav"] for s in SOLUTIONS)),
        ("WhatsApp", PHONE),
        ("E-mail", EMAIL),
        ("Instagram", "@cr8conecta"),
    ]
    facts_html = '<dl class="facts">%s</dl>' % "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (esc(k), esc(v)) for k, v in facts)
    story = (
        '<div class="prose"><p>A CR8 Conecta está no mercado desde 2021. Começamos focados em tráfego pago e percebemos que gerar contatos já não bastava: o resultado dependia de tudo o que acontece antes e depois do anúncio. Dessa percepção nasceu o Método PAR 360.</p>'
        "<p>O método reúne Posicionamento, Atração e Retenção em um sistema completo, que funciona como um gerador de vendas contínuo, cobrindo desde a forma como a empresa se posiciona até o acompanhamento, a recompra e a indicação vindas do mesmo cliente.</p>"
        "<p>Já aplicamos o método em diversos setores, incluindo imobiliárias. Se há um pilar em que mais fazemos diferença, é a Retenção: o que acontece com o contato depois que ele demonstra interesse e ainda não fechou.</p></div>"
    )
    leader = (
        '<div class="prose"><p>Carlos da Silva é sócio-fundador e CEO da CR8 Conecta. Ele lidera a estratégia da agência e acompanha de perto o trabalho com cada cliente. Ao lado dele, um time que reúne copywriting, tráfego pago, automações, social media e planejamento de funil.</p></div>'
        '<ul class="team" style="margin-top:2.5rem">%s</ul>' % team
    )
    body = f"""<main id="conteudo">
<section class="page-hero hero-light"><div class="wrap">
{crumbs(c, [("Início", ""), ("Sobre", None)])}
<h1>Uma agência de Curitiba focada em resultado comercial</h1>
<p class="lead">A CR8 Conecta é uma agência de marketing e vendas de Curitiba, fundada em 2021. Trabalhamos com empresas de serviços e comércio especializado que já têm mercado e querem vender de forma previsível.</p>
</div></section>
{ledger("Nossa história", story)}
{ledger("Como trabalhamos", principles)}
{ledger("Quem conduz e o time", leader)}
{ledger("A CR8 Conecta em resumo", facts_html, "Dados da empresa, para consulta rápida.")}
{cta_band(c, "Vamos conversar sobre a sua empresa?", "Peça o diagnóstico gratuito e veja como o Método PAR 360 se aplica ao seu negócio. Sem compromisso.")}
</main>"""
    write_page("sobre", head(c, title, desc, graph) + header(c, "sobre") + body + footer(c) + tail(c))


def build_contact():
    c = Ctx("contato")
    url = c.url()
    title = "Contato e diagnóstico gratuito | CR8 Conecta"
    desc = "Peça o diagnóstico gratuito da sua empresa. Fale com a CR8 Conecta pelo WhatsApp (41) 99525-7590 ou por e-mail. Retorno em até 24 horas."
    graph = [
        org_node(), website_node(),
        webpage_node(url, title, desc, page_type="ContactPage", extra={"breadcrumb": {"@id": url + "#breadcrumb"}}),
        breadcrumb_node(url, [("Início", SITE + "/"), ("Contato", url)]),
    ]
    info = f"""<dl class="contact-list">
<div><dt>WhatsApp</dt><dd><a href="{WA_URL}" data-cta="whatsapp" target="_blank" rel="noopener">{PHONE}</a></dd></div>
<div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}" data-cta="email">{EMAIL}</a></dd></div>
<div><dt>Instagram</dt><dd><a href="{INSTAGRAM}" target="_blank" rel="noopener">@cr8conecta</a></dd></div>
<div><dt>Onde estamos</dt><dd>Curitiba, PR. Atendimento em Curitiba e região metropolitana, e também em outros estados.</dd></div>
<div><dt>Retorno</dt><dd>Em até 24 horas</dd></div>
</dl>"""
    form = f"""<form class="form" id="contact-form" data-whatsapp="{WHATSAPP}">
<div><label for="nome">Seu nome</label><input id="nome" name="nome" type="text" autocomplete="name" required></div>
<div><label for="empresa">Empresa</label><input id="empresa" name="empresa" type="text" autocomplete="organization" required></div>
<div><label for="segmento">Segmento</label><input id="segmento" name="segmento" type="text" placeholder="Ex.: refrigeração, imobiliária, oficina"></div>
<div><label for="cidade">Cidade e região de atuação</label><input id="cidade" name="cidade" type="text" placeholder="Ex.: Curitiba e região metropolitana"></div>
<div><label for="interesse">O que você quer melhorar primeiro?</label>
<select id="interesse" name="interesse"><option value="">Ainda não sei, quero o diagnóstico</option><option>Aparecer mais no Google</option><option>Gerar clientes novos com anúncios</option><option>Organizar o comercial e o follow-up</option><option>Atender mais rápido no WhatsApp</option><option>Ter um site novo ou páginas para anúncios</option></select></div>
<div><button class="btn btn-primary" type="submit">Enviar pelo WhatsApp</button><p class="hint" style="margin-top:0.8rem">Ao enviar, o WhatsApp abre com a mensagem pronta para você conferir. Este site não guarda os dados do formulário.</p></div>
</form>"""
    body = f"""<main id="conteudo">
<section class="page-hero hero-light"><div class="wrap">
{crumbs(c, [("Início", ""), ("Contato", None)])}
<h1>Vamos olhar sua empresa de fora</h1>
<p class="lead">O diagnóstico gratuito analisa como sua empresa aparece, atrai e converte hoje e mostra onde estão as oportunidades. Sem compromisso, com retorno em até 24 horas.</p>
</div></section>
<section class="section"><div class="wrap ledger"><div><h2 style="font-size:1.6rem;margin-bottom:1.2rem">Fale direto</h2>{info}</div><div><h2 style="font-size:1.6rem;margin-bottom:1.5rem">Peça seu diagnóstico</h2>{form}</div></div></section>
<section class="section" id="mapa"><div class="wrap ledger"><div class="ledger-head"><h2>Onde estamos</h2><p>Base em Curitiba, PR. Atendemos empresas da cidade, da região metropolitana e de todo o Brasil.</p><p><a href="https://www.google.com/maps?cid=13746290579143037967" target="_blank" rel="noopener">Abrir no Google Maps</a></p></div><div><div class="map"><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d461059.48963458673!2d-49.2994293!3d-25.470765099999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd9ded0238c3c3d3%3A0xbec4a273651e940f!2sAg%C3%AAncia%20de%20Marketing%20Digital%20%7C%20Cr8%20Conecta!5e0!3m2!1spt-BR!2sbr!4v1791938567131!5m2!1spt-BR!2sbr" title="Mapa com a localização da CR8 Conecta, agência de marketing em Curitiba" width="600" height="450" style="border:0" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe></div></div></div></section>
</main>"""
    write_page("contato", head(c, title, desc, graph) + header(c, "contato") + body + footer(c) + tail(c))


def build_privacy():
    c = Ctx("politica-de-privacidade")
    url = c.url()
    title = "Política de privacidade | CR8 Conecta"
    desc = "Como a CR8 Conecta trata os dados de quem visita este site e de quem entra em contato, de acordo com a Lei Geral de Proteção de Dados (LGPD)."
    graph = [
        org_node(), website_node(),
        webpage_node(url, title, desc, extra={"breadcrumb": {"@id": url + "#breadcrumb"}}),
        breadcrumb_node(url, [("Início", SITE + "/"), ("Política de privacidade", url)]),
    ]
    body = f"""<main id="conteudo">
<section class="page-hero hero-light"><div class="wrap">
{crumbs(c, [("Início", ""), ("Política de privacidade", None)])}
<h1>Política de privacidade</h1>
<p class="lead">Aqui explicamos, de forma simples, quais dados este site coleta, para que usamos e como você pode exercer seus direitos, conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018).</p>
<p class="updated">Atualizada em <time datetime="{MODIFIED}">{MODIFIED_HUMAN}</time></p>
</div></section>
<section class="section"><div class="wrap"><div class="prose" style="max-width:48rem">
<h2>Quem somos</h2>
<p>A CR8 Conecta é uma agência de marketing e vendas com base em Curitiba, PR, e é a responsável pelo tratamento dos dados descritos nesta página. Para qualquer assunto sobre privacidade, fale conosco pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a> ou pelo WhatsApp {PHONE}.</p>
<h2>Quais dados tratamos</h2>
<ul>
<li><strong>Dados que você nos envia no formulário de contato:</strong> nome, empresa, segmento, cidade e região de atuação e o que você quer melhorar primeiro. O formulário não envia nada para o nosso servidor: ele monta uma mensagem e abre o seu WhatsApp para você conferir e enviar. Este site não guarda os dados do formulário.</li>
<li><strong>Dados que você nos envia por WhatsApp, telefone ou e-mail:</strong> o que você escrever e o seu número ou e-mail. Esses dados ficam no WhatsApp e no e-mail da CR8 Conecta.</li>
<li><strong>Dados de navegação:</strong> o site usa o Google Tag Manager para medir o uso das páginas e registrar ações como cliques nos botões de contato, envio do formulário e reprodução de vídeos. Conforme as ferramentas configuradas nele, isso pode incluir identificadores de navegador (cookies), tipo de aparelho, páginas visitadas e origem da visita.</li>
</ul>
<h2>Para que usamos os dados</h2>
<ul>
<li>Responder ao seu contato e preparar o diagnóstico gratuito que você pediu.</li>
<li>Entender como o site é usado e melhorá-lo.</li>
<li>Medir e otimizar nossas campanhas de divulgação.</li>
<li>Cumprir obrigações legais, quando houver.</li>
</ul>
<h2>Em que bases legais</h2>
<p>Tratamos os dados para atender ao seu pedido de contato e de diagnóstico, para nosso legítimo interesse em melhorar o site e a divulgação dos nossos serviços e, quando a lei exigir, com o seu consentimento. Você pode retirar o consentimento quando quiser.</p>
<h2>Com quem compartilhamos</h2>
<p>Não vendemos seus dados. Eles podem ser tratados por fornecedores que fazem o site e o atendimento funcionarem:</p>
<ul>
<li><strong>Google:</strong> Google Tag Manager e Google Maps, no mapa da página de contato. Os vídeos de depoimento usam o YouTube e só são carregados quando você clica para assistir.</li>
<li><strong>WhatsApp (Meta):</strong> quando você nos chama pelo WhatsApp, a conversa passa a seguir os termos e a política de privacidade do WhatsApp.</li>
<li><strong>Hospedagem do site:</strong> a Hostinger guarda os arquivos do site e os registros técnicos de acesso.</li>
</ul>
<p>Alguns desses fornecedores podem tratar dados fora do Brasil, seguindo as regras de transferência internacional da LGPD.</p>
<h2>Cookies</h2>
<p>Cookies são pequenos arquivos que o navegador guarda para lembrar informações sobre a sua visita. Os cookies deste site vêm das ferramentas de medição carregadas pelo Google Tag Manager. Você pode apagar ou bloquear cookies nas configurações do seu navegador. Algumas medições deixam de funcionar se você bloquear, mas o site continua abrindo normalmente.</p>
<h2>Por quanto tempo guardamos</h2>
<p>Guardamos os dados pelo tempo necessário para atender ao seu contato e para cumprir obrigações legais. Depois disso, eles são apagados ou anonimizados.</p>
<h2>Seus direitos</h2>
<p>Pela LGPD, você pode pedir a qualquer momento: confirmação de que tratamos seus dados, acesso a eles, correção, anonimização, bloqueio ou eliminação de dados desnecessários, portabilidade, informação sobre com quem compartilhamos e a retirada do consentimento. Para isso, escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>. Respondemos dentro do prazo previsto em lei. Se achar que seus dados foram tratados de forma indevida, você também pode recorrer à Autoridade Nacional de Proteção de Dados (ANPD).</p>
<h2>Segurança</h2>
<p>O site usa conexão segura (HTTPS) e adotamos medidas razoáveis para proteger os dados contra acesso indevido. Nenhum sistema é totalmente livre de riscos, e por isso pedimos que você não envie senhas nem dados de pagamento por mensagem.</p>
<h2>Mudanças nesta política</h2>
<p>Podemos atualizar esta página quando o site ou a lei mudarem. A data no topo mostra a última atualização.</p>
</div></div></section>
</main>"""
    write_page("politica-de-privacidade", head(c, title, desc, graph) + header(c, "politica-de-privacidade") + body + footer(c) + tail(c))


def build_404():
    c = Ctx("")
    c.depth = 0
    title = "Página não encontrada | CR8 Conecta"
    desc = "A página que você procurou não existe. Volte para a página inicial da CR8 Conecta."
    # 404 usa caminhos absolutos para funcionar em qualquer URL
    class Abs(Ctx):
        @property
        def root(self):
            return "/"
    a = Abs("")
    body = f"""<main id="conteudo"><section class="page-hero"><div class="wrap">
<h1>Essa página não foi encontrada</h1>
<p class="lead">O endereço pode ter mudado ou não existe mais. Veja as soluções da CR8 Conecta ou volte ao início.</p>
<div class="btn-row"><a class="btn btn-primary" href="/">Ir para a página inicial</a><a class="btn btn-ghost" href="/metodo-par-360/">Conhecer o Método PAR 360</a></div>
</div></section></main>"""
    text = head(a, title, desc, [org_node()], noindex=True) + header(a) + body + footer(a) + tail(a)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(destaque(text))


def build_files():
    pages = [""] + [s["slug"] for s in SOLUTIONS] + [PAR["slug"], "sobre", "contato", "politica-de-privacidade"]
    urls = []
    for slug in pages:
        loc = SITE + "/" + (slug + "/" if slug else "")
        pr = "1.0" if slug == "" else ("0.9" if slug in [s["slug"] for s in SOLUTIONS] or slug == PAR["slug"] else ("0.3" if slug == "politica-de-privacidade" else "0.6"))
        urls.append("<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (loc, MODIFIED, pr))
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join(urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
    robots = "# CR8 Conecta: o site é aberto a buscadores e a ferramentas de IA.\nUser-agent: *\nAllow: /\n\n"
    robots += "".join("User-agent: %s\nAllow: /\n\n" % b for b in bots)
    robots += "Sitemap: %s/sitemap.xml\n" % SITE
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    lines = [
        "# CR8 Conecta",
        "",
        "> Agência de marketing e vendas de Curitiba (PR), fundada em 2021 por Carlos da Silva. Usa o Método PAR 360 (Posicionamento, Atração e Retenção) para empresas de serviços e comércio especializado venderem de forma previsível, sem depender só de indicação. Atende Curitiba e região metropolitana, outros estados do Brasil e os Estados Unidos.",
        "",
        "## Soluções",
        "",
    ]
    for s in SOLUTIONS:
        lines.append("- [%s](%s/%s/): %s" % (s["nav"], SITE, s["slug"], s["desc"]))
    lines += [
        "",
        "## Sobre a empresa",
        "",
        "- [Método PAR 360](%s/%s/): %s" % (SITE, PAR["slug"], PAR["desc"]),
        "- [Sobre a CR8 Conecta](%s/sobre/): história, time e dados da empresa." % SITE,
        "- [Contato e diagnóstico gratuito](%s/contato/): WhatsApp %s, e-mail %s." % (SITE, PHONE, EMAIL),
        "",
        "## Fatos rápidos",
        "",
        "- Fundação: 2021. Sede: Curitiba, Paraná, Brasil.",
        "- Fundador e CEO: Carlos da Silva.",
        "- O investimento em anúncios é pago pelo cliente diretamente às plataformas (Google e Meta). A CR8 Conecta cobra pela gestão.",
        "- Diagnóstico gratuito, sem compromisso, com retorno em até 24 horas.",
        "",
    ]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    build_home()
    for s in SOLUTIONS:
        build_solution(s)
    build_par()
    build_about()
    build_contact()
    build_privacy()
    build_404()
    build_files()
    print("ok", OUT, "preview" if PREVIEW else "prod")
