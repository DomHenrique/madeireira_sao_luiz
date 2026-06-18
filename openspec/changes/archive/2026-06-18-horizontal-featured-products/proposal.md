## Why

Os cards da seção "Produtos em Destaque" na página inicial atualmente ocupam muito espaço vertical na tela devido ao formato grid com cards grandes (imagem 4:3, descrição de até 3 linhas e paddings extensos). Isso prejudica a experiência em monitores menores e exige muita rolagem do usuário. A alteração para um layout de carrossel horizontal de movimento contínuo não só economiza espaço vertical, como também confere maior dinamismo e modernidade à interface inicial da Matcon.

## What Changes

- Transformação da estrutura de Grid (colunas) da seção "Produtos em Destaque" (`home.html`) para um contêiner horizontal (carrossel).
- Redução da altura vertical dos cards (`.product-card`):
  - Alteração do `aspect-ratio` da imagem de 4:3 para 16:9.
  - Ocultamento ou redução da descrição textual do produto (`product.description`) apenas na Home.
- Implementação de rolagem horizontal contínua e suave via JavaScript Nativo (`requestAnimationFrame`), permitindo interação tátil em dispositivos móveis e pausa no hover.
- Adição de setas de navegação esquerda/direita que permitem o usuário avançar ou retroceder a rolagem do carrossel ao serem clicadas.

## Capabilities

### New Capabilities
Nenhuma nova funcionalidade a nível de produto/sistema. Apenas uma alteração na apresentação (UI).

### Modified Capabilities
- `home-page-layout`: Os requisitos de interface da seção "Produtos em Destaque" estão mudando de uma grade estática para um carrossel horizontal contínuo.

## Impact

- `templates/core/home.html` e `lp/index.html` (nova estrutura HTML para o contêiner do carrossel e botões de seta).
- `static/css/design_system.css` e `lp/style.css` (novas classes de layout flexível com `overflow-x` para o carrossel e ajustes nos paddings/aspect-ratio do `product-card` na home e na LP).
- Adição de script JS para controlar a lógica de auto-scroll nativo e setas, tanto no Django (`home.html` ou arquivo estático) quanto na Landing Page (`lp/script.js`).
