## Context

A Madeireira São Luiz (Matcon) já possui uma Landing Page (`lp/index.html`) que apresenta a empresa, seus diferenciais e um portfólio reduzido de produtos em destaque. Entretanto, essa página possui diversos links para navegação interna e visualização de catálogo, o que pode diluir a atenção de visitantes originados de tráfego pago. Para otimizar o funil de conversão de anúncios, é necessário criar uma versão focada ("Squeeze Page"), onde a única ação possível é o contato via WhatsApp.

## Goals / Non-Goals

**Goals:**
- Criar uma nova LP (`lp/conversao.html` ou equivalente) a partir da base visual e estilística da LP original.
- Remover elementos de distração (Navbar, Footer complexo, Vitrine de Produtos).
- Direcionar todos os links e interações (Botões do Hero, Cards de Categoria, etc.) para o WhatsApp.

**Non-Goals:**
- Não iremos refazer o Design System ou estilos da página; aproveitaremos o `style.css` e o HTML estrutural já existentes.
- Não iremos substituir a página `index.html` padrão, que continua servindo ao tráfego orgânico/institucional.

## Decisions

- **Criação de um novo arquivo HTML:** Criaremos `lp/conversao.html` copiando o conteúdo de `lp/index.html` e limpando as seções indesejadas. Isso evita complexidades no backend (Django) e mantém os arquivos estáticos simples e independentes.
- **Reaproveitamento de Assets:** `style.css`, `script.js` e as imagens já presentes continuarão sendo utilizados para garantir consistência visual.
- **Links Hardcoded para WhatsApp:** Todos os `<a>` que agem como botão receberão o link direto do WhatsApp (mantendo a URL `https://wa.me/...` existente ou adaptando o texto de pré-visualização).

## Risks / Trade-offs

- **[Risco] Duplicação de código HTML:** Manter duas LPs separadas significa que futuras alterações de identidade visual (como logo ou estilos estruturais) precisarão ser feitas nos dois arquivos.
  - **Mitigação:** Como se trata de LPs estáticas, a duplicação é o padrão comum para criar variações de funil sem engessar a arquitetura principal.
