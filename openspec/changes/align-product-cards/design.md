## Context

Os cards de produto na home page (`.product-card`) estão desalinhados na base, fazendo com que o preço e o botão "Orçar" fiquem flutuando em alturas variadas, dependendo do tamanho do nome do produto. A estrutura do card utiliza Flexbox (`display: flex; flex-direction: column`) e a descrição possui `flex: 1` para ocupar o espaço extra. Entretanto, no carrossel da home a descrição não é renderizada (`display: none;`), fazendo o rodapé "subir" e colar no título.

## Goals / Non-Goals

**Goals:**
- Alinhar todos os rodapés (preço + botão) perfeitamente na base do card, criando uma linha de botões uniforme no carrossel de produtos da home.

**Non-Goals:**
- Alterar o design ou paleta de cores do componente.
- Restringir ou truncar o nome do produto a uma linha (o texto completo deve permanecer visível).

## Decisions

- **Decisão:** Aplicar a regra CSS `margin-top: auto` à classe `.product-card__footer`.
  - **Justificativa:** É a prática padrão em layouts de coluna Flexbox para "empurrar" um elemento para a base do contêiner flexível. Isso permite que qualquer espaço ocioso provocado pela variação do título fique entre o título e o rodapé. É uma solução limpa (CSS puro) sem custo de performance.
  - **Alternativa Considerada:** Truncar o título do produto com line-clamp. Descartado porque pode esconder informações cruciais sobre as dimensões ou características do produto. Outra alternativa seria usar Javascript para normalizar as alturas, mas isso é anti-padrão (overkill).

## Risks / Trade-offs

- **[Risco] Compatibilidade:** Muito baixo, `margin-top: auto` em flex containers é suportado universalmente em navegadores modernos.
- **[Risco] Impacto em outras páginas:** Nenhum, pois se a descrição (`.product-card__desc`) estiver visível em outra página, ela já faz o preenchimento pelo `flex: 1` e o `margin-top: auto` atuará apenas como uma camada extra de segurança estrutural.
