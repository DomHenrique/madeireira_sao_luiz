## 1. Backend: Modelo e Lógica de Dados

- [x] 1.1 Criar o modelo `Marca` em `core/models.py` com os campos `name` (Char), `logo` (Image), `active` (Boolean), `order` (Integer) e `url` (URL, opcional).
- [x] 1.2 Criar e rodar as migrações para o novo modelo de Marca (`makemigrations core` e `migrate`).
- [x] 1.3 Registrar o modelo no `core/admin.py` criando uma classe `MarcaAdmin` para facilitar a gestão no painel (list_display, search_fields, etc.).
- [x] 1.4 Modificar a view `home` em `core/views.py` para consultar as marcas ativas (`Marca.objects.filter(active=True).order_by('order')`) e enviá-las no contexto como `marcas_destaque`.

## 2. Frontend: CSS da Animação (Design System & LP)

- [x] 2.1 Adicionar em `static/css/design_system.css` a estrutura do Marquee: `.marquee-wrapper` com `overflow: hidden`, e `.marquee-track` com `display: flex`, `width: max-content` e `animation: marquee-scroll 20s linear infinite`.
- [x] 2.2 Criar o `@keyframes marquee-scroll` que faz a translação de `transform: translateX(0)` até `transform: translateX(-50%)`.
- [x] 2.3 Estilizar os logos dentro da track (ex: altura fixa de 60px, grayscale dinâmico, margens entre eles) e adicionar `.marquee-track:hover` com `animation-play-state: paused`.
- [x] 2.4 Replicar as exatas mesmas regras de CSS no arquivo `lp/style.css` da Landing Page.

## 3. Frontend: Templates HTML (Django & LP)

- [x] 3.1 Adicionar a nova seção `<section id="marcas">` no `templates/core/home.html` (abaixo dos destaques ou categorias).
- [x] 3.2 Estruturar a div `.marquee-wrapper` e `.marquee-track` na `home.html`, fazendo **dois loops** sequenciais do `{% for marca in marcas_destaque %}` lado a lado para garantir que a animação não tenha buracos ao resetar o 50%.
- [x] 3.3 Adicionar a mesma seção de marcas no arquivo `lp/index.html` (Landing Page estática), colando os logos e HTML em hardcode duas vezes seguidas para replicar o comportamento do Django na versão puramente estática.
