# -*- coding: utf-8 -*-
"""Ilustrações em HTML/CSS (sem imagens externas) para as páginas de solução."""

def _cap(t):
    return '<p class="fig-cap">Ilustração: %s</p>' % t

def _wrap(cls, label, inner, cap):
    return '<figure class="fig %s" role="img" aria-label="%s">%s%s</figure>' % (cls, label, inner, _cap(cap))

def perfil():
    ic = {
      "Rotas": '<path d="M12 2 2 12l10 10 10-10L12 2zm1 13v-3H9v3H7v-4a1 1 0 0 1 1-1h5V7l3.5 3.5L13 14z" fill="currentColor"/>',
      "Ligar": '<path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z" fill="currentColor"/>',
      "WhatsApp": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 13.9c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9 0-1.4.7-2 1-2.3.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1.1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3z" fill="currentColor"/>',
      "Site": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm6.9 6h-2.9a15.6 15.6 0 0 0-1.4-3.6A8 8 0 0 1 18.9 8zM12 4c.8 1.2 1.5 2.5 1.9 4h-3.8c.4-1.5 1.1-2.8 1.9-4zM4.3 14a8 8 0 0 1 0-4h3.4a16.5 16.5 0 0 0 0 4H4.3zm.8 2h2.9c.3 1.3.8 2.5 1.4 3.6A8 8 0 0 1 5.1 16zM8 8H5.1a8 8 0 0 1 4.3-3.6C8.8 5.5 8.3 6.7 8 8zm4 12c-.8-1.2-1.5-2.5-1.9-4h3.8c-.4 1.5-1.1 2.8-1.9 4zm2.3-6H9.7a14.7 14.7 0 0 1 0-4h4.6a14.7 14.7 0 0 1 0 4zm.3 5.6c.6-1.1 1.1-2.3 1.4-3.6h2.9a8 8 0 0 1-4.3 3.6zm1.7-5.6a16.5 16.5 0 0 0 0-4h3.4a8 8 0 0 1 0 4h-3.4z" fill="currentColor"/>',
    }
    acts = "".join('<span><i><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></i>%s</span>' % (v, k) for k, v in ic.items())
    inner = """<div class="gb">
<div class="gb-map" aria-hidden="true"><svg viewBox="0 0 400 150" preserveAspectRatio="xMidYMid slice"><rect width="400" height="150" fill="#e9e6e1"/><path d="M250 0h150v70H300z" fill="#d6e4cf"/><path d="M0 110 400 60" stroke="#fff" stroke-width="12"/><path d="M120 0v150M300 0 260 150M0 30h400" stroke="#fff" stroke-width="7"/><path d="M0 85h400M200 0v150" stroke="#f7f5f1" stroke-width="4"/><path d="M0 150 70 120 140 150z" fill="#c9dbe6"/></svg>
<span class="gb-pin"><svg viewBox="0 0 24 32"><path d="M12 0C5.4 0 0 5.2 0 11.7 0 20 12 32 12 32s12-12 12-20.3C24 5.2 18.6 0 12 0z" fill="#d93a2f"/><circle cx="12" cy="11.5" r="4.5" fill="#fff"/></svg></span><span class="gb-dot d1"></span><span class="gb-dot d2"></span><span class="gb-dot d3"></span></div>
<div class="gb-sheet"><span class="gb-handle"></span>
<b class="gb-name">Sua Empresa</b>
<div class="gb-rate"><strong>4,9</strong><span class="gb-st">&#9733;&#9733;&#9733;&#9733;&#9733;</span><small>(128)</small></div>
<small class="gb-cat">Prestador de serviços · Curitiba</small>
<small class="gb-open"><em>Aberto</em> · Fecha às 18:00</small>
<div class="gb-acts">%s</div>
<div class="gb-ph"><i class="a"></i><i class="b"></i><i class="c"></i></div>
<div class="gb-rev"><span class="gb-av">M</span><div><span class="gb-st sm">&#9733;&#9733;&#9733;&#9733;&#9733;</span><p>“Atendimento rápido e muito profissional. Recomendo!”</p></div></div>
</div></div>""" % acts
    return _wrap("f-gbp", "Ilustração de uma ficha do Perfil da Empresa no Google no celular: mapa com a empresa marcada, nota 4,9 com avaliações, horário de funcionamento, botões de rota, ligar, WhatsApp e site, fotos e uma avaliação de cliente.", inner, "a ficha da empresa no Google e no Maps (exemplo).")

def landing():
    inner = """<div class="ad-chip"><span>Anúncio</span><svg viewBox="0 0 24 12" aria-hidden="true"><path d="M0 6h20M15 1l6 5-6 5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><span>Página de captura</span></div>
<div class="win"><div class="win-bar"><i></i><i></i><i></i></div>
<div class="lp"><div class="lp-copy"><u class="b1"></u><u class="b1 s"></u><u class="b2"></u><u class="b2 s"></u><ul><li>Atendimento na sua região</li><li>Orçamento sem compromisso</li><li>Resposta rápida no WhatsApp</li></ul></div>
<div class="lp-form"><span class="f"></span><span class="f"></span><span class="btnx">Pedir orçamento</span></div></div></div>"""
    return _wrap("f-landing", "Ilustração de uma landing page: do anúncio para uma página objetiva com benefícios e um formulário curto com o botão Pedir orçamento.", inner, "uma página com um objetivo só, pronta para receber anúncios.")

def site():
    inner = """<div class="win"><div class="win-bar"><i></i><i></i><i></i></div>
<div class="st"><div class="st-nav"><span class="lg"></span><u></u><u></u><u></u><span class="btnx sm">Contato</span></div>
<div class="st-hero"><u class="b1"></u><u class="b1 s"></u><u class="b2"></u><span class="btnx">Pedir orçamento</span></div>
<div class="st-cards"><span><i></i><u></u></span><span><i></i><u></u></span><span><i></i><u></u></span></div></div></div>
<div class="phone" aria-hidden="true"><div class="ph-top"></div><u class="b1"></u><u class="b2"></u><span class="btnx sm">WhatsApp</span><div class="ph-card"></div></div>"""
    return _wrap("f-site", "Ilustração de um site institucional no computador, com menu, destaque, botão e serviços, e a mesma página adaptada para o celular.", inner, "o mesmo site no computador e no celular.")

def redes():
    tiles = [("t1","Dica"),("t2","Bastidores"),("t3","Reels"),("t4","Cliente"),("t5","Serviço"),("t6","Antes e depois"),("t7","Depoimento"),("t8","Dica"),("t9","Reels")]
    grid = "".join('<span class="%s"><b>%s</b></span>' % (c, n) for c, n in tiles)
    inner = """<div class="ig-top"><span class="av"></span><div><b>@suaempresa</b><small>Serviços em Curitiba</small></div><span class="follow">Seguir</span></div>
<div class="ig-grid">%s</div>""" % grid
    return _wrap("f-redes", "Ilustração de um perfil de Instagram da empresa com uma grade de publicações organizadas em dicas, bastidores, reels, clientes e depoimentos.", inner, "um perfil com identidade e conteúdo que passa credibilidade.")

def trafego():
    inner = """<div class="ads"><div class="gad"><span class="tag">Anúncio</span><b>Sua empresa em Curitiba</b><u class="b2"></u><u class="b2 s"></u><div class="sl"><span>Orçamento</span><span>Serviços</span></div><small>Google Ads</small></div>
<div class="mad"><div class="m-top"><span class="av"></span><div><b>Sua empresa</b><small>Patrocinado</small></div></div><div class="m-img"></div><div class="m-cta"><span>Fale com a gente</span><span class="btnx sm">Enviar mensagem</span></div><small>Meta Ads</small></div></div>
<div class="arrow-down" aria-hidden="true"><svg viewBox="0 0 12 22"><path d="M6 0v18M1 13l5 6 5-6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></div>
<div class="lead-chip"><span class="wa"></span><div><b>Novo contato no WhatsApp</b><small>Cliente pedindo orçamento</small></div></div>"""
    return _wrap("f-trafego", "Ilustração de um anúncio no Google e de um anúncio no Instagram e Facebook levando um novo contato direto para o WhatsApp da empresa.", inner, "anúncios no Google e na Meta que levam o cliente para a conversa.")

def crm():
    cols = [("Novo contato", ["Cliente A","Cliente B"]),("Em conversa", ["Cliente C"]),("Proposta", ["Cliente D"]),("Fechado", ["Cliente E"])]
    h = ""
    for i, (n, cards) in enumerate(cols):
        cs = "".join('<span class="kc"><b>%s</b><u></u></span>' % c for c in cards)
        h += '<div class="kcol%s"><h4>%s</h4>%s</div>' % (" won" if i == 3 else "", n, cs)
    inner = '<div class="kanban">%s</div><div class="follow-chip"><span class="clock"></span><span>Follow-up agendado para amanhã</span></div>' % h
    return _wrap("f-crm", "Ilustração de um funil de vendas em colunas: novo contato, em conversa, proposta e fechado, com um lembrete de follow-up agendado.", inner, "cada contato em uma etapa, sem ficar perdido.")

def ia():
    inner = """<div class="wa-top"><span class="av"></span><div><b>Sua empresa</b><small>online</small></div></div>
<div class="wa-chat"><p class="bubble them">Oi, vocês atendem em Pinhais?</p>
<p class="bubble us"><em>Atendimento por IA</em>Atendemos sim! Qual serviço você precisa?</p>
<p class="bubble them">Preciso de um orçamento.</p>
<p class="bubble us"><em>Atendimento por IA</em>Perfeito. Vou chamar alguém da equipe para continuar com você.</p></div>
<div class="follow-chip"><span class="handoff"></span><span>Conversa passa para a equipe</span></div>"""
    return _wrap("f-ia", "Ilustração de uma conversa de WhatsApp em que o atendimento por inteligência artificial responde ao cliente e passa a conversa para a equipe.", inner, "resposta imediata e a equipe assumindo na hora certa.")

def par_loop():
    inner = """<div class="loop">
<div class="node n1"><b>Posicionamento</b><small>Ser encontrado e parecer o melhor</small></div>
<span class="conn" aria-hidden="true"></span>
<div class="node n2"><b>Atração</b><small>Anúncios para quem já procura</small></div>
<span class="conn" aria-hidden="true"></span>
<div class="node n3"><b>Retenção</b><small>Comercial organizado e acompanhamento</small></div>
<div class="back" aria-hidden="true"><span>Clientes e indicações realimentam o ciclo</span></div></div>"""
    return _wrap("f-loop", "Ilustração do Método PAR 360: Posicionamento leva a Atração, que leva a Retenção, e os clientes e indicações voltam a alimentar o ciclo.", inner, "os três pilares funcionando como um ciclo.")


# ---------------------------------------------------------------------------
# Mockups extras: site no computador e no celular, números do perfil e resposta de IA
# ---------------------------------------------------------------------------
def devices():
    inner = """<div class="dv-stage"><div class="dv-laptop"><div class="dv-screen"><div class="sx">
<div class="sx-nav"><span class="sx-logo"><i></i>Sua Empresa</span><span class="sx-links"><b>Início</b><b>Serviços</b><b>Sobre</b><b>Contato</b></span><span class="sx-btn">Pedir orçamento</span></div>
<div class="sx-hero"><div class="sx-copy"><small>Curitiba e região</small><strong>Serviço de confiança para a sua empresa</strong><span class="sx-p">Atendimento rápido, orçamento sem compromisso e equipe especializada.</span><span class="sx-row"><span class="sx-btn">Pedir orçamento</span><span class="sx-ghost">Ver serviços</span></span></div><div class="sx-art"><i></i><i></i><i></i></div></div>
<div class="sx-cards"><span><i></i><b>Serviço A</b><u></u><u></u></span><span><i></i><b>Serviço B</b><u></u><u></u></span><span><i></i><b>Serviço C</b><u></u><u></u></span></div>
<div class="sx-proof"><span>&#9733;&#9733;&#9733;&#9733;&#9733; Avaliada pelos clientes</span><span>Atendimento no WhatsApp</span><span>Orçamento sem compromisso</span></div>
</div></div><div class="dv-base"></div></div>
<div class="dv-phone"><div class="dv-notch"></div><div class="sm">
<div class="sm-nav"><span class="sx-logo"><i></i>Sua Empresa</span><span class="sm-burger"><u></u><u></u><u></u></span></div>
<div class="sm-hero"><small>Curitiba e região</small><strong>Serviço de confiança para a sua empresa</strong><span class="sx-btn">Pedir orçamento</span></div>
<div class="sm-card"><i></i><b>Serviço A</b><u></u></div><div class="sm-card"><i></i><b>Serviço B</b><u></u></div><div class="sm-card"><i></i><b>Serviço C</b><u></u></div>
<span class="sm-wa">WhatsApp</span></div></div></div>"""
    return '<figure class="fig f-devices wide" role="img" aria-label="Ilustração de um site institucional aberto em um notebook, com menu, destaque, serviços e avaliações, e a mesma página adaptada ao celular, com botão de WhatsApp.">%s%s</figure>' % (inner, _cap("o mesmo site no computador e no celular, com uma página clara para cada serviço."))


def metricas():
    kpis = [("Visualizações no Maps", "820"), ("Visualizações na Busca", "1.240"), ("Ligações", "46"),
            ("Pedidos de rota", "58"), ("Cliques no WhatsApp", "73"), ("Cliques no site", "91")]
    cards = "".join('<div class="mt-k"><small>%s</small><b>%s</b></div>' % (k, v) for k, v in kpis)
    heights = [34, 42, 38, 55, 48, 62, 58, 70, 66, 78, 74, 88]
    bars = "".join('<i style="--h:%d%%"></i>' % h for h in heights)
    inner = """<div class="mt-head"><b>Desempenho do perfil</b><span>Últimos 30 dias</span></div>
<div class="mt-grid">%s</div>
<div class="mt-chart"><small>Pessoas que viram o perfil, por semana</small><div class="mt-bars">%s</div></div>""" % (cards, bars)
    return '<figure class="fig f-metricas wide" role="img" aria-label="Ilustração do painel de desempenho de um Perfil da Empresa no Google, com visualizações no Maps e na Busca, ligações, pedidos de rota e cliques no WhatsApp e no site, com números de exemplo.">%s%s</figure>' % (inner, _cap("os números do perfil, com valores de exemplo só para mostrar o formato."))


def ia_resposta():
    inner = """<div class="ai-top"><span class="ai-dot"></span><b>Assistente de IA</b></div>
<p class="ai-q">Qual a melhor empresa de serviços em Curitiba para me atender?</p>
<div class="ai-a"><p>Uma boa opção é a <b>Sua Empresa</b>, em Curitiba. Ela tem perfil completo no Google, avaliações recentes de clientes e um site que explica cada serviço, com perguntas e respostas claras.</p>
<ul class="ai-src"><li>Perfil da Empresa no Google</li><li>Site da empresa</li><li>Avaliações de clientes</li></ul></div>"""
    return '<figure class="fig f-ai" role="img" aria-label="Ilustração de uma resposta de assistente de inteligência artificial que recomenda uma empresa organizada, citando o perfil no Google, o site e as avaliações de clientes.">%s%s</figure>' % (inner, _cap("uma resposta de IA citando uma empresa bem organizada. Nenhuma ferramenta garante a recomendação."))

FIGS = {
    "google-meu-negocio": perfil, "criacao-de-sites": lambda: devices(),
    "gestao-de-redes-sociais": redes, "trafego-pago": trafego, "crm-de-vendas": crm,
    "automacao-ia-atendimento": ia, "metodo-par-360": par_loop,
}

def fig(slug):
    f = FIGS.get(slug)
    return f() if f else ""


# ---------------------------------------------------------------------------
# Página de CRM: fluxo de automação, caixa de entrada e app no celular
# ---------------------------------------------------------------------------
def _node(x, y, w, h, title, sub="", kind="", lines=None):
    t_lines = lines or [title]
    ty = y + (22 if sub or len(t_lines) > 1 else h / 2 + 5)
    tspans = "".join('<tspan x="%d" dy="%d">%s</tspan>' % (x + 16, 0 if i == 0 else 17, tl) for i, tl in enumerate(t_lines))
    out = '<rect class="wf-n %s" x="%d" y="%d" width="%d" height="%d" rx="14"/>' % (kind, x, y, w, h)
    out += '<text class="wf-t" x="%d" y="%d">%s</text>' % (x + 16, ty, tspans)
    if sub:
        sy = ty + 17 * (len(t_lines) - 1) + 19
        out += '<text class="wf-s" x="%d" y="%d">%s</text>' % (x + 16, sy, sub)
    return out


def _pill(x, y, label, color):
    w = 14 + len(label) * 7
    return '<rect x="%d" y="%d" width="%d" height="20" rx="10" fill="#0a101a" stroke="%s"/><text class="wf-p" x="%d" y="%d" fill="%s" text-anchor="middle">%s</text>' % (
        x - w / 2, y - 10, w, color, x, y + 4, color, label)


def wf_svg():
    parts = []
    line = lambda d: '<path class="wf-l" d="%s"/>' % d
    parts.append(line("M400 74 V120"))
    parts.append(line("M400 184 V212 H120 V250"))
    parts.append(line("M400 184 V212 H495 V250"))
    for a, b in [(314, 340), (404, 430), (494, 520)]:
        parts.append(line("M120 %d V%d" % (a, b)))
    parts.append(line("M495 314 V342 H335 V370"))
    parts.append(line("M495 342 V370"))
    parts.append(line("M495 342 H655 V370"))
    for x in (335, 495, 655):
        parts.append(line("M%d 454 V480" % x))
    parts.append(_node(280, 10, 240, 64, "Pedido de atendimento", "Gatilho: tag de handoff da IA", "trig"))
    parts.append(_node(250, 120, 300, 64, "Empreendimento exclusivo?", "Imóvel com corretor dedicado", "dec"))
    parts.append(_node(5, 250, 230, 64, "Atribuir ao corretor", "Responsável pelo imóvel"))
    parts.append(_node(5, 340, 230, 64, "Avisar corretor e gestora", "Aviso na hora, no celular"))
    parts.append(_node(5, 430, 230, 64, "Mover para Em qualificação", "Cartão no funil"))
    parts.append(_node(5, 520, 230, 44, "Fim do fluxo", "", "end"))
    parts.append(_node(375, 250, 240, 64, "Regra de qualificação", "Conforme o que o contato disse", "dec"))
    parts.append(_node(260, 370, 150, 84, "", "", "ok", lines=["Intenção forte", "de compra"]))
    parts.append(_node(420, 370, 150, 84, "", "", "ok", lines=["Informou a faixa", "de investimento"]))
    parts.append(_node(580, 370, 150, 84, "", "", "", lines=["Sem perfil", "definido ainda"]))
    parts.append(_node(260, 480, 150, 50, "Qualificado", "", "ok"))
    parts.append(_node(420, 480, 150, 50, "Qualificado", "", "ok"))
    parts.append(_node(580, 480, 150, 64, "Em qualificação", "Avisa a equipe", ""))
    parts.append(_pill(260, 212, "Sim", "#6da3ff"))
    parts.append(_pill(447, 212, "Não", "#c486ff"))
    return '<svg class="wf" viewBox="0 0 740 580" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">%s</svg>' % "".join(parts)


def crm_flow():
    return ('<figure class="fig wide" role="img" aria-label="Exemplo de fluxo de automação do CRM: quando a IA pede ajuda humana, o CRM verifica se o contato é de um empreendimento exclusivo, atribui ao corretor, avisa a equipe, qualifica o contato conforme o que ele disse e move o cartão no funil.">'
            '<div class="wf-scroll">%s</div>%s</figure>') % (wf_svg(), _cap("um fluxo real de qualificação e passagem para o corretor, montado no CRM (exemplo para imobiliárias)."))


def crm_inbox():
    rows = [
        ("c-wa", "Cliente A", "Quanto custa a instalação?", "Novo"),
        ("c-ig", "Cliente B", "Vi o anúncio no Instagram.", "Em conversa"),
        ("c-fb", "Cliente C", "Podem passar o orçamento?", "Proposta"),
        ("c-wa", "Cliente D", "Confirmado para quinta, 14h.", "Visita"),
    ]
    items = "".join(
        '<div class="ib-row%s"><span class="ch %s"></span><div><b>%s</b><small>%s</small></div><span class="st">%s</span></div>' % (
            " sel" if i == 0 else "", c, n, m, s) for i, (c, n, m, s) in enumerate(rows))
    inner = '<div class="ib-head"><b>Conversas</b><span class="chips"><i class="c-wa"></i><i class="c-ig"></i><i class="c-fb"></i><i class="c-em"></i></span></div>%s' % items
    return _wrap("f-inbox", "Ilustração da caixa de entrada do CRM com conversas de WhatsApp, Instagram e Facebook em uma só lista, cada uma com a etapa do funil.", inner, "WhatsApp, Instagram e Facebook em uma lista só.")


def crm_mobile():
    inner = """<div class="mob" aria-hidden="true"><div class="mob-top"></div>
<div class="note-m"><span class="ic"></span><div><b>Novo contato</b><small>Pediu orçamento pelo WhatsApp</small></div></div>
<div class="note-m"><span class="ic p"></span><div><b>Lembrete</b><small>Visita agendada para amanhã</small></div></div>
<div class="note-m"><span class="ic w"></span><div><b>Follow-up</b><small>Proposta enviada há 2 dias sem resposta</small></div></div></div>"""
    return _wrap("f-mobile", "Ilustração de um celular com avisos do CRM: novo contato, lembrete de visita e follow-up de proposta sem resposta.", inner, "avisos para a equipe agir na hora certa.")


CAPS = [
    ("Funil visual", "Cada contato em uma etapa, do primeiro contato ao fechamento."),
    ("Caixa de entrada única", "Conversas de WhatsApp, Instagram e Facebook no mesmo lugar."),
    ("Automações", "Resposta, follow-up e avisos disparados no momento certo."),
    ("Agentes de IA", "Atendimento, qualificação e agendamento antes de chamar a equipe."),
    ("Agenda e lembretes", "Visitas e reuniões marcadas, com aviso para o cliente e para a equipe."),
    ("Formulários e páginas", "Captação com formulários e páginas ligados direto ao funil."),
    ("Painel de números", "Origem dos contatos, propostas e fechamentos em um painel."),
    ("Integrações", "Anúncios do Google e da Meta, formulários e outras ferramentas."),
]


def crm_caps():
    return '<ul class="caps">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (t, d) for t, d in CAPS)


AUTOS = [
    ("Resposta imediata", "O contato novo entra no funil e recebe a primeira mensagem em segundos."),
    ("Follow-up com prazo", "Mensagens e tarefas nos dias certos, até o contato decidir."),
    ("Lembrete de visita ou reunião", "Cliente e equipe recebem o aviso antes do horário marcado."),
    ("Reativação", "Quem esfriou volta a ser lembrado, com uma mensagem no momento certo."),
    ("Aviso à equipe", "Quando o contato precisa de uma pessoa, o responsável é avisado na hora."),
]


def crm_autos():
    return '<ul class="autos">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (t, d) for t, d in AUTOS)


def crm_feedback():
    inner = """<div class="loop">
<div class="node n1"><b>Anúncio no Google ou na Meta</b><small>Campanha, criativo e público</small></div>
<span class="conn" aria-hidden="true"></span>
<div class="node n2"><b>Contato entra no CRM</b><small>Com a origem registrada</small></div>
<span class="conn" aria-hidden="true"></span>
<div class="node n3"><b>Venda registrada</b><small>Valor e etapa no funil</small></div>
<span class="conn" aria-hidden="true"></span>
<div class="node n4"><b>Dado volta para a plataforma</b><small>Google Ads e Meta Ads aprendem quem compra</small></div>
<div class="back" aria-hidden="true"><span>A campanha seguinte aprende com as vendas</span></div></div>"""
    return _wrap("f-loop wide", "Ilustração do ciclo do CRM com os anúncios: o anúncio gera um contato com origem registrada, o contato vira venda e a venda volta para o Google Ads e o Meta Ads, que passam a buscar quem compra.", inner, "da campanha à venda, e da venda de volta para a campanha.")


VENDEDORES = [
    ("Tarefas do dia", "Cada vendedor abre o CRM e vê quem precisa de retorno hoje."),
    ("Distribuição dos contatos", "Os contatos novos são divididos entre a equipe por regra, sem disputa e sem fila parada."),
    ("Retornos cobrados", "Contato sem resposta vira aviso para o vendedor e para o gestor."),
    ("Painel de cada vendedor", "Conversas, propostas e fechamentos por pessoa, para o gestor orientar com dados."),
]


def crm_vendedores():
    return '<ul class="autos">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (t, d) for t, d in VENDEDORES)


IA_CRM = [
    ("Atende na hora", "Responde o contato novo em segundos, inclusive fora do horário comercial."),
    ("Qualifica", "Faz as perguntas certas para entender o que a pessoa precisa e se faz sentido para a empresa."),
    ("Agenda", "Marca visita, reunião ou retorno direto na agenda da equipe."),
    ("Passa para a pessoa certa", "Quando precisa de um humano, entrega a conversa com o histórico e avisa o responsável."),
]


def crm_ia():
    return '<ul class="autos">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (t, d) for t, d in IA_CRM)
