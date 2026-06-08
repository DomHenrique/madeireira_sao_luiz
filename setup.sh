#!/usr/bin/env bash
# ============================================================
# setup.sh — Script de setup automático
# Madereira São Luiz
# Uso: bash setup.sh
# ============================================================

set -e  # Encerra em caso de erro

BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BOLD}🪵  Madereira São Luiz — Setup Automático${NC}"
echo "────────────────────────────────────────────"

# ── 1. Verificar Python 3.12+ ──────────────────────────────
echo -e "\n${YELLOW}[1/6] Verificando versão do Python...${NC}"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED="3.12"
if python3 -c "import sys; exit(0 if sys.version_info >= (3,12) else 1)"; then
  echo -e "${GREEN}✅ Python $PYTHON_VERSION encontrado.${NC}"
else
  echo -e "${RED}❌ Python 3.12+ é necessário. Versão atual: $PYTHON_VERSION${NC}"
  exit 1
fi

# ── 2. Criar e ativar virtualenv ───────────────────────────
echo -e "\n${YELLOW}[2/6] Criando ambiente virtual...${NC}"
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo -e "${GREEN}✅ Virtualenv criado em ./venv${NC}"
else
  echo -e "${GREEN}✅ Virtualenv já existe, pulando criação.${NC}"
fi
source venv/bin/activate

# ── 3. Instalar dependências ───────────────────────────────
echo -e "\n${YELLOW}[3/6] Instalando dependências...${NC}"
pip install -q -r requirements.txt
echo -e "${GREEN}✅ Dependências instaladas.${NC}"

# ── 4. Configurar .env ────────────────────────────────────
echo -e "\n${YELLOW}[4/6] Verificando arquivo .env...${NC}"
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo -e "${RED}⚠️  Arquivo .env criado a partir do .env.example."
  echo -e "    ATENÇÃO: Edite o .env com suas credenciais antes de continuar!${NC}"
  echo ""
  read -p "Pressione ENTER após editar o .env para continuar..."
else
  echo -e "${GREEN}✅ Arquivo .env encontrado.${NC}"
fi

# ── 5. Aplicar migrations ──────────────────────────────────
echo -e "\n${YELLOW}[5/6] Aplicando migrations...${NC}"
python manage.py migrate
echo -e "${GREEN}✅ Banco de dados atualizado.${NC}"

# ── 6. Criar superusuário (opcional) ──────────────────────
echo -e "\n${YELLOW}[6/6] Criar superusuário para o Admin?${NC}"
read -p "Deseja criar um superusuário agora? [s/N]: " CREATE_SUPER
if [[ "$CREATE_SUPER" =~ ^[Ss]$ ]]; then
  python manage.py createsuperuser
fi

# ── Coletar estáticos ──────────────────────────────────────
echo -e "\n${YELLOW}Coletando arquivos estáticos...${NC}"
python manage.py collectstatic --noinput -v 0
echo -e "${GREEN}✅ Estáticos coletados.${NC}"

# ── Resumo ─────────────────────────────────────────────────
echo ""
echo -e "────────────────────────────────────────────"
echo -e "${BOLD}${GREEN}🎉 Setup concluído com sucesso!${NC}"
echo ""
echo -e "Para iniciar o servidor de desenvolvimento:"
echo -e "  ${BOLD}source venv/bin/activate${NC}"
echo -e "  ${BOLD}python manage.py runserver${NC}"
echo ""
echo -e "Painel Admin: ${BOLD}http://127.0.0.1:8000/admin${NC}"
echo -e "────────────────────────────────────────────"
