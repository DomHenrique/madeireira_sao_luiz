## 1. Infraestrutura / Docker

- [x] 1.1 Atualizar `docker-compose.yml`: `container_name` de `madereira_sao_luiz_web` para `matcon_web`
- [x] 1.2 Atualizar labels Traefik: renomear routers/services de `madereira` / `madereira-http` para `matcon` / `matcon-http`
- [x] 1.3 Atualizar hostname Traefik de `saoluiz.griddmkt360.com.br` para `matcon.griddmkt360.com.br` (linhas 38 e 44)

## 2. Configuração Django

- [x] 2.1 Atualizar `config/settings.py`: comentário do topo (`Django settings - Madereira São Luiz` → `Matcon`)
- [x] 2.2 Atualizar `config/settings.py`: `JAZZMIN_SETTINGS` — `site_title`, `site_header`, `site_brand` e `copyright`
- [x] 2.3 Atualizar `config/urls.py`: docstring/comentário do módulo
- [x] 2.4 Atualizar `config/wsgi.py`: docstring/comentário do módulo

## 3. Templates Django

- [x] 3.1 Atualizar `templates/base.html`: meta description padrão, title padrão, og:title, og:description, og:site_name, header logo e footer
- [x] 3.2 Atualizar `templates/core/home.html`: meta description, eyebrow text, texto sobre a empresa, structured data `itemprop="name"`, texto da seção WhatsApp
- [x] 3.3 Atualizar `templates/core/about_us.html`: title, h2 da empresa, texto descritivo (manter "Tupandi, RS" como dado do cliente)
- [x] 3.4 Atualizar `templates/core/product_detail.html`: title e texto do link de WhatsApp
- [x] 3.5 Atualizar `templates/core/products.html`: meta_description padrão
- [x] 3.6 Atualizar `templates/robots.txt`: URL do sitemap

## 4. Landing Page

- [x] 4.1 Atualizar `lp/index.html`: meta description, title, og:title, og:description, og:site_name, header logo, eyebrow text, texto sobre a empresa, seção featured, WhatsApp CTA, footer brand e copyright
- [x] 4.2 Atualizar `lp/style.css`: comentário do cabeçalho

## 5. CSS Estático

- [x] 5.1 Atualizar `static/css/design_system.css`: comentários do cabeçalho
- [x] 5.2 Atualizar `static/css/admin_custom.css`: comentário do cabeçalho

## 6. Scripts e Documentação

- [x] 6.1 Atualizar `setup.sh`: mensagem do banner de setup
- [x] 6.2 Atualizar `README.md`: título, referências ao nome do projeto e ao bucket

## 7. Verificação Final

- [x] 7.1 Executar grep — zero referências ativas encontradas (apenas bucket S3, migrations e scripts utilitários legados esperados)
- [x] 7.2 Confirmar que o server Django sobe sem erros: `python manage.py check` → **0 issues**
