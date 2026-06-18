## ADDED Requirements

### Requirement: Identidade de marca Matcon exibida em todo o sistema
O sistema SHALL exibir "Matcon" como nome da empresa em todos os pontos de interface — admin Django, templates públicos, landing page, metadados SEO e configurações de infraestrutura.

#### Scenario: Admin Django exibe marca Matcon
- **WHEN** um usuário acessa o painel administrativo Django
- **THEN** o título da aba, o cabeçalho do site e o nome da marca SHALL exibir "Matcon" (sem referência à "Madeireira São Luiz")

#### Scenario: Templates públicos exibem marca Matcon
- **WHEN** um visitante acessa qualquer página pública do site (home, produtos, sobre, detalhe de produto)
- **THEN** o nome exibido no header, footer, metadados og:title e og:site_name SHALL ser "Matcon"

#### Scenario: Landing page exibe marca Matcon
- **WHEN** um visitante acessa a landing page (`lp/index.html`)
- **THEN** todos os textos de marca, título da página e metadados SHALL referenciar "Matcon"

#### Scenario: Docker Compose roteia para domínio Matcon
- **WHEN** o container é iniciado com o docker-compose.yml
- **THEN** o Traefik SHALL rotear tráfego do host `matcon.griddmkt360.com.br` para o serviço, com container_name `matcon_web`

#### Scenario: Robots.txt referencia sitemap correto
- **WHEN** um crawler acessa `/robots.txt`
- **THEN** o sitemap SHALL apontar para `https://www.matcon.griddmkt360.com.br/sitemap.xml` (ou domínio configurado)
