# Site CR8 Conecta (cr8conecta.com.br)

Site estático da CR8 Conecta, agência de marketing e vendas de Curitiba que trabalha com o Método PAR 360 (Posicionamento, Atração, Retenção). Dono: Carlos da Silva. Responda sempre em português, de forma curta.

## Como o deploy funciona

- Este repositório É o site: a raiz do repositório vai inteira para a pasta `public_html` da Hostinger.
- A Hostinger está ligada ao GitHub com implantação automática: todo `git push` na branch `main` atualiza o site no ar em poucos segundos.
- Por isso: **só faça push depois de gerar e conferir**. Antes de qualquer push, mostre ao Carlos o que mudou e peça um "pode publicar".
- Arquivos internos (`_fonte/`, arquivos `.md`, `.git`) ficam bloqueados para o público pelo `.htaccess`.

## Estrutura

```
index.html, sobre/, contato/, metodo-par-360/   páginas geradas (não editar à mão)
google-meu-negocio/, criacao-de-sites/, gestao-de-redes-sociais/,
trafego-pago/, crm-de-vendas/, automacao-ia-atendimento/
404.html, sitemap.xml, robots.txt, llms.txt     também gerados
assets/css/style.css   visual do site (editado direto, não é gerado)
assets/js/site.js      menu, formulário para WhatsApp, eventos do GTM, animação da home
assets/team/           fotos do time (600x600, jpg)
assets/logos/, assets/img/, assets/fonts/
.htaccess              https, sem www, 404, redirecionamento /landing-pages/ -> /criacao-de-sites/
_fonte/data.py         TODO o texto: soluções, perguntas frequentes, time, depoimentos, segmentos
_fonte/build.py        estrutura das páginas, SEO, dados estruturados (JSON-LD), sitemap
_fonte/art.py          ilustrações e mockups feitos em HTML/CSS
_fonte/gerar.py        gera tudo: python3 _fonte/gerar.py
```

## Fluxo para qualquer alteração

1. Texto ou estrutura: edite `_fonte/data.py` ou `_fonte/build.py`. Visual: edite `assets/css/style.css`.
2. Rode `python3 _fonte/gerar.py` (só precisa de Python 3, sem bibliotecas extras).
3. Confira localmente: `python3 -m http.server 8000` e abra http://localhost:8000. Confira celular (390 px) e computador; nada pode passar da largura da tela.
4. Mostre o resultado ao Carlos. Com o "pode publicar": `git add -A && git commit -m "descrição curta" && git push`.

## Regras de conteúdo (decididas pelo Carlos)

- Use "Perfil da Empresa no Google" como nome principal; "Google Meu Negócio" só como nome antigo/sinônimo.
- O CRM se chama publicamente "CRM CR8 Conecta". Nunca citar a plataforma por trás dele (GoHighLevel/GHL). Não mostrar preços do CRM nem de nenhum serviço.
- Nas páginas de Perfil da Empresa no Google e de Criação de Sites, deixar claro que a CR8 trabalha para o site e a empresa aparecerem também nas respostas de inteligência artificial, de forma orgânica.
- Não usar travessão (—) nos textos.
- Não inventar números, depoimentos ou clientes. Só dados com fonte verificável; se não tiver fonte, não usar.
- Paleta oficial: marinho #0d2743, azul acinzentado #8c9eac, nude #dad5cf, branco #ffffff. Seções alternam escuras e claras.
- Visual sóbrio: o Carlos não quer cara de site feito por IA. Evitar brilhos, formas flutuando, efeitos de aparecer ao rolar em todo bloco, cartões de vidro com sombra, gradientes decorativos. Preferir fotos reais e listas limpas.
- Regras de design (espaçamento, tipografia, contraste, botões, metas de altura das páginas, checklist): ver `GUIA-VISUAL.md`. Prints de referência ficam em `referencias/`, que não vai para o GitHub nem para o site.
- WhatsApp e telefone: (41) 99525-7590 (wa.me/5541995257590). Google Tag Manager: GTM-W52QP5QB.

## Estado da publicação (atualizado em 15/10/2026)

- O site novo está NO AR em cr8conecta.com.br. Foi enviado por zip pelo Gerenciador de Arquivos da Hostinger (extraído em `public_html`, sem apagar nada). A Hostinger NÃO está ligada a este repositório: `git push` atualiza só o GitHub, não o domínio.
- `public_html` também guarda outras ferramentas no ar (crm, link, marketing, geradordevendas, cardenuto, diagnosticoimobiliarias, propostapersonalizada, southwindprovisorio, vendor). Nunca esvaziar essa pasta.
- No servidor há só um `.htaccess` MÍNIMO (enviado em 19/10/2026) com o redirecionamento 301 de www para sem www; o `.htaccess` completo do repositório NÃO foi enviado (afetaria as outras ferramentas). Para desfazer o redirecionamento, renomear/remover esse arquivo no Gerenciador de Arquivos. Para atualizar o site: gerar o zip sem `_fonte/`, `.md`, `.htaccess`, `.gitignore`, enviar e extrair por cima com "overwrite".
- Backups da home antiga: pasta e zip `Documentos\backup-cr8conecta-ao-vivo-2026-10-15`, branch `backup-site-antigo-2026-10-15` no GitHub, tag `backup-antes-ux-2026-10-15`, e backups diários de arquivos da Hostinger.
- Cuidado: o repositório privado `cr8-site` publicava o site antigo por FTP (existe `.ftp-deploy-sync-state.json` no servidor). Se ele rodar de novo, pode reenviar a home antiga por cima.

## Pendências conhecidas

- Mudanças visuais só no site local, NÃO publicadas (aprovação do Carlos pendente): capa clara (nude/branco) em todas as páginas e resto do site em azul com gradiente e brilho suave (a pedido; foge da regra "sem brilhos, gradientes decorativos" e de "seções alternam escuras e claras"), fundo escuro mais fundo (#0a1c2e), texto corrido em Archivo (sem serifa), títulos mais leves, capas claras em Sobre e Contato, home sem o cartão escuro dos pilares. Ilustrações e cartões das capas também ficaram claros. O bloco "CAPA CLARA em todas as páginas" no fim de `assets/css/style.css` define a capa clara e o azul com brilho; apagar esse bloco volta ao azul liso.

- Melhoria de UX em andamento (tudo local, NADA publicado): home reordenada, CSS sem brilho/degradê, cores de contraste corrigidas, página do CRM enxuta (conferidas). Páginas de serviço (Perfil no Google, Criação de Sites, Redes Sociais, Tráfego, Automação): ilustrações escondidas no celular e faixa de convite no meio, geradas mas NÃO conferidas no celular, no desktop nem no contraste. Conferir tudo antes de qualquer "pode publicar".
- Propostas para o CRM ainda sem decisão: compactar listas, tirar a seção "Uma plataforma no lugar de várias ferramentas", links compactos em "Continue explorando".
- Figma da home (conta da Amanda, ainda sem acesso da CR8): https://www.figma.com/design/5lhZ3wX844SzClvDX9jf0G. O Figma não atualiza o site sozinho.

- Página de política de privacidade (necessária para anúncios e formulário).
- Blog em `/blog/` (estrutura preparada, ainda sem conteúdo).
- Depois de publicar: enviar `https://cr8conecta.com.br/sitemap.xml` no Google Search Console e criar os acionadores no GTM para os eventos `cta_click`, `generate_lead` e `video_play`.
