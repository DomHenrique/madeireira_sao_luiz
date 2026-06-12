# 🪵 Madereira São Luiz — Site Institucional

Site institucional de alto desempenho desenvolvido em **Django 6**, com painel administrativo **Jazzmin**, banco de dados **PostgreSQL via Supabase** e imagens gerenciadas pelo **Supabase Storage** (S3-compatible).

O sistema conta com um poderoso **Sistema de Campanhas**, gestão de produtos, responsividade nativa e nota 100/100 no Lighthouse.

---

## ✨ Novidades e Funcionalidades

- **Sistema de Campanhas e Banners Inteligentes**: 
  - Crie campanhas (ex: "Mês dos Namorados", "Black Friday") para customizar a página inicial com seus próprios banners, título e descrição.
  - Suporte a **Imagens Mobile Específicas** nos banners, poupando banda e melhorando a UX no celular (tag `<picture>`).
- **Dashboard Customizado (Admin)**: Acompanhe métricas rápidas pelo painel (Total de Produtos, Campanhas Ativas, Campanhas Pausadas e Produtos em Destaque).
- **Múltiplas Unidades (Filiais)**: Gestão de múltiplos endereços físicos, com geração de rotas automáticas, horários de funcionamento, Google Maps e botões diretos para WhatsApp.
- **Acessibilidade e Performance (Lighthouse 100/100/100)**: Interface otimizada com excelente contraste de cores, ordem de cabeçalhos semântica e suporte total a leitores de tela e dispositivos móveis.
- **Design System Isolado**: Cores, tipografia e espaçamentos padronizados em um único arquivo `design_system.css` para fácil manutenção e *rebranding*.

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
# Edite o arquivo .env com suas credenciais do PostgreSQL
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
├── core/                # App principal de produtos e conteúdo
│   ├── models.py        # Campaign, Banner, Testimonial, Category, Product
│   ├── views.py         # home, products, product_detail
│   └── admin.py         # Admin configurado com Jazzmin e Dashboards Custom
├── empresa/             # App institucional
│   └── models.py        # Unidade (Lojas físicas, endereços e WhatsApp)
├── static/
│   └── css/
│       ├── design_system.css  # ← Design System principal
│       └── admin_custom.css   # ← Estilos do Dashboard Jazzmin
├── templates/
│   ├── base.html        # Layout base (navbar, footer, whatsapp float)
│   ├── core/            # Templates das páginas (home, products)
│   └── admin/           # Dashboard e widgets customizados do painel
├── media/               # Uploads locais (em desenvolvimento)
├── .env.example         # Template de variáveis de ambiente
├── manage.py
└── requirements.txt
```

---

## 🎨 Design System

O arquivo [`static/css/design_system.css`](static/css/design_system.css) é **isolado** e contém todos os tokens de design (cores, tipografia, espaçamentos). Para alterar a identidade visual, edite apenas este arquivo. O sistema baseia-se em cores fortes focadas na marca.

---

## 🛠️ Gerenciamento de Conteúdo

Todo o conteúdo é gerenciado pelo **Painel Administrativo** (django-jazzmin, tema dark, com estatísticas ativas). O painel é composto pelos seguintes modelos:

| Modelo | Módulo | Função |
|--------|--------|--------|
| **Campaign** | Core | Campanhas promocionais que ativam/desativam seções e cores da Home. |
| **Banner** | Core | Banners do carrossel vinculados à campanhas (suporta imagem Mobile e Desktop). |
| **Product** | Core | Produtos com preço, imagem e flags de destaque/promoção e página de detalhes. |
| **Category** | Core | Categorias de produtos com ícones do Bootstrap. |
| **Testimonial** | Core | Depoimentos com suporte a foto de perfil e nota de estrelas. |
| **Unidade** | Empresa | Cadastro das Lojas físicas com link para mapa e WhatsApp com mensagem. |

---

## 🔑 Tecnologias

- **Django 6** + Python 3.12+
- **PostgreSQL** (via Supabase)
- **Supabase Storage** (S3-compatible) via `django-storages` + `boto3`
- **django-jazzmin** (painel admin customizado e dark mode safe)
- **Bootstrap 5.3** + CSS Responsivo Customizado (Acessibilidade 100/100)
- **Playwright** (Automação de testes e auditorias local)
- **Pillow** (processamento de imagens em Python)
