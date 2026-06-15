# Auditoria de Métricas e Divergências — Sinop Agro-GIS

Este documento apresenta o resultado da auditoria de consistência numérica e metodológica entre o [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md), o dashboard [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) e os Jupyter Notebooks do projeto **Sinop Agro-GIS**.

---

## 📊 Tabela de Inconsistências e Divergências de Métricas

| Métrica | Valor Encontrado | Arquivo / Local onde aparece | Observação | Ação Recomendada |
| :--- | :--- | :--- | :--- | :--- |
| **Área de Soja (2024)** | `169.851 ha` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 307)<br>[README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 124) | Valor arredondado para inteiro inferior. | Padronizar para `169.852 ha` ou manter o decimal de precisão. |
| | `169.852 ha` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 340)<br>[06_analise_temporal.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/06_analise_temporal.ipynb) (lin. 107)<br>[03_visualizacao.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/03_visualizacao.ipynb) (lin. 166) | Valor arredondado para o inteiro mais próximo. | Padronizar a exibição para `169.852 ha` para manter uniformidade. |
| | `169.851,83 ha` | [coverage_by_class_2024.csv](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/processed/coverage_by_class_2024.csv) (lin. 23)<br>[04_dados_reais_mapbiomas.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/04_dados_reais_mapbiomas.ipynb) | Valor exato de saída do raster de satélite. | Utilizar este valor como o valor real em notas técnicas de apoio. |
| **Área Total do Município** | `399.085,86 ha` / `399.086 ha` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 37, 40)<br>[README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 152) | Área calculada a partir da soma total dos pixels do raster MapBiomas. | Explicar que a área total do raster difere levemente do vetor oficial. |
| | `399.034 ha` / `3.990,3 km²` | [02_analise_espacial.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/02_analise_espacial.ipynb) (lin. 193-194) | Área do polígono de limites do IBGE 2022 projetado em UTM Zone 21S. | Adotar `3.990,3 km²` como a área territorial oficial. |
| | `399.033,9 ha` / `3.990,34 km²` | [07_logistica_infraestrutura.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/07_logistica_infraestrutura.ipynb) (lin. 150) | Pequena variação decimal por causa do método de arredondamento de ponto flutuante. | Corrigir o print de texto de `07_logistica_infraestrutura.ipynb` para `3.990,3 km²`. |
| **Correlação Soja x Floresta** | `−0,98` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 179) | Valor estático programado no card HTML do dashboard. | Atualizar o card do HTML para `-0,99` (ou `-0,9937`). |
| | `-0.9937` | [06_analise_temporal.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/06_analise_temporal.ipynb) (lin. 185)<br>[generate_notebook_06.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/generate_notebook_06.py) | Valor exato calculado via Pearson (Pandas/NumPy) no notebook. | Utilizar `-0,99` como valor de arredondamento consensual. |
| **Extensão da Malha Viária** | `1.842,15 km` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 153, 403-408)<br>[README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 153) | Quilometragem consolidada no dashboard. Exclui ou oculta vias de serviço/locais. | Explicar o critério de filtragem das vias (excluindo vias locais/serviço). |
| | `3.640,42 km` | [07_logistica_infraestrutura.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/07_logistica_infraestrutura.ipynb) (lin. 151) | Extensão bruta somando todas as categorias espaciais do OSM (ex: residenciais, terciárias, serviço). | Padronizar a malha ou justificar a exclusão de vias secundárias no dashboard. |
| **Extensão da Rodovia BR-163** | `72,82 km` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 407)<br>[README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 160) | Valor no gráfico/tabela viária do dashboard. | Uniformizar o valor da rodovia em todos os pontos. |
| | `63,85 km` | [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 155) | Valor de texto citado no README. | Corrigir a menção textual de 63,85 km para o valor consensual final. |
| | `81,21 km` | [07_logistica_infraestrutura.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/07_logistica_infraestrutura.ipynb) (lin. 227) | Extensão total calculada pelo notebook com base nos links de pista do OSM. | Verificar se há sobreposição ou duplicação de faixas (pista dupla) no cálculo do notebook. |
| **Tabela SIDRA IBGE Citada** | `Tabela 1613` | [data/README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/README.md) (lin. 40)<br>[guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) | Tabela antiga ou alternativa para o Censo Agropecuário/PAM. | Alterar todas as ocorrências para a Tabela 5457. |
| | `Tabela 5457` | [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 131)<br>[generate_notebook_06.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/generate_notebook_06.py) | Tabela correta e atualizada da Produção Agrícola Municipal (PAM). | Adotar como a citação padrão do repositório. |
| **Período de Análise** | `2000–2023` | [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 16)<br>[data/README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/README.md) (lin. 42) | Limitação temporal antiga. | Atualizar o texto para "2000–2024". |
| | `2000–2024` | [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 175, 338)<br>[06_analise_temporal.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/06_analise_temporal.ipynb) | Período de cobertura de solo real alcançado pela Coleção 10.1. | Adotar este intervalo temporal para todos os dados de uso de solo. |

---

## 📌 Decisões Pendentes do Autor

Antes de consolidar o projeto e realizar o commit final na branch `chore/reproducibility-v02`, você (o autor) precisa tomar as seguintes decisões estruturais e conceituais:

### 1. Critério de Extensão Viária (Logística)
* **Contexto:** Há uma diferença enorme entre os **3.640,42 km** calculados no Notebook 07 e os **1.842,15 km** exibidos no dashboard e no README.
* **Sua Decisão:**
  - **Opção A (Recomendada):** Manter o dashboard filtrado (excluindo ruelas residenciais de menor relevância e caminhos de serviço agrícola particulares) e documentar explicitamente no Notebook 07 e no [limitations.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/limitations.md) que a extensão logística principal de escoamento é de ~1.842 km, enquanto a malha geográfica municipal bruta totaliza ~3.640 km.
  - **Opção B:** Atualizar os valores do dashboard e do README para refletir os 3.640,42 km totais calculados no Notebook 07.

### 2. Duplicidade da Extensão da BR-163
* **Contexto:** O Notebook calcula **81,21 km** para a BR-163, enquanto o dashboard lista **72,82 km** e o texto do README cita **63,85 km**. Essa diferença geralmente ocorre porque o OpenStreetMap mapeia trechos duplicados de pistas separadas (rodovia duplicada gera dois segmentos paralelos computados na soma geométrica).
* **Sua Decisão:**
  - **Opção A (Recomendada):** Adotar os **81,21 km** calculados espacialmente pelo notebook (que representa o comprimento total de linhas de rodovia no OSM dentro do polígono) e atualizar o dashboard e o README.
  - **Opção B:** Adotar a extensão do eixo linear simples (que desconsidera a pista dupla paralela), obtendo a distância real de travessia do município (~72,82 km), e filtrar o notebook para contar apenas uma das mãos da via.

### 3. Padronização de Arredondamento da Soja (2024)
* **Contexto:** A área espectral exata da soja medida é de `169.851,83 ha`. Ela aparece escrita como `169.851 ha` ou `169.852 ha`.
* **Sua Decisão:**
  - Definir se utilizaremos a convenção de arredondamento padrão para cima (`169.852 ha` em todas as citações textuais) ou a representação inteira inferior truncada (`169.851 ha`).

### 4. Nomenclatura das Tabelas de Dados
* **Contexto:** O repositório cita ora a Tabela 1613, ora a Tabela 5457 do IBGE/SIDRA.
* **Sua Decisão:**
  - Adotar e padronizar unicamente a citação da **Tabela 5457** (que é a tabela do SIDRA para Lavouras Temporárias - PAM), atualizando o [guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) e o [data/README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/README.md).

---

## 🛠️ Decisões adotadas na consolidação

O projeto foi consolidado aplicando as seguintes diretrizes acordadas pelo autor:

1. **Área de Soja (2024):** Padronizada nos textos principais para **169.852 ha** (arredondamento inteiro padrão) e mantido o valor técnico exato de **169.851,83 ha** em notas metodológicas ou dicionário.
   * *Arquivos atualizados:* [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 307) e [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 28).
2. **Área Total do Município:** Adotada a área político-administrativa de limites oficiais do IBGE de **3.990,3 km²** (vetor) e mantido o valor raster MapBiomas de **399.085,86 ha** nas análises espectrais, justificando a diferença nas limitações metodológicas.
   * *Arquivos atualizados:* [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 33, 139) e [docs/methodology.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/methodology.md) (Seção "Consolidação").
3. **Correlação Soja x Floresta:** Padronizado o coeficiente para **-0,99** nos textos principais e dashboard, mantendo a nota de cálculo exato do Pearson r = -0,9937.
   * *Arquivos atualizados:* [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 179) e [docs/methodology.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/methodology.md).
4. **Malha Viária e BR-163:**
   * Consolidado o total de **1.842,15 km** no dashboard e no README para representar a malha logística principal filtrada.
   * Documentado que os **3.640,42 km** obtidos na análise espacial bruta do Notebook 07 incluem vias urbanas secundárias e acessos de serviço menores.
   * Padronizada a BR-163 como **72,82 km** de travessia do eixo central simplificado, explicando que o valor de **81,21 km** representa o somatório de pistas duplas e marginais mapeadas no OSM.
   * *Arquivos atualizados:* [index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html) (lin. 244, 254), [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 33, 140), [docs/methodology.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/methodology.md) e [docs/limitations.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/limitations.md).
5. **Tabelas SIDRA/IBGE:** Padronizada a citação como **Tabela 5457**, e a Tabela 1613 classificada como referência antiga.
   * *Arquivos atualizados:* [data/README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/README.md) (lin. 40) e [guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) (lin. 48).
6. **Período de Análise:** Padronizado para **2000–2024** para dados de cobertura vegetal (MapBiomas) e mantido **2010–2023** para os dados da lavoura temporária (IBGE PAM), explicitando a diferença de abrangência espectral x tabular nas limitações e metodologia.
   * *Arquivos atualizados:* [README.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/README.md) (lin. 12, 140) e [docs/methodology.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/methodology.md).

