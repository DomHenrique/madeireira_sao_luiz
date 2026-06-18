## Why

O sistema foi desenvolvido originalmente para a "Madeireira São Luiz" e precisa ser transformado em um sistema modelo (white-label) reutilizável. A Matcon é o primeiro cliente desse modelo, e toda referência à marca anterior deve ser substituída para que o sistema possa ser implantado com identidade própria da Matcon — incluindo URLs de produção no domínio `matcon.griddmkt360.com.br`.

## What Changes

- Substituir todas as ocorrências de "Madeireira São Luiz" / "Madereira São Luiz" por "Matcon" nos templates HTML, CSS, Python e arquivos de configuração
- Atualizar o `docker-compose.yml`: container name, labels do Traefik e hostname para `matcon.griddmkt360.com.br`
- Atualizar `config/settings.py`: `JAZZMIN_SETTINGS` (site_title, site_header, site_brand, copyright) e comentários
- Atualizar `config/urls.py` e `config/wsgi.py` (docstrings/comentários)
- Atualizar `setup.sh` (mensagens de setup)
- Atualizar `lp/index.html` e `lp/style.css` (landing page pública)
- Atualizar todos os templates Django: `base.html`, `home.html`, `about_us.html`, `product_detail.html`, `products.html`, `robots.txt`
- Atualizar arquivos CSS: `design_system.css`, `admin_custom.css`
- Atualizar `README.md`
- **NÃO alterar**: banco de dados (Supabase/PostgreSQL), bucket S3/Supabase Storage (`madeireira-sao-luiz`), migrations existentes
- **NÃO alterar**: conteúdo geográfico/local (Tupandi, RS) e links do Google Maps (são dados do cliente, mantidos como modelo)

## Capabilities

### New Capabilities

- `brand-identity`: Define a identidade de marca "Matcon" em todos os pontos de exibição do sistema — nome, domínio, metadados SEO, textos de rodapé e admin

### Modified Capabilities

<!-- Nenhuma capability existente com spec formal. Todas as mudanças são de configuração e conteúdo de marca. -->

## Impact

- **docker-compose.yml**: container_name, Traefik router/service names, Host rule (domínio)
- **config/settings.py**: JAZZMIN_SETTINGS (títulos do admin Django)
- **config/urls.py**, **config/wsgi.py**: comentários/docstrings
- **setup.sh**: mensagens de terminal
- **lp/index.html + lp/style.css**: landing page pública
- **templates/**: base.html, home.html, about_us.html, product_detail.html, products.html, robots.txt
- **static/css/**: design_system.css, admin_custom.css
- **README.md**: documentação
- Sem impacto em banco de dados, migrations ou storage
