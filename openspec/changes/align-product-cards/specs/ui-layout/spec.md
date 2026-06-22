## ADDED Requirements

### Requirement: Alinhamento de Base em Cards
O contêiner do rodapé (`.product-card__footer`) que aloja o preço e o botão de ação DEVE posicionar-se sempre na borda inferior do card (`.product-card`), independente do conteúdo ou comprimento do texto acima dele.

#### Scenario: Card com título curto
- **WHEN** o título do produto possui apenas 1 linha e a descrição está oculta
- **THEN** o rodapé é deslocado e pinado no final da altura total do card

#### Scenario: Card com título longo
- **WHEN** o título do produto quebra para 2 ou mais linhas
- **THEN** o rodapé permanece na mesma linha de base dos outros cards vizinhos, empurrado de forma fluida pelo motor do Flexbox
