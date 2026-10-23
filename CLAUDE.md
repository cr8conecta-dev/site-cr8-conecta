# Site CR8 Conecta (cr8conecta.com.br)

Site estático da CR8 Conecta, agência de marketing e vendas de Curitiba que trabalha com o Método PAR 360 (Posicionamento, Atração, Retenção). Dono: Carlos da Silva. Responda sempre em português, de forma curta.

## Como o deploy funciona

- Este repositório É o site. Todo `git push` na branch `main` dispara o GitHub Actions (`.github/workflows/deploy.yml`), que roda `python3 _fonte/gerar.py` e envia por FTPS para a Hostinger em cerca de 1 minuto. Não precisa mais de zip.
- A conta FTP `u118620461.deploy` começa uma pasta abaixo do docroot, por isso o workflow usa `server-dir: ../`. Não mudar sem testar.
- O envio nunca apaga nada (`dangerous-clean-slate: false`; estado em `.ftp-deploy-cr8-site-novo.json`) e não envia `_fonte/`, `.md`, `.htaccess`, `.git*`, `referencias/`. As outras ferramentas em `public_html` ficam intactas.
- Por isso: **só faça push depois de gerar e conferir**. Antes de qualquer push, mostre ao Carlos o que mudou e peça um "pode publicar".
- Teste sem enviar: Actions > Publicar > Run workflow (dry_run = true).

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
- NUNCA usar laranja nem violeta/roxo no site (pedido do Carlos). Destaques e brilhos só em tons de azul.
- Títulos (h1/h2): a parte final sai em gradiente azul (classe `.grad`, aplicada sozinha por `destaque()` em `_fonte/build.py`; pedido do Carlos). Botões principais da capa também em gradiente azul.
- Cookies (LGPD): o Google Tag Manager só carrega depois do "Aceitar" no aviso de cookies (`cr8LoadGTM` no head, escolha em localStorage `cr8-cookies`; link "Cookies" no rodapé reabre o aviso). Não recolocar o GTM direto no head nem o noscript do GTM.
- Paleta oficial: marinho #0d2743, azul acinzentado #8c9eac, nude #dad5cf, branco #ffffff. Seções alternam escuras e claras.
- Visual sóbrio: o Carlos não quer cara de site feito por IA. Evitar brilhos, formas flutuando, efeitos de aparecer ao rolar em todo bloco, cartões de vidro com sombra, gradientes decorativos. Preferir fotos reais e listas limpas.
- Regras de design (espaçamento, tipografia, contraste, botões, metas de altura das páginas, checklist): ver `GUIA-VISUAL.md`. Prints de referência ficam em `referencias/`, que não vai para o GitHub nem para o site.
- WhatsApp e telefone: (41) 99525-7590 (wa.me/5541995257590). Google Tag Manager: GTM-W52QP5QB.

## Estado da publicação (atualizado em 19/10/2026)

- O site novo está NO AR em cr8conecta.com.br, publicado pelo deploy automático (ver acima).
- `public_html` também guarda outras ferramentas no ar (crm, link, marketing, geradordevendas, cardenuto, diagnosticoimobiliarias, propostapersonalizada, southwindprovisorio, vendor). Nunca esvaziar essa pasta. O WordPress em `southwindprovisorio` já respondia 404 na raiz, não é causado pelo deploy.
- No servidor há só um `.htaccess` MÍNIMO com o redirecionamento 301 de www para sem www; o `.htaccess` completo do repositório NÃO é enviado (afetaria as outras ferramentas).
- Sobra uma pasta antiga `public_html/public_html/` (cópia criada por testes do deploy) que está acessível em /public_html/; deve ser apagada pelo Carlos no Gerenciador de Arquivos.
- Backups da home antiga: pasta e zip `Documentos\backup-cr8conecta-ao-vivo-2026-10-15`, branch `backup-site-antigo-2026-10-15`, tag `backup-antes-ux-2026-10-15`, backups diários da Hostinger.
- Cuidado: o repositório privado `cr8-site` publicava o site antigo por FTP. Se ele rodar de novo, pode reenviar a home antiga por cima; desativar o workflow dele.

## Buscadores (atualizado em 21/10/2026)

- Google Search Console: propriedade `https://cr8conecta.com.br/` verificada por arquivo HTML (`google34f91344faf878f5.html` na raiz; NÃO apagar). Sitemap enviado e processado (10 páginas). Indexação pedida para a home e as páginas de serviço.
- Bing Webmaster Tools: site cadastrado, sitemap com sucesso. IndexNow ligado: arquivo-chave `6c58b88af9a41c8b16223861420d7101.txt` na raiz (NÃO apagar) e passo no deploy que avisa o Bing a cada publicação.
- Bing Places: listagem da CR8 importada do Google, verificada, publicação em andamento (7 a 12 dias). O site no Perfil do Google deve ser `https://cr8conecta.com.br/` (sem www, com https); o Bing copia do Google.

## Pendências conhecidas

- Visual novo JÁ NO AR desde 19/10/2026, mas sem a aprovação do Carlos ainda: capa clara (nude/branco) em todas as páginas e resto do site em azul com gradiente e brilho suave (a pedido; foge da regra "sem brilhos, gradientes decorativos" e de "seções alternam escuras e claras"), fundo escuro mais fundo (#0a1c2e), texto corrido em Archivo (sem serifa), títulos mais leves, capas claras em Sobre e Contato, home sem o cartão escuro dos pilares. Ilustrações das páginas agora são painéis escuros estilo dashboard (bloco "PAINÉIS ESTILO DASHBOARD" no fim do CSS; apagar o bloco volta ao painel claro). Botão flutuante de WhatsApp em todas as páginas. O bloco "CAPA CLARA em todas as páginas" no fim de `assets/css/style.css` define a capa clara e o azul com brilho; apagar esse bloco volta ao azul liso.

- Melhoria de UX (no ar): home reordenada, CSS sem brilho/degradê, cores de contraste corrigidas, página do CRM enxuta (conferidas). Páginas de serviço (Perfil no Google, Criação de Sites, Redes Sociais, Tráfego, Automação): ilustrações escondidas no celular e faixa de convite no meio, geradas mas NÃO conferidas no celular, no desktop nem no contraste. Conferir tudo antes de qualquer "pode publicar".
- Propostas para o CRM ainda sem decisão: compactar listas, tirar a seção "Uma plataforma no lugar de várias ferramentas", links compactos em "Continue explorando".
- Figma da home (conta da Amanda, ainda sem acesso da CR8): https://www.figma.com/design/5lhZ3wX844SzClvDX9jf0G. O Figma não atualiza o site sozinho.

- Página de política de privacidade (necessária para anúncios e formulário).
- Blog em `/blog/` NO AR com 3 artigos (lista `POSTS` em `_fonte/data.py`; para criar artigo, acrescentar um item lá). Regras: sem preços, sem números inventados, sem travessão, sem citar GHL. Próximos temas sugeridos: redes sociais para empresas de serviço, IA no atendimento por WhatsApp, o que é o Método PAR 360.
- Depois de publicar: enviar `https://cr8conecta.com.br/sitemap.xml` no Google Search Console e criar os acionadores no GTM para os eventos `cta_click`, `generate_lead` e `video_play`.
