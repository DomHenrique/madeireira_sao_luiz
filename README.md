# 🪵 Madereira São Luiz — Site Institucional

Site institucional desenvolvido em **Django 6**, com painel administrativo **Jazzmin**, banco de dados **PostgreSQL via Supabase** e imagens gerenciadas pelo **Supabase Storage** (S3-compatible).

---

## 🚀 Setup Local (Desenvolvimento)

### 1. Pré-requisitos
- Python 3.12+
- Git

### 2. Clonar o repositório
```bash
git clone <url-do-repositório>
cd "madereira são luiz"
```

### 3. Criar e ativar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
# ou: venv\Scripts\activate  (Windows)
```

### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

### 6. Aplicar migrations e criar superusuário
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Painel Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## ☁️ Configuração do Supabase (Produção)

### Banco de Dados
1. Crie um projeto no [Supabase](https://supabase.com)
2. Em **Settings → Database**, copie a `Connection string (URI)` no modo `Transaction`
3. Cole em `DATABASE_URL` no seu `.env`

### Storage de Imagens
1. No Supabase, acesse **Storage** e crie um bucket chamado `madereira-sao-luiz`
2. Configure o bucket como **público** para leitura
3. Em **Settings → API**, copie:
   - `Project URL` → `SUPABASE_URL`
   - `anon key` → `SUPABASE_ANON_KEY`
4. Para as credenciais S3 (django-storages), acesse **Settings → Storage** e gere as credenciais S3:
   - `Access Key ID` → `AWS_ACCESS_KEY_ID`
   - `Secret Access Key` → `AWS_SECRET_ACCESS_KEY`
   - `Endpoint` → `AWS_S3_ENDPOINT_URL` (formato: `https://<project-id>.supabase.co/storage/v1/s3`)
5. Defina `USE_SUPABASE_STORAGE=True` no `.env` de produção

---

## 📁 Estrutura do Projeto

```
.
├── config/              # Configurações globais (settings.py, urls.py, wsgi.py)
├── core/                # App principal
│   ├── models.py        # Banner, Testimonial, Category, Product
│   ├── views.py         # home, products
│   ├── admin.py         # Admin configurado com Jazzmin
│   └── urls.py
├── static/
│   └── css/
│       └── design_system.css  # ← Altere aqui para mudar toda a identidade visual
├── templates/
│   ├── base.html        # Layout base (navbar, footer, whatsapp float)
│   └── core/
│       ├── home.html    # Página inicial completa
│       └── products.html # Listagem de produtos
├── media/               # Uploads locais (em desenvolvimento)
├── .env.example         # Template de variáveis de ambiente
├── manage.py
└── requirements.txt
```

---

## 🎨 Design System

O arquivo [`static/css/design_system.css`](static/css/design_system.css) é **isolado** e contém todos os tokens de design (cores, tipografia, espaçamentos). Para alterar a identidade visual, edite apenas este arquivo.

**Paleta principal:**
- 🟡 Âmbar: `#D4820A` (cor primária da marca)
- ⚫ Carvão: `#1A1A2E` (fundo escuro / navbar)
- 🟤 Bege: `#F7F4EF` (fundo claro)

---

## 🛠️ Gerenciamento de Conteúdo

Todo o conteúdo é gerenciado pelo **Painel Administrativo** (django-jazzmin, tema dark):

| Modelo | Função |
|--------|--------|
| **Banner** | Banners do carrossel hero (título, imagem, link, ordem) |
| **Testimonial** | Depoimentos de clientes (foto, estrelas, cidade) |
| **Category** | Categorias de produtos (ícone Bootstrap Icons, slug) |
| **Product** | Produtos com preço, imagem e flags de destaque/promoção |

---

## 🔑 Tecnologias

- **Django 6** + Python 3.12+
- **PostgreSQL** (Supabase)
- **Supabase Storage** via `django-storages` + `boto3` (S3-compatible)
- **django-jazzmin** (painel admin dark)
- **Bootstrap 5.3** + CSS personalizado (sem Tailwind)
- **Pillow** (processamento de imagens)
