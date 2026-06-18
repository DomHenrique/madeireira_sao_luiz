## Why

A seção "Marcas em Destaque" atualmente não existe. O usuário aprovou a ideia de criar uma seção que mostre marcas que a empresa trabalha, em formato de letreiro digital contínuo (marquee) em loop infinito. Isso adicionará dinamismo à home do site, aproveitando o espaço de tela para mostrar mais marcas através de uma animação suave e contínua feita puramente com CSS.

## What Changes

- Criação do modelo `Marca` no backend (Django Admin) para gerenciar as logomarcas que aparecem no site.
- Injeção das `marcas_destaque` na view `home`.
- Inclusão da seção "Marcas em Destaque" nos templates `home.html` (Django) e `lp/index.html` (Landing Page).
- Criação de um contêiner "marquee" ocultando o "overflow" e usando `display: flex; width: max-content;`.
- Criação do CSS para a animação "scroll-left" usando `@keyframes`, permitindo translação contínua.
- Duplicação dos elementos do loop `{% for marca in marcas_destaque %}` (e elementos estáticos na LP) no template HTML para garantir que o carrossel reinicie de forma transparente.
- Adição da ação `hover` para pausar a animação (`animation-play-state: paused`).

## Capabilities

### New Capabilities
Nenhuma.

### Modified Capabilities
- `marcas`: O requisito do frontend que falava de "horizontal carousel" agora é especificamente "infinite CSS marquee". 

## Impact

- **Backend:** Criação do model `Marca` em `core/models.py`, registro no `core/admin.py` e query no `core/views.py`.
- **Templates:** `templates/core/home.html` e `lp/index.html` receberão a nova seção de marcas com os logos duplicados em tela.
- **CSS:** `static/css/design_system.css` e `lp/style.css` receberão o `@keyframes marquee` e as classes responsáveis pelo loop contínuo e ocultação do overflow.
- **Performance:** Nenhuma biblioteca Javascript nova (impacto zero na main thread), totalmente resolvido via motor CSS.
