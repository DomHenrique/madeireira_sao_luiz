# 🚀 Spec-Driven Development: White Label Django Institucional

Este documento é a especificação técnica (Spec) baseada no projeto original. Ele serve como um **Guia de Recriação Passo a Passo** para gerar um clone exato deste sistema para uma **nova empresa**, mudando apenas a parte comercial (nomes, textos) e o design (cores, tipografia).

Para recriar o projeto do zero usando uma IA (como o Antigravity/Gemini), basta fornecer este arquivo como contexto e pedir para ela seguir o **Passo a Passo**.

---

## 🏗️ 1. Arquitetura e Stack Tecnológica
A base do projeto deve ser construída estritamente com as seguintes tecnologias:
- **Backend**: Django 6 + Python 3.12+
- **Banco de Dados**: PostgreSQL (Supabase) via `psycopg2-binary`
- **Storage**: Supabase Storage S3-compatible via `django-storages` e `boto3`
- **Painel Administrativo**: `django-jazzmin` (Dark Mode enabled)
- **Frontend**: HTML5 Semântico, Vanilla CSS (arquitetura BEM/isolada), e Bootstrap 5.3 via CDN.
- **Sem Frameworks JS Pesados**: Nada de React/Vue/Tailwind. Usar apenas Javascript puro quando necessário para UI.

---

## 🎨 2. Variáveis Comerciais e de Design (O que deve ser alterado)
Antes de iniciar o código, defina estas variáveis para a nova empresa:

1. **Nome da Empresa**: `[NOME_DA_EMPRESA]`
2. **Nicho de Mercado**: `[EX: Clínica Odontológica, Escritório de Advocacia, Loja de Peças]`
3. **Cores da Marca**:
   - `Primary`: `[COR_HEXADECIMAL]` (Ex: Laranja #dc6f00)
   - `Primary Dark`: `[COR_HEXADECIMAL]` (Tom mais escuro para contraste/hover)
   - `Primary Light`: `[COR_HEXADECIMAL]` (Tom mais claro)
   - `Accent`: `[COR_HEXADECIMAL]` (Cor secundária)
4. **Tipografia**: `[GOOGLE_FONT_PRIMARIA]` e `[GOOGLE_FONT_SECUNDARIA]`
5. **Dados do Superusuário**:
   - `Admin Username`: `[USERNAME]`
   - `Admin Email`: `[EMAIL_ADMIN]`
   - `Admin Password`: `[SENHA_FORTE]`
6. **Dados da Primeira Unidade (Matriz)**: A IA deve exigir todos estes dados antes de rodar as migrations finais:
   - `Endereço Completo`, `Cidade`, `Estado`, `CEP`
   - `Telefone Fixo` e `WhatsApp`
   - `E-mail de Contato`
   - `Horário de Funcionamento`
   - `Link do Google Maps (Iframe)` e `Link de Rota do Google Maps`

---

## ⚙️ 3. Passo a Passo de Implementação (Para a IA / Desenvolvedor)

### Fase 1: Infraestrutura na Cloud (Supabase via MCP)
Antes de escrever código, a infraestrutura deve ser provisionada:
1. Solicite à IA que habilite ou acesse o **Supabase MCP** (se disponível na IDE).
2. Use o MCP para criar um novo **Projeto no Supabase** com o `[NOME_DA_EMPRESA]`.
3. Capture a URI de Conexão do PostgreSQL (Transaction mode) e salve no arquivo `.env`.
4. Crie um **Bucket público** no Supabase Storage para gerenciar as imagens (ex: `[nome]-media`).
5. Gere e capture as credenciais compatíveis com S3 (Access Key, Secret Key e Endpoint) para o `django-storages` no `.env`.

### Fase 2: Setup do Projeto Django
1. Inicie um projeto Django padrão (`django-admin startproject config .`).
2. Instale as dependências: `django`, `django-jazzmin`, `django-storages`, `boto3`, `psycopg2-binary`, `pillow`, `python-dotenv`.
3. Configure o `settings.py` para conectar ao banco do Supabase e ao Storage configurados na Fase 1.
4. Execute as migrations iniciais (`python manage.py migrate`).
5. Crie o Superusuário usando os dados informados na seção de variáveis (utilize `python manage.py createsuperuser --noinput` e defina a senha via shell, ou crie interativamente).

### Fase 3: Aplicativo "Empresa" (Gestão de Filiais)
1. Crie o app `empresa`.
2. Crie o modelo `Unidade` contendo:
   - Nome da filial, Endereço completo, Cidade, Estado, CEP.
   - Contatos: Telefone, Email, WhatsApp (usando regex/validators).
   - Horários de funcionamento (TextField).
   - Links: Rota do Google Maps (para botão "Traçar Rota") e URL do Iframe do Mapa (para embutir no site).
   - Booleano `is_matriz` (Apenas uma pode ser matriz, usar no `save()` para garantir exclusividade).
3. Após gerar as migrations (`makemigrations` e `migrate`), **Crie imediatamente a Primeira Unidade (Matriz)** no banco de dados (via `manage.py shell` ou Data Migration) usando os dados coletados na Seção 2. Isso garante que a Home do site (botões de rota, contato e rodapé) funcione sem erros de cara.

### Fase 4: Aplicativo "Core" (Gestão de Conteúdo e Catálogo)
1. Crie o app `core`.
2. Implemente os seguintes modelos relacionais:
   - **Campaign**: Título, subtítulo, status (ativa/inativa), data início/fim.
   - **Banner**: Vinculado a uma Campaign. Imagem Desktop, Imagem Mobile, título, link de redirecionamento, ordem de exibição.
   - **Category**: Nome, slug, ícone (classe do Bootstrap Icons, ex: `bi-tools`).
   - **Product**: Vinculado a uma Category. Nome, slug, descrição, preço, preço promocional, imagem principal, flags booleanas (`is_active`, `is_highlight`).
   - **Testimonial**: Nome do cliente, foto de perfil, texto, cidade, nota de 1 a 5 estrelas.

### Fase 5: O Painel Administrativo (Jazzmin + Custom Dashboard)
1. Ative o `django-jazzmin` no `INSTALLED_APPS` (antes do `django.contrib.admin`).
2. Configure o `JAZZMIN_SETTINGS` no `settings.py` para usar tema dark e o nome da nova empresa.
3. Crie um template customizado para o painel em `templates/admin/index.html` (sobrescrevendo o do Jazzmin).
4. No `index.html`, crie 4 "Stats Cards" no topo usando CSS translúcido (Glassmorphism dark):
   - Produtos Cadastrados (Count total).
   - Produtos em Destaque (Count de `is_highlight=True`).
   - Campanhas Ativas (No ar).
   - Campanhas Inativas (Pausadas).
   *(Crie um arquivo `admin_stats.py` em `templatetags` para injetar esses dados no painel).*

### Fase 6: O Frontend (Design System Isolado)
1. Crie um arquivo `static/css/design_system.css`.
2. Defina as variáveis de cor (CSS Custom Properties `:root`) usando as cores estabelecidas na **Fase 2**.
3. Crie os templates em `templates/core/`:
   - `base.html`: Navbar fixo no topo, footer com links rápidos, e botão flutuante de WhatsApp puxando os dados do modelo `Unidade` (`is_matriz=True`).
   - `home.html`: 
     - Carrossel no topo carregando apenas Banners da **Campaign ativa** (usando a tag `<picture>` para alternar imagem mobile/desktop nativamente).
     - Seção de Diferenciais (Ícones + Texto).
     - Seção "Produtos em Destaque" limitados a 4 ou 8.
     - Seção "Categorias".
     - Seção "Depoimentos".
     - Seção "Nossas Lojas/Unidades" com botão de rotas, WhatsApp e o Iframe do Google Maps embutido (exigindo `title=` no iframe para acessibilidade).
   - `products.html`: Catálogo completo com paginação e filtro por categoria.
   - `product_detail.html`: Página isolada de um produto com botão "Orçar via WhatsApp".

### Fase 7: Auditoria Final (A11y e Lighthouse 100/100)
1. Todo o HTML gerado deve seguir semântica rigorosa (Hierarquia perfeita: H1 -> H2 -> H3, sem pular níveis).
2. Todo link e botão deve ter contraste WCAG AA+ em relação ao seu fundo.
3. Botões isolados no mobile devem ter área de clique (`target-size`) de no mínimo 48x48px (inclusive dots de carrossel).
4. Imagens devem usar `loading="lazy"`, exceto os banners do carrossel que devem usar `loading="eager"` na primeira foto.

---

## 📝 Resumo do Processo
Ao aplicar este documento em um novo prompt, você garante que o novo sistema herdará **toda a performance técnica, SEO, acessibilidade, escalabilidade de banco em cloud e facilidade de gestão do admin**, personalizando apenas a maquiagem estética para o novo cliente!
