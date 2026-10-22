# Site da Moza · mozabr.com.br

Site institucional da Moza Assessoria. Uma página só, com âncoras. O objetivo
é único: gerar conversa no WhatsApp.

## Fonte de verdade

Este projeto não decide marca nem copy. Ele executa o que já está decidido.

**Atalho:** `DESIGN.md` na raiz junta cor, tipografia, componente, espaço,
profundidade e limites num arquivo só, para agente ler de primeira. Ele é
**derivado** do brandbook, não substitui. Mudou a marca? Muda no brandbook e
depois atualiza o DESIGN.md.

- Tokens (cor, tipografia, espaçamento): seção 06 de
  `../next-cerebro/marca/rebranding/fontes/brandbook-moza.md`
- Estrutura e argumento: `../next-cerebro/marca/rebranding/fontes/arquitetura-site.md`
- Copy oficial: `../next-cerebro/marca/rebranding/fontes/kit-comunicacao.md`
- Copy do Marketing 360: `../next-cerebro/marca/rebranding/fontes/copy-360-site.md`
  (escrito pelo Murillo em 10/09/2026, com as regras de onde entra e o que não
  pode). Escopo que sustenta: `../next-cerebro/marca/produto-360.md`
- Tom de voz: `../next-cerebro/marca/rebranding/fontes/tom-de-voz.md`
- O desenho fechado seção a seção: `kit-de-secoes.html` (abrir no navegador)

Mudou alguma coisa de marca? Muda lá primeiro, depois aqui. Nunca o contrário.

## Regras invioláveis do conteúdo

- Nunca travessão. Vírgula, dois-pontos, parênteses ou ponto.
- Nenhuma exclamação no site.
- Caixa alta só em etiqueta e sigla, nunca para dar ênfase.
- Zero preço, zero prazo, zero comparativo de plano.
- Nunca "nosso time", "nossa equipe" nem plural de fachada. É "a Moza", "nós",
  ou o nome do sócio.
- Palavras banidas: garantido, explosivo, revolucionário, fórmula, segredo,
  alavancar, acelerar, turbinar, pisar fundo, o melhor do mercado.
- As etapas são Centro (Diagnóstico) e Raio 1 a 4 (Posicionamento, Conteúdo,
  Venda, Jornada). Nunca numeradas de 01 a 05.

## Regras técnicas

- HTML e CSS estáticos. Sem framework, sem etapa de build, sem npm no site.
  A pasta `public/` é literalmente o que sobe para a Hostinger.
- Fontes servidas do próprio domínio (`public/assets/fonts/`), variáveis,
  51 KB para Jost e Manrope inteiras. Nunca chamar o Google Fonts.
- Ciano `#00B4FF` tem teto de 5% da área em qualquer dobra. Um acento, nunca dois.
- Todo filho direto de grid leva `min-width:0`. Coluna `1fr` vale
  `minmax(auto,1fr)` e o item mais largo estica a coluna para fora da tela.
- Todo link de WhatsApp com a mensagem já preenchida.
- `prefers-reduced-motion` respeitado: o giro cai para 40% e o argumento
  continua de pé só pelo texto.
- Nada de `backdrop-filter` em elemento que fique por cima do cubo. Ele cria
  raiz de fundo e recorta o que está atrás numa borda dura, o que faz o cubo
  aparecer picado nas frestas entre cartões.

## Publicar

**O site está na Vercel e publica sozinho a cada push na `main`** (projeto `site-moza`, saída `public/`,
`cleanUrls` ligado). Constatado em 28/09/2026: um push subiu páginas novas direto para o ar. Então:

1. Push na `main` é publicação. Página nova ou texto público passa pela aprovação do Kauan antes do push.
2. O endereço público é `https://www.mozabr.com.br`, sem `.html` (`/privacidade`, não `/privacidade.html`).
   O endereço sem `www` redireciona para ele.
3. Conferir no celular de verdade depois de publicar.

Páginas fora do fluxo principal: `privacidade.html` (política exigida pela Meta para o app de Tech Provider,
com `#exclusao`) e `conectar-whatsapp.html` (cadastro incorporado do WhatsApp para clientes do
pré-atendimento, noindex, só abre com convite).

Refazer o cartão de compartilhamento depois de mexer no texto do hero:

```
python3 -m http.server 8899 &
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --window-size=1200,630 --virtual-time-budget=3000 \
  --screenshot=public/assets/img/og-moza.png http://127.0.0.1:8899/ferramentas/og.html
```

## O acervo (`#acervo`)

Padrão "Explore os detalhes" da Apple: tópicos clicáveis de um lado, a obra do
outro. É `role="tablist"` de verdade, com seta navegando entre abas, e a aba
escolhida vive no endereço (`#acervo=<chave>`), para mandar o link já aberto na
prova certa. O JS acha abas e grupos por índice: acrescentar aba não pede JS.

**A produção de conteúdo vem primeiro, a vitrine por último.** O que a Moza
mais faz é posicionamento e conteúdo; print de site era a primeira coisa que
aparecia e dava a impressão errada do que a casa vende.

- **Aba 1, Produção de conteúdo**: os filmes, montados aqui do roteiro ao som.
  Fonte em `../videos/`, transcodados para `public/assets/video/`. Cada um tem
  três arquivos: o laço curto e mudo (~200KB, roda no cartão), o cartaz, e o
  filme inteiro com som (só baixa no toque). Hoje: Via Brasil (reel da Saveiro),
  PP Automóveis (guia do feirão com rota no drone) e Demari (abertura de
  palestra).
- **Aba 2, Vitrine digital**: os sites de cliente. **Só entra obra que está no
  ar.** Se tirar um site do ar, tira do acervo.

### O que NÃO pode entrar no acervo

**A série do Panamera da Garage 665 saiu em 21/10/2026: a Garage 665 nunca
virou cliente.** Prova de acervo é trabalho entregue a cliente fechado, não
peça feita em tratativa comercial.

Em `next-cerebro/marketing/estudio/masters/` existem masters de Via Brasil, PP
e Santo André que parecem prova. **Não são.** O `*-usage.json` de cada um diz
`status: candidata_gerada_nao_aprovada` e `modelo: gpt-image-*`: candidatas de
IA do desenvolvimento do pipeline. Os arquivos em `estudio/referencias/` são
**fotos de concorrentes**, lidas do estoque público deles.

**Antes de subir peça do estúdio, ler o `-usage.json` e confirmar que o cliente
fechou.**

Nota: não existe vídeo de Porsche da Via Brasil. O filme da Via Brasil é a
**Saveiro Robust 2023**; o Porsche era a série da Garage 665, que saiu.

## Duas seções, duas linguagens

O espelho e o método usam a **mesma mecânica de rolagem** (palco travado, cenas
atravessando a profundidade) e por isso **não podem ter o mesmo desenho**. Se
tiverem, o site se repete e o visitante sente que já viu aquilo.

- **Espelho**: a roda. Objeto renderizado, com volume, luz e textura.
- **Método**: as chapas (`ferramentas/obra.py`). Cinco chapas de vidro que
  descem e assentam uma sobre a outra, num eixo de registro. Empilhamento de
  passes, como gravura ou montagem ótica.

**São elementos em perspectiva 3D do navegador, não SVG.** Quem faz o ângulo é
o `perspective` do palco e a câmera gira com a rolagem (`--giro`). A isometria
desenhada à mão morreu em 21/10/2026: era parelelogramo chapado, sem material e
sem câmera, e foi reprovada por simples.

Duas reprovações já aconteceram aqui, e o teste de cada uma vale:
1. **Não pode puxar para arquitetura** (18/09). Processo e precisão, não obra.
2. **Não pode ser desenho chapado** (21/10). Precisa de material, profundidade
   de verdade e ponto de vista que se mexe.

O método é a **faixa escura da segunda metade** (`tom-azul`), em teste desde
18/09/2026. Se for para voltar ao claro, é trocar a classe e o `data-chao` da
seção: o resto (emenda entre faixas, cor do texto, chips) se ajusta sozinho
pelos tokens de tom.

## O teto do vetor

A roda já levou três passadas: luz de uma fonte só em `userSpaceOnUse`,
especular no ombro, oclusão nos encontros, luz de recorte, faceta escura na
lâmina, banda de rodagem deslocada atrás (que é o que tira a leitura de ícone)
e grão de borracha em azulejo de 48px.

Em 18/09/2026 o Kauan mandou a referência (`Fontes/roda-referencia-azul.png`) e
a roda foi refeita nesse padrão. **Três coisas eram o que a deixava genérica:**

1. O aro era **cromado**. Aro prata é de carro de rua; aro de corrida é preto
   brilhante, e nele o que descreve a forma não é a cor, é o fio de especular
   na quina virada para a luz.
2. Os raios eram **retos**. Agora são dez, em Y, que é o que existe em roda de
   competição. Raio reto lê como ícone.
3. O pneu era **fino demais**. Na referência o aro tem 54% do diâmetro total; a
   versão anterior tinha 69%, e era isso que dava leitura de bicicleta.

Armadilha: raio fino contra poço escuro some, e sobra só o fio de luz. A roda
vira teia de aranha. A lâmina precisa de corpo e de face mais clara que o poço.

**Ainda é desenho, não fotografia.** Gradiente de SVG tem teto.

Cuidado com o grão: azulejo grande demais vira pedrisco. A 18 unidades do
viewBox ele some como grão; a 72 ele aparece como lixa.

## A barra de rolagem da casa

Substitui a do sistema só em ponteiro fino (`hover:hover and pointer:fine`).
Em toque a nativa já se esconde sozinha e uma barra fixa na borda atrapalharia.

Ela não é um tubo com um bastão: é um mapa. Uma marca por seção (`[data-chao]`),
a marca da seção atual acesa em ciano, clique pula para lá, e o punho arrasta.
Numa página com dois trechos travados isso é orientação, não enfeite.

## Gradiente de SVG mora em SVG que sempre existe

Os `<linearGradient>` do M ficam no `<svg>` do **portal**, não no do objeto
travado. O objeto travado é `display:none` abaixo de 900px, e um paint server
dentro de subárvore escondida não resolve: o path fica sem tinta e o M
simplesmente não aparece. Isso pegava todo visitante de celular, que é a
maioria. Se mover os defs de novo, conferir em 393px antes de subir.

## Filho em z-index negativo precisa de contexto próprio

`.hero` leva `isolation:isolate`. A textura e os véus do hero vivem em z-index
negativo, e sem um contexto de empilhamento na própria seção eles caem atrás
do fundo dela: a foto carrega, ocupa a tela inteira e **não pinta um pixel**.
O sintoma é traiçoeiro porque tudo parece certo no DOM. O jeito de confirmar é
amostrar o pixel renderizado: se ele dá exatamente a cor de fundo (`5,7,10`),
a camada não está pintando, não está escura.

## Imagem de fonte não entra no git

`Fontes/` está no `.gitignore` menos o `LEIA-ME.md`, que registra a origem e a
licença de cada arquivo. **Antes de publicar qualquer imagem, conferir a
origem** com `mdls -name kMDItemWhereFroms arquivo.jpg`. Borrar logo resolve
confusão de marca, não resolve direito autoral: o que se licencia é a
fotografia, não o que aparece nela.

## O modo headless antigo trava nesta máquina

`--headless` (antigo) pendura por minutos; `--headless=new` resolve. O
`foto.mjs` e o `qa.mjs` já usam o novo. Se uma captura travar, conferir também
a memória livre (`vm_stat`): com o Chrome do Kauan aberto sobra pouca, e aí
qualquer render fica lento. Nunca matar Chrome por nome: só os processos com
`user-data-dir=/tmp/moza-*` são nossos.

## O site rola suave, a sonda não pode

`html` tem `scroll-behavior:smooth`. Qualquer `scrollTo` de ferramenta precisa
de `behavior:'instant'`, senão a captura sai de um ponto do caminho em vez do
destino e você passa a tarde caçando um defeito que não existe. Isso já custou
tempo duas vezes: uma culpando imagem que carrega tarde, outra achando que a
animação não chegava ao fim.

## Desempenho: a régua é 60fps em celular médio

Medido em 19/10/2026 com `Emulation.setCPUThrottlingRate: 4` e largura de
390px, rolando 90 quadros em cada dobra pesada (hero, espelho, campo WebGL,
chapas, acervo): **60fps em todas, zero quadro acima de 33ms.**

A ressalva honesta: é headless com CPU estrangulada num Mac, que é o proxy
padrão, não um aparelho de verdade. Se mexer em WebGL, filtro de desfoque ou
número de camadas animadas, **medir de novo antes de subir**. A sonda está em
`ferramentas/` como molde do `foto.mjs`.

Por que importa: jurado de Awwwards (2026) resume o corte em quatro, e o
terceiro é o que mais reprova: direção de arte, movimento dirigido, **60fps em
celular médio sob estrangulamento**, e fallback de movimento reduzido que não
seja quebrado.

## Armadilha da sonda de QA

Alvo de toque se mede por `offsetWidth`/`offsetHeight`, **nunca** por
`getBoundingClientRect()`. O retângulo vem já transformado, e o `rotateX` da
animação de profundidade achata a medida: dá falso positivo de alvo pequeno em
elemento que tem 46px de layout. Isso custou tempo uma vez.

## O que ainda falta no site

- `assets/img/pratica/`: três capturas anonimizadas (mapa mental, deck, painel).
  Trocar os blocos `.artefato__vazio` do index por `<img>`.
- `assets/img/socios/`: retratos do Kauan e do Murillo. Trocar o svg do
  `.socio__retrato` por `<img>`. Sem eles a seção sobe com o marcador da marca.
