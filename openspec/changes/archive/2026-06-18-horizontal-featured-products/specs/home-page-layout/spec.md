## ADDED Requirements

### Requirement: Carrossel Horizontal de Produtos em Destaque
A seção "Produtos em Destaque" SHALL ser renderizada como um contêiner de rolagem horizontal contínua, permitindo que os produtos apareçam lado a lado sem quebrar linhas na página inicial.

#### Scenario: Visualização no Desktop
- **WHEN** o usuário rola a página inicial até a seção de Produtos em Destaque
- **THEN** os cards de produtos aparecem um ao lado do outro, movendo-se lentamente de forma contínua para a esquerda.

### Requirement: Navegação Manual do Carrossel
O usuário SHALL conseguir interagir com o carrossel usando setas de navegação nas laterais para avançar ou recuar os produtos de forma acelerada.

#### Scenario: Clique na Seta Esquerda
- **WHEN** o usuário clica na seta de navegação esquerda
- **THEN** o carrossel de produtos desloca a visualização para a esquerda, exibindo os produtos anteriores.

#### Scenario: Clique na Seta Direita
- **WHEN** o usuário clica na seta de navegação direita
- **THEN** o carrossel de produtos desloca a visualização para a direita, exibindo os próximos produtos.

### Requirement: Layout do Card Otimizado
Os cards dentro do carrossel SHALL possuir uma altura reduzida em relação ao layout padrão de listagem, com as imagens no formato panorâmico e sem a exibição do texto descritivo.

#### Scenario: Cards Renderizados no Carrossel
- **WHEN** os produtos são carregados na seção de Produtos em Destaque
- **THEN** as imagens devem obedecer a um ratio de `16:9` e os parágrafos de descrição não devem ser visíveis.
