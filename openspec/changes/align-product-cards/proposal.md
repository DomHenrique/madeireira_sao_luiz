## Why

Os cards de produtos em destaque na home page (carrossel) estão com os rodapés (preço e botão de orçamento) desalinhados. O problema ocorre porque os títulos dos produtos variam em número de linhas (1 ou 2) e, no modo carrossel, a descrição (que serviria para preencher o espaço como flexível) é escondida (`display: none`). Como não há nenhum elemento com espaço flexível (`flex: 1` ou `margin: auto`) para preencher o vão, o rodapé fica "colado" no título de forma inconsistente em cada card. O alinhamento na base deixará o design muito mais refinado e agradável.

## What Changes

- Adicionar a propriedade `margin-top: auto;` na classe `.product-card__footer` dentro do `style.css`.
- Essa simples modificação Flexbox forçará o contêiner de preços e botões a grudar sempre na parte mais baixa de cada card, mantendo uma linha visual horizontal constante entre todos os cards exibidos, independente de variações textuais acima deles.

## Capabilities

### New Capabilities
- `ui-layout`: Ajustes estruturais e visuais de alinhamento em componentes de tela.

### Modified Capabilities
Nenhuma.

## Impact

- Modificação apenas na classe `.product-card__footer` no arquivo de estilos global: `lp/style.css`.
- Não afetará a estrutura HTML das páginas ou o comportamento interativo, tratando-se estritamente de um ajuste CSS moderno.
