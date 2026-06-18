## Context

A seção "Produtos em Destaque" da página inicial exibia os produtos em uma grade verticalizada (colunas do Bootstrap), fazendo com que os cards de produtos empilhassem e tomassem muito espaço vertical na tela, especialmente porque cada card utilizava imagens grandes (4:3) e muito texto de descrição.

Para melhorar o layout, estamos transformando a grade em um **Carrossel Horizontal de rolagem contínua**, sem bibliotecas pesadas. O desafio principal é conciliar o auto-scroll (marquee) suave via JavaScript com a capacidade do usuário usar setas nativas ou toque para navegar pelos itens.

## Goals / Non-Goals

**Goals:**
- Mudar o container de produtos da Home e da Landing Page de uma `.row` que quebra linhas para um contêiner `.featured-carousel-track` de rolagem horizontal.
- Diminuir a altura do `.product-card`, passando a imagem para um ratio de `16:9` e escondendo a tag `<p>` da descrição no contexto do carrossel.
- Adicionar scroll automático leve da direita para a esquerda usando `requestAnimationFrame` que pausa no `:hover`.
- Botões de `<` e `>` nas extremidades para rolar manualmente `+300px` por clique.

**Non-Goals:**
- Não alterar a exibição do produto na página de `/produtos/` (listagem total) — lá deve continuar sendo um grid normal.
- Não incluir bibliotecas JS de terceiros (ex: Swiper, Slick), mantendo zero dependências no frontend.
- Não mudar a estrutura dos modelos em Python. O backend continuará retornando a query `featured_products`.

## Decisions

- **CSS vs JS para o Auto-scroll**:
  - *Alternativa*: Animação CSS de `transform: translateX` infinita.
  - *Problema da Alternativa*: Muito complexo adicionar setas interativas por cima de uma timeline puramente CSS.
  - *Decisão*: Usaremos um wrapper com `overflow-x: auto; scroll-behavior: smooth;` no CSS, e um script JS Vanilla rodando `requestAnimationFrame` que incrementa o `.scrollLeft` aos poucos. As setas simplesmente somam/subtraem valor ao `.scrollLeft`. Essa lógica será aplicada tanto no app Django quanto no `lp/script.js`.
- **Ajuste de Altura dos Cards**:
  - *Decisão*: Usaremos um seletor CSS específico `.featured-carousel-track .product-card__image-wrap { aspect-ratio: 16/9; }` e `.featured-carousel-track .product-card__desc { display: none; }` em ambos os arquivos CSS (`design_system.css` e `lp/style.css`). Dessa forma evitamos sujar o CSS base e não quebramos a exibição em outras partes do sistema.

## Risks / Trade-offs

- **Experiência de Uso em Mobile**: Um scroll contínuo muito rápido pode irritar no celular.
  - *Mitigação*: O script verificará interações de toque (`touchstart`) para parar o scroll contínuo e deixar o usuário deslizar naturalmente usando o scroll nativo do CSS.
- **Scroll Infinito "Real" (Looping)**: JS puro não repete itens sozinhos sem clonagem de DOM. Fazer os produtos voltarem ao início sem corte (looping perfeito) requer clonar todos os cards no DOM.
  - *Mitigação*: Implementaremos um looping simples: quando o `scrollLeft` atingir o máximo (`scrollWidth - clientWidth`), o script rebobina o carrossel para 0 suavemente, ou clona os nós caso haja menos de 10 produtos. Para simplificar e manter a acessibilidade, apenas rolaremos para a direita e voltaremos ao início quando bater na parede final.
