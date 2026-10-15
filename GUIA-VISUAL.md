# Guia visual do site CR8 Conecta

Regras de design para qualquer mudança no site. Complementa o CLAUDE.md (marca, conteúdo, deploy). Quando houver conflito, vale o CLAUDE.md.

Origem: pesquisa em sites de referência (outubro de 2026) mais os números reais do `assets/css/style.css`. Os valores marcados "de referência" foram lidos no navegador e podem vir de elementos secundários da página: servem de ordem de grandeza, não de regra exata.

## 1. Princípios (valem para toda página)

1. **Uma ação principal por tela.** Um botão primário, sempre da mesma cor. O secundário é só contorno. (Animalz usa um único botão colorido no site todo.)
2. **Abertura em 3 coisas:** promessa clara, um botão e prova. A prova pode ser uma linha de resultado real ou logos de clientes autorizados. (Conversion mostra a faixa de clientes já na primeira tela.)
3. **Hierarquia por tipografia e espaço, não por efeito.** Título grande, texto de apoio menor, bastante ar. (Pentagram: fundo liso, quase nenhuma decoração.)
4. **Prova cedo.** Resultados e depoimentos antes de explicar o método. Pessoas reais convencem mais que números sozinhos.
5. **Texto curto.** No celular, o texto de apoio da abertura tem no máximo 2 frases. Parágrafos de até 4 linhas.
6. **Fotos reais do time e dos clientes** no lugar de ilustração genérica.
7. **Nada que pareça feito por IA:** sem brilho, sem degradê decorativo, sem formas flutuando, sem cartão de vidro com sombra, sem efeito de aparecer em todo bloco (ver CLAUDE.md).

## 2. Números atuais do site (do CSS)

| Elemento | Hoje |
|---|---|
| Fontes | Archivo (títulos e interface), Newsreader (texto corrido) |
| H1 | 800, `clamp(2.45rem, 6vw, 4.7rem)`, altura de linha 1.02, espaçamento -0.028em |
| H2 | 700, `clamp(1.7rem, 3vw, 2.5rem)`, altura de linha 1.1 |
| H3 | 650, 1.25rem |
| Texto de apoio (`.lead`) | `clamp(1.2rem, 1.9vw, 1.42rem)`, altura de linha 1.55, largura máx. 36em |
| Corpo | 1.1875rem (19px) no desktop, altura de linha 1.65 |
| Largura do conteúdo | 1200px |
| Espaço vertical das seções | `clamp(3.5rem, 8vw, 6.5rem)` |
| Botão | arredondado, preenchimento `1rem 1.55rem`, peso 650 |

## 3. Regras para novas mudanças

**Espaçamento.** Use múltiplos de 8px: 8, 16, 24, 32, 48, 64, 96. Evite valores soltos. Entre título e conteúdo da mesma seção, nunca menos que 24px (já houve título colado nos vídeos).

**Tipografia.**
- No máximo 2 famílias (as duas acima).
- No máximo 4 tamanhos de título por página (H1, H2, H3 e rótulo).
- Largura de leitura: 60 a 75 caracteres por linha (em torno de 38em).
- Teste futuro, sem decisão: sites como McKinsey (títulos peso 300, 44/52) e Stripe (peso 300 com espaçamento de letras levemente negativo) usam títulos leves, o que dá ar mais sóbrio. Só testar se o Carlos pedir.

**Cor e contraste.**
- Paleta fixa do CLAUDE.md: marinho, azul acinzentado, nude, branco.
- Texto normal com contraste mínimo de 4,5:1; texto grande, 3:1.
- Nunca fixar cor clara em componente que pode cair em seção clara. Usar `var(--text)`, `var(--muted)` e `var(--head)`, que mudam com a seção. (Foi a causa dos rótulos do formulário e do aviso do Perfil no Google.)
- Seções alternam escura e clara. Evitar duas seções seguidas do mesmo tom.

**Botões.**
- Altura mínima de 44px, área de toque confortável no celular.
- Um primário por seção. Textos de ação: "Pedir diagnóstico gratuito", sem variar o nome a cada página.
- Sem degradê, sem brilho, sem movimento ao passar o mouse (só mudança de cor).

**Imagens.**
- Fotos do time em 600x600, em círculo ou quadrado, sempre do mesmo estilo.
- Logos de clientes só com autorização.

## 4. Padrão de página

**Home.** Abertura (promessa, 1 botão, 2 frases) > resultados > depoimentos > método > para quem é > quem está por trás > perguntas frequentes > convite final.
Meta no celular: até 12 telas (cerca de 10.000px). Hoje: 10.205px.

**Páginas de serviço.** Abertura > o que resolve > como funciona > convite no meio da página > perguntas > convite final.
Meta no celular: até 10 telas (cerca de 8.000px). Hoje: CRM 17.142px, Perfil no Google 10.676px, Criação de Sites 9.318px, Tráfego 8.346px, Automação 7.309px, Redes Sociais 6.569px.

**Cabeçalho.** No celular, o botão de diagnóstico deve estar visível sem abrir o menu. Sem barra fixa na tela sem aprovação do Carlos.

## 5. Checklist antes de mostrar ao Carlos

- [ ] Celular (375px) e desktop (1280px) conferidos, sem rolagem lateral.
- [ ] Nenhum texto com contraste abaixo de 3:1 (rodar a checagem em todas as páginas).
- [ ] Um só botão primário por seção, sempre com a mesma cor.
- [ ] Nada de brilho, degradê decorativo ou sombra pesada.
- [ ] Título nunca colado no conteúdo (mínimo 24px).
- [ ] Texto novo sem travessão e sem número sem fonte.
- [ ] Altura do celular dentro da meta da seção 4.

## 6. Referências e o que copiar

| Site | O que copiar |
|---|---|
| Pentagram (pentagram.com) | Fundo liso, hierarquia só com tipografia e espaço |
| Animalz (animalz.co) | Um botão colorido só, serifa nos títulos, fundo claro e calmo |
| Conversion (conversion.com.br) | Promessa, botão e faixa de clientes logo na primeira tela. Não copiar o fundo escuro com brilho |
| McKinsey (mckinsey.com) | Títulos leves e grandes, muito espaço, tom de seriedade |
| Stripe (stripe.com/br) | Escala de texto limpa, poucas cores, muito ar |
| RD Station (rdstation.com) | Seções com espaço vertical de 56 a 64px, coluna de texto estreita (cerca de 760px) |

Quando o Carlos mandar novas referências (pasta `referencias/`), registrar aqui o que elas têm em comum e o que foi adotado.
