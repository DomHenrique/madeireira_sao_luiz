## ADDED Requirements

### Requirement: Exclusividade de Links para WhatsApp
A página de conversão MUST ter todos os links e botões direcionando unicamente para contatos de WhatsApp, não permitindo links para âncoras locais (exceto se inevitável para UX, mas como não haverá navbar, não deve haver) ou páginas externas.

#### Scenario: Interação com Banner Principal
- **WHEN** o usuário clica em "Fazer Orçamento" ou botões similares no Banner/Hero
- **THEN** o sistema abre o link do WhatsApp (`https://wa.me/...`) para iniciar o atendimento

#### Scenario: Interação com Categorias
- **WHEN** o usuário clica no card de "Madeiras Brutas" ou outra categoria
- **THEN** o sistema abre o link do WhatsApp para a respectiva consulta de categoria

### Requirement: Estrutura Focada
A página de conversão MUST NÃO conter Navbar (menu superior), Footer complexo (rodapé) ou Vitrine de Produtos (carrossel de ofertas).

#### Scenario: Visualização da Página
- **WHEN** o usuário acessa a Squeeze Page (ex: `/lp/conversao.html`)
- **THEN** o sistema não exibe o menu superior nem opções de navegação adicionais
- **THEN** o sistema não exibe o bloco de Produtos em Destaque
- **THEN** o sistema exibe corretamente os blocos de Histórico, Diferenciais, Depoimentos, Marcas e Localização.
