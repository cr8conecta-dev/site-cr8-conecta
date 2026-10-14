# Primeira publicação: GitHub + Hostinger com deploy automático

Abra esta pasta no Claude Code e cole a mensagem abaixo.

---

Leia o CLAUDE.md e o COMECE-AQUI.md desta pasta. Quero publicar este site em cr8conecta.com.br com deploy automático: GitHub + Hostinger. Me guie uma ação por vez, esperando minha resposta antes da próxima. Toda ação que eu tiver que fazer deve começar com "👉 FAÇA:" em negrito, e textos para copiar devem vir em caixa de código. Faça você mesmo tudo o que der para fazer pelo terminal.

Roteiro:

1. Confira se `git` e o GitHub CLI (`gh`) estão instalados e se o `gh` está logado (`gh auth status`). Se faltar algo, me ajude a instalar e a fazer o login (`gh auth login`).
2. Rode `python3 _fonte/gerar.py` e confirme que nada mudou em relação ao último commit (`git status`).
3. Crie o repositório público `site-cr8-conecta` na minha conta e envie a branch `main`:
   `gh repo create site-cr8-conecta --public --source=. --remote=origin --push`
4. Antes de mexer na Hostinger, me peça para fazer backup do site que está no ar hoje: hPanel > Sites > cr8conecta.com.br > Arquivos > Backups (ou baixar a pasta `public_html` pelo Gerenciador de Arquivos).
5. Me guie para esvaziar a pasta `public_html` do domínio (a Hostinger exige a pasta vazia para conectar o Git). Confirme comigo antes, porque isso tira o site atual do ar até o passo 6 terminar.
6. Me guie no hPanel: Sites > cr8conecta.com.br > Avançado > GIT. Em "Criar um novo repositório":
   - Repositório: `https://github.com/MEU_USUARIO/site-cr8-conecta.git` (descubra o usuário com `gh api user -q .login`)
   - Branch: `main`
   - Diretório: deixar em branco (instala direto em public_html)
   Depois clicar em Criar e em Implantar.
7. Ainda nessa tela, me peça para clicar em "Implantação automática" e copiar a URL do webhook. Com a URL, crie o webhook no GitHub:
   `gh api repos/MEU_USUARIO/site-cr8-conecta/hooks -f name=web -F active=true -f events[]=push -f config[url]=URL_DO_WEBHOOK -f config[content_type]=json`
8. Teste: faça uma alteração mínima (por exemplo a data no rodapé), gere, faça commit e push, e confira em https://cr8conecta.com.br se atualizou.
9. Confira no ar: https e sem www funcionando, página 404, /landing-pages/ indo para /criacao-de-sites/, mapa na página Contato, vídeos dos depoimentos, e que https://cr8conecta.com.br/_fonte/data.py e /CLAUDE.md dão erro 403.
10. Por último, me lembre de enviar o sitemap no Google Search Console: `https://cr8conecta.com.br/sitemap.xml`.

---

Depois da primeira publicação, para qualquer alteração basta pedir ao Claude Code nesta pasta (por exemplo: "troque o texto da seção X" ou "adicione o segmento Y"). Ele altera, gera, mostra para você e só publica quando você disser "pode publicar".
