## 1. Ajustes de CSS (Design System & Landing Page)

- [x] 1.1 Adicionar classes do contêiner `.featured-carousel-wrapper` e da trilha `.featured-carousel-track` no `static/css/design_system.css` e no `lp/style.css`.
- [x] 1.2 Ajustar os cards dentro do `.featured-carousel-track`: fixar `min-width`, alterar `.product-card__image-wrap` para `aspect-ratio: 16/9` (em ambos os CSS).
- [x] 1.3 Ocultar a descrição `.product-card__desc` e estilizar os botões de seta do carrossel nos dois CSS.

## 2. Refatoração dos Templates (Home & Landing Page)

- [x] 2.1 Envolver o laço de produtos no `templates/core/home.html` com as divs `.featured-carousel-wrapper` e `.featured-carousel-track`.
- [x] 2.2 Fazer a mesma substituição estrutural na listagem estática de produtos do `lp/index.html`.
- [x] 2.3 Adicionar os botões HTML de seta esquerda/direita com ícones correspondentes em ambos os templates.

## 3. Lógica JavaScript de Scroll Contínuo

- [x] 3.1 Adicionar o script de carrossel no `lp/script.js` e também integrado na Home do Django (via tag `<script>` ou arquivo estático JS).
- [x] 3.2 Implementar `requestAnimationFrame` para auto-scroll contínuo do `.featured-carousel-track`.
- [x] 3.3 Adicionar listeners de pausa no hover/touch e gerenciar clique nas setas de navegação `scrollBy({ left: +/- 300 })`.
- [x] 3.4 Implementar reinício suave do loop quando a rolagem atinge o final.
