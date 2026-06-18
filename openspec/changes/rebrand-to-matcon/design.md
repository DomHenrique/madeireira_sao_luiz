## Context

O projeto é um site institucional/e-commerce Django para empresas do setor de construção civil e madeireiras. Ele foi criado com a marca "Madeireira São Luiz" mas foi concebido desde o início como um sistema white-label reutilizável (ver `WHITE_LABEL_SPEC.md`).

A mudança atual é puramente de **rebranding**: substituição de strings de marca em arquivos de texto/código, sem alteração de lógica de negócio, banco de dados ou infraestrutura de storage. O banco Supabase/PostgreSQL e o bucket S3 (`madeireira-sao-luiz`) são mantidos intactos para evitar downtime e perda de dados.

## Goals / Non-Goals

**Goals:**
- Substituir todas as referências visíveis à marca "Madeireira São Luiz" por "Matcon"
- Atualizar o domínio de produção no docker-compose para `matcon.griddmkt360.com.br`
- Atualizar labels do Traefik e container name para refletir o novo nome
- Garantir que admin Django, templates públicos, landing page e metadados SEO exibam "Matcon"

**Non-Goals:**
- Renomear o bucket S3/Supabase Storage
- Alterar ou criar migrations de banco de dados
- Modificar lógica de negócio, modelos, views ou URLs da aplicação
- Alterar conteúdo geográfico/local (endereço, Google Maps, Tupandi/RS)
- Redesign visual (cores, fontes, layout)

## Decisions

### 1. Substituição por busca global de string, arquivo por arquivo

**Decisão**: Fazer substituição literal de strings, arquivo por arquivo, usando edição direta com as ferramentas de código. Não usar scripts `sed` em massa.

**Rationale**: A abordagem arquivo-por-arquivo permite revisão do contexto de cada ocorrência, evitando substituições indevidas (ex: nome do bucket S3 que é mantido, comentários de migração, etc.). É mais segura para um projeto de tamanho limitado (~14 arquivos afetados).

### 2. Manter o bucket S3 com o nome original

**Decisão**: `AWS_STORAGE_BUCKET_NAME=madeireira-sao-luiz` permanece inalterado no `.env` e `settings.py`.

**Rationale**: Renomear o bucket exigiria migrar todos os arquivos de mídia no Supabase Storage, o que está fora do escopo e representa risco de perda de dados.

### 3. Manter o banco de dados Supabase sem alterações

**Decisão**: Nenhuma migration nova será criada. O texto default do campo `featured_subtitle` na migration `0009` não será alterado retroativamente.

**Rationale**: O texto existente no banco é dado da instância, não do código. A migration já foi aplicada. Alterar o default no código não afeta registros já criados.

### 4. Traefik: substituir todos os identificadores de router/service

**Decisão**: Renomear `madereira` → `matcon` em todos os labels Traefik do docker-compose, e o hostname de `saoluiz.griddmkt360.com.br` para `matcon.griddmkt360.com.br`.

**Rationale**: O hostname é o que define o roteamento real na VPS. Os identificadores de router/service são apenas nomes internos do Traefik, mas devem ser consistentes para evitar conflitos se coexistir com outros projetos no mesmo servidor.

## Risks / Trade-offs

| Risco | Mitigação |
|-------|-----------|
| Ocorrência de "Madeireira" esquecida em algum template | Verificação final com `grep -r "madeireira\|Madeireira\|São Luiz\|sao.luiz"` após todas as edições |
| Conflito de nome no Traefik se o container antigo ainda estiver rodando | Parar o container antigo antes do deploy com o novo compose |
| E-mail de contato `contato@madeireirasaoluiz.com.br` na LP ainda referencia domínio antigo | Aceito como limitação — domínio de e-mail do cliente, não do sistema |
