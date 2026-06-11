"""
Django settings - Madereira São Luiz
Utiliza Supabase para banco de dados (PostgreSQL) e Storage (S3-compatible).
"""

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# ────────────────────────────────────────────────────────────────────────────
# Paths & Env
# ────────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# ────────────────────────────────────────────────────────────────────────────
# Security
# ────────────────────────────────────────────────────────────────────────────
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-fallback-key-dev")
DEBUG = os.environ.get("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# CSRF — obrigatório em produção com HTTPS ou proxy reverso (nginx, Cloudflare, etc.)
# Liste todos os domínios/subdomínios que servem o site, incluindo o protocolo.
# Ex.: CSRF_TRUSTED_ORIGINS=https://madeireiro1360.com.br,https://www.madeireiro1360.com.br
_csrf_origins_env = os.environ.get("CSRF_TRUSTED_ORIGINS", "")
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf_origins_env.split(",") if o.strip()]

# Segurança de cookies — ative em produção (HTTPS obrigatório)
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", "False") == "True"
SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "False") == "True"

# Necessário quando há proxy reverso que termina o TLS (nginx, Cloudflare, etc.)
# Informa ao Django que a requisição chegou via HTTPS mesmo que internamente seja HTTP
if os.environ.get("TRUST_PROXY_SSL", "False") == "True":
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ────────────────────────────────────────────────────────────────────────────
# Installed Apps
# ────────────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    # Jazzmin DEVE ser o primeiro para sobrescrever o admin padrão
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    # Terceiros
    "storages",
    # Apps locais
    "core",
    "empresa",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "empresa.context_processors.empresa_context",
                "core.context_processors.global_categories",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ────────────────────────────────────────────────────────────────────────────
# Database — Supabase PostgreSQL via dj_database_url
# ────────────────────────────────────────────────────────────────────────────
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# ────────────────────────────────────────────────────────────────────────────
# Storage — Supabase Storage (S3-compatible) via django-storages
# Defina USE_SUPABASE_STORAGE=True no .env para ativar em produção
# ────────────────────────────────────────────────────────────────────────────
USE_SUPABASE_STORAGE = os.environ.get("USE_SUPABASE_STORAGE", "False") == "True"

if USE_SUPABASE_STORAGE:
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
    BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "madeireira-sao-luiz")
    
    # Constrói o custom_domain para gerar URLs públicas limpas do Supabase
    # Ex: cgoyqzedyqpzrdijtwxa.supabase.co/storage/v1/object/public/madeireira-sao-luiz
    _custom_domain = f"{SUPABASE_URL.replace('https://', '').replace('http://', '')}/storage/v1/object/public/{BUCKET_NAME}" if SUPABASE_URL else None

    # Backend S3 para Supabase Storage
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
                "secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
                "bucket_name": BUCKET_NAME,
                "endpoint_url": os.environ.get("AWS_S3_ENDPOINT_URL", "").rstrip("/").replace(".storage.supabase.co", ".supabase.co"),
                "region_name": os.environ.get("AWS_S3_REGION_NAME", "sa-east-1"),
                "file_overwrite": False,
                "default_acl": None,
                "custom_domain": _custom_domain,
                "querystring_auth": False,
                "url_protocol": "https:",
                "signature_version": "s3v4",
                "addressing_style": "path",
            },
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    # URL pública das mídias no Supabase Storage
    MEDIA_URL = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/"
    MEDIA_ROOT = ""  # Sem armazenamento local quando usando Supabase
else:
    # Armazenamento local para desenvolvimento
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"

# ────────────────────────────────────────────────────────────────────────────
# Static Files
# ────────────────────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ────────────────────────────────────────────────────────────────────────────
# Auth Password Validators
# ────────────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ────────────────────────────────────────────────────────────────────────────
# Internationalization
# ────────────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ────────────────────────────────────────────────────────────────────────────
# Django Jazzmin — Painel Admin Tema Dark
# ────────────────────────────────────────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "Madereira São Luiz",
    "site_header": "Madereira São Luiz",
    "site_brand": "🪵 São Luiz",
    "site_logo": None,
    "login_logo": None,
    "welcome_sign": "Bem-vindo ao Painel Administrativo",
    "copyright": "Madereira São Luiz © 2025",
    "search_model": ["auth.User"],
    "topmenu_links": [
        {"name": "Ver Site", "url": "/", "new_window": True, "icon": "fas fa-eye"},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.Banner": "fas fa-images",
        "core.Testimonial": "fas fa-star",
        "core.Product": "fas fa-box",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
    },
    "language_chooser": False,
    "custom_css": "css/admin_custom.css",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-warning",
    "accent": "accent-warning",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
