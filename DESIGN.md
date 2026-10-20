# DESIGN.md · Moza

> **Este arquivo é derivado, não é fonte.** A fonte é a seção 06 do brandbook
> (`../next-cerebro/marca/rebranding/fontes/brandbook-moza.md`). Mudou a marca?
> Muda lá primeiro, depois aqui. Nunca o contrário.
>
> Ele existe porque o brandbook é escrito para gente e está espalhado em 508
> linhas, e um agente precisa de um lugar só com cor, fonte, componente e
> limite. Última conferência contra o brandbook: 19/10/2026.

---

## 1 · Tema visual e atmosfera

Instrumento de precisão, não cartaz de agência. A página é escura e larga no
hero, clara e arejada no corpo, e volta ao escuro na chamada e no rodapé. A
densidade é baixa de propósito: cada dobra tem um assunto, e manchete é
fragmento curto com ponto final, nunca frase explicativa.

O que a marca quer dizer é **centro**. Mozzo é o cubo da roda, a peça do meio
onde os raios se prendem. Toda decisão visual serve a isso: um acento, no
lugar exato, e o resto se cala.

**Nunca:** cara de template, gradiente decorativo, cartão dentro de cartão,
selinho de jargão, sombra colorida, emoji na interface.

## 2 · Paleta e papéis

A base da marca é fundo escuro. **O site é exceção registrada** (brandbook,
12/09/2026): preto só no hero, na chamada e no rodapé; o corpo joga em branco,
cinza frio e uma faixa de azul-marinho.

| Papel | Valor | Onde vive |
|---|---|---|
| Acento único, CTA, destaque | `#00B4FF` ciano | **Teto de ~5% da área em qualquer dobra. Um acento, nunca dois** |
| Chão escuro | `#05070A` | Hero e rodapé |
| Chão escuro, nível 2 e 3 | `#0A0E13` · `#10161D` | Superfície elevada no escuro |
| Azul-marinho de seção | `#0A2340` | O nome, o método, a chamada |
| Chão claro | `#FFFFFF` · `#F2F5F9` | Corpo da página |
| Texto claro | `#E6EDF3` | Sobre fundo escuro |
| Texto mudo | `#78848F` | Legenda e metadado |
| Texto em peça clara | `#123A5F` azul-tinta | **Não é segundo acento.** É o `#E6EDF3` do outro lado |
| Link e texto de acento no claro | `#0071AD` | O ciano **não passa contraste como texto sobre branco** |
| Fio | `rgba(230,237,243,.07)` e `.15` | Divisória e borda |

**A regra que mais se quebra sem perceber:** no fundo claro o ciano só vale em
preenchimento (botão). Texto e link em ciano sobre branco é erro de contraste.

Cada seção declara o seu chão em `data-chao`, e o `html` acompanha. A emenda
entre faixas lê essa cor sozinha.

## 3 · Tipografia

| Papel | Fonte | Peso |
|---|---|---|
| Display e títulos | **Jost** (revival aberta da Futura) | 300 |
| Corpo | **Manrope** | 400, 600 no `strong` |

Servidas do próprio domínio (`assets/fonts/`, variáveis, 51 KB as duas).
**Nunca chamar o Google Fonts.**

| Classe | Tamanho | Uso |
|---|---|---|
| `.tela` | `clamp(2.6rem, 7.2vw, 5.6rem)` · altura 1.02 · tracking −.032em | Manchete de dobra |
| `.tela--m` | `clamp(2.1rem, 5vw, 3.6rem)` | Um degrau abaixo, dentro de cena |
| `.titulo` | `clamp(2rem, 4.6vw, 3.4rem)` | Título de bloco |
| `.sub` | `clamp(1.45rem, 2.6vw, 1.95rem)` | Subtítulo, h1 do hero |
| `.corpo` | 18.5px · altura 1.55 · máx 58ch | Texto corrido |
| `.corpo--g` | `clamp(1.2rem, 1.9vw, 1.45rem)` | Linha de apoio da dobra |
| `.etiqueta` | 12.5px · tracking .24em · caixa alta | Rótulo de seção |

Caixa alta **só em etiqueta e sigla**, nunca para dar ênfase.
`text-wrap: balance` em toda manchete, para não deixar palavra órfã.

**A wordmark não é fonte.** Está desenhada em vetor, letra por letra. Ninguém
recria digitando em Jost.

## 4 · Componentes

**Botão** (`.btn`): pílula, altura mínima 46px, `--canto: 2px` no resto do site
mas raio total aqui.
- `.btn--primario`: fundo ciano, texto `#04141F`. Hover sobe 1px e ganha brilho.
  No clique abre um anel que some. É o único micro-movimento de botão do site.
- `.btn--fantasma`: transparente, borda `--fio-2`.

**Aba** (`.aba`): `role="tab"` de verdade, seta do teclado navega, a escolhida
vive no endereço (`#acervo=<chave>`).

**Cartão de obra** (`.obraCard`): imagem com raio 14px, borda de fio, legenda
embaixo. A imagem cresce 3% no hover, em 900ms.

**Pergunta** (`.pergunta`): `<details>` nativo, uma aberta por vez.

**Painel de vidro** (`.vidro`): só no escuro. **Nunca `backdrop-filter`** em
elemento que fique por cima de objeto: ele cria raiz de fundo e recorta o que
está atrás numa borda dura.

**Barra de rolagem da casa**: substitui a nativa só em ponteiro fino. É mapa,
não tubo: uma marca por seção, a atual acesa em ciano.

## 5 · Layout e espaço

Escala de oito passos, em px fixo. Não inventar valor fora dela.

```
--s1 8   --s2 16   --s3 22   --s4 34
--s5 50  --s6 70   --s7 96   --s8 124
```

- Largura do envelope: `--largura: 1120px`.
- Respiro de seção: `padding-block: clamp(--s6, 8.5vw, --s8)`.
- Medida de leitura: 58ch no corpo, 42ch dentro de cena de portal.
- **Todo filho direto de grid leva `min-width: 0`.** Coluna `1fr` vale
  `minmax(auto, 1fr)`, e o item mais largo estica a coluna para fora da tela.
- No desktop, dentro dos portais: informação de um lado, objeto do outro.
  No celular o objeto vai para cima do texto.

## 6 · Profundidade

A página tem eixo Z de verdade, não sombra fingida.

- Palco travado com `perspective: 1200px`. As cenas atravessam em `translateZ`,
  de −1500 a 0 e saindo em +860.
- **A escala nunca é escrita à mão.** O objeto anda em linha reta no Z e a
  perspectiva faz a aceleração: a curva é a hipérbole `1200/(1200−z)`. É o que
  separa aproximação de câmera de crescimento de keyframe.
- Sombra: `0 26px 60px rgba(0,60,120,.4)` no escuro, mais fechada no claro.
- **`transform` em ancestral quebra `position: sticky`.** A perspectiva vai no
  próprio elemento travado, nunca acima dele.
- **Filho em `z-index` negativo precisa de contexto próprio.** Sem
  `isolation: isolate` na seção, ele cai atrás do fundo dela e não pinta.

## 7 · Pode e não pode

**Pode**
- Foto de produção da casa, em cliente real, com o pátio e o letreiro dele.
- Drone da Moza sobre o estoque de quem a casa atende.
- Objeto desenhado em vetor pela casa, a partir de referência.

**Não pode**
- Banco de imagem automotivo, carro esportivo genérico, close de roda comprado.
  O critério é a origem: **se a foto é prova do trabalho, entra; se é
  ilustração comprada, não entra** (brandbook, 08/09/2026).
- Stock techy, mockup genérico, gráfico de constelação, ícone de banco.
- Dois acentos. Hue fora da família do azul.
- Travessão. Exclamação. Caixa alta para ênfase.
- Preço, prazo, comparativo de plano.
- "Nosso time", "nossa equipe", plural de fachada. É "a Moza", "nós", ou o
  nome do sócio.
- Palavras banidas: garantido, explosivo, revolucionário, fórmula, segredo,
  alavancar, acelerar, turbinar, pisar fundo, o melhor do mercado, visão 360,
  ICP, personas.
- **Número, depoimento ou dado de cliente que não exista e não esteja
  autorizado.**

## 8 · Responsivo

- Quebra única em **900px**. Abaixo dela o portal empilha, o objeto travado
  some e a roda vira objeto acima do texto.
- Alvo de toque **mínimo 44px**. Medir por `offsetWidth`/`offsetHeight`, nunca
  por `getBoundingClientRect()`: o retângulo vem transformado e a animação de
  profundidade achata a medida.
- Sem rolagem horizontal em nenhuma largura de 320 a 1440.
- `scroll-padding-top: 92px`, senão a âncora para embaixo do cabeçalho fixo.
- `env(safe-area-inset-*)` no hero, que sangra de borda a borda.
- `touch-action: manipulation` em tudo que clica, senão o navegador espera
  300ms por um duplo toque.

## 9 · Guia de pedido para o agente

Cores de bolso: ciano `#00B4FF`, marinho `#0A2340`, tinta `#123A5F`,
breu `#05070A`, claro `#E6EDF3`, mudo `#78848F`.

Pedidos que funcionam:

```
Monta a seção seguindo o DESIGN.md: tom claro, etiqueta, .tela de manchete,
.corpo--g de apoio. Um acento só, dentro do teto de 5%.
```

```
Essa dobra está com cara de template. Relê a seção 7 do DESIGN.md e me diz o
que está quebrando, antes de corrigir.
```

**Antes de entregar qualquer dobra:** rodar `node ferramentas/qa.mjs`. Ele
confere estouro horizontal, alvo de toque, `alt` e contagem de `h1` em sete
telas, e não confia no olho.
