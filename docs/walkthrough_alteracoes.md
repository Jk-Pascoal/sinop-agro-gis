# Walkthrough — Alterações Realizadas no Sinop Agro-GIS

Este documento resume as implementações realizadas para dinamizar os dados e processar a infraestrutura logística do município de Sinop-MT.

---

## 🛠️ Modificações Realizadas

### 1. 📂 Dinamização de Dados Históricos do IBGE
*   **[producao_ibge.csv](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/producao_agricola/producao_ibge.csv)**: Criado com todos os dados históricos de safras de Soja, Milho e Algodão (2010–2023) retirados do notebook.
*   **[05_producao_ibge_sidra.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/05_producao_ibge_sidra.ipynb)**: Atualizado para ler o CSV criado dinamicamente, eliminando as listas de dados fixas em código.

### 2. 🛣️ Correção de Download da Malha Viária
*   **[download_dados.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/download_dados.py)**: Corrigida a URL do Geofabrik adicionando o termo `-free` para o arquivo compactado das rodovias do Centro-Oeste (`centro-oeste-latest-free.shp.zip`).

### 3. 🗺️ Processamento da Infraestrutura Logística de Sinop
*   **[processa_logistica.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/processa_logistica.py)**: Desenvolvido script de processamento espacial que:
    - Carrega o limite de Sinop (`sinop_recorte.shp`).
    - Lê os shapefiles gerais de rodovias, ferrovias e POIs baixados.
    - Executa o recorte espacial (`gpd.clip`) restrito a Sinop.
    - Filtra silos e armazéns agrícolas de grandes tradings (Cargill, Bunge, Amaggi, LDC, ADM, etc.) usando busca textual em nomes e categorias.
    - Exporta camadas limpas para `data/malha_viaria/`.

### 4. ⚙️ Script de Coordenação em Segundo Plano
*   **[wait_and_process.py](file:///C:/Users/Administrador/.gemini/antigravity-cli/scratch/wait_and_process.py)**: Script em segundo plano que aguarda a conclusão do download do arquivo de 478MB realizado pelo `curl.exe`, realiza a extração do ZIP e executa automaticamente a extração/filtro espacial das camadas de Sinop.

---

## 🔬 Verificação e Validação (Fase 1)

- **Notebook de Produção**: Pronto para uso. A leitura do CSV agora carrega e plota os gráficos perfeitamente com os dados originais.
- **Download e Processamento Logístico**: As tarefas de download e processamento de infraestrutura logística foram **concluídas com sucesso** e validadas!
- **Resultado das Camadas (data/malha_viaria/)**:
  - `sinop_rodovias.shp`: Gerado com sucesso (1.09 MB, contendo 6.394 segmentos de vias recortados no limite territorial de Sinop).
  - `sinop_ferrovias.shp`: Criado (vazio/100 bytes, uma vez que não há ferrovias cruzando o território municipal de Sinop).
  - `sinop_silos.shp`: Não gerado, pois nenhum ponto no dataset público de POIs do Geofabrik atendeu aos filtros semânticos de armazenagem/silos em Sinop.
- **Limpeza de Espaço**: O ZIP de 456 MB e todos os shapefiles brutos extraídos regionalmente (cerca de 2 GB) foram limpos com sucesso, mantendo o tamanho do projeto leve e dentro das diretrizes de armazenamento do notebook.

---

## 🛠️ Modificações Realizadas (Fase 2)

### 1. 📂 Notebook de Análise Temporal Integrada
*   **[06_analise_temporal.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/06_analise_temporal.ipynb)**: Criado notebook para correlacionar a evolução física (MapBiomas) e estatística (IBGE PAM).
*   **[generate_notebook_06.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/generate_notebook_06.py)**: Script gerador programático usando nbformat.

### 2. 📈 Geração e Exportação de Novos Gráficos
*   `13_analise_temporal_integrada.png`: Gráfico de dois eixos confrontando o desmatamento físico e o aumento da produção de soja.
*   `14_produtividade_historica.png`: Gráfico detalhando a produtividade de soja e milho (t/ha) entre 2010 e 2023.

---

## 🔬 Verificação e Validação (Fase 2)

- **Evolução Temporal 2000–2024 (MapBiomas)**:
  - Perda de Floresta: -114.321 ha (-46,95%).
  - Expansão de Soja: +137.852 ha (+430,79%).
  - Correlação: Pearson de **-0,9841** comprovando transição direta.
- **Crescimento de Produtividade (IBGE)**:
  - Soja: ~3.17 t/ha e Milho: ~7.0 t/ha, indicando intensificação agrícola ao invés de desmatamento contínuo.

---

## 🛠️ Modificações Realizadas (Fase 3)

### 1. 📂 Notebook de Análise da Malha Viária
*   **[07_logistica_infraestrutura.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/07_logistica_infraestrutura.ipynb)**: Criado notebook para calcular as métricas espaciais e gerar a representação cartográfica da malha viária de Sinop.
*   **[generate_notebook_07.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/generate_notebook_07.py)**: Script gerador programático para o notebook 07.

### 2. 🗺️ Geração e Exportação do Mapa Viário
*   `15_malha_viaria_sinop.png`: Mapa temático da malha viária de Sinop-MT, destacando a rodovia federal BR-163 (eixo principal) e as estaduais/locais sobre um canvas escuro estruturado.

---

## 🔬 Verificação e Validação (Fase 3)

- **Métricas Logísticas Calculadas**:
  - Extensão total da malha viária: **1.842,15 km** de estradas.
  - Densidade viária: **0,462 km/km²** (km de vias por km² de área).
  - Extensão da BR-163: **63,85 km** cruzando o território municipal.
- **Estruturação por Classe**:
  - *Track* (estradas de terra): **1.228,15 km (66,7%)** — confirmando a grande infraestrutura rural secundária de acesso às fazendas.
  - *Residential* (vias urbanas): **348,65 km (18,9%)**.
  - *Rodovias de Conexão (Secondary/Tertiary):* **85,50 km (4,6%)**.
  - *Eixo Federal de Escoamento (Trunk/Primary):* **72,82 km (4,0%)**.

---

## 🛠️ Modificações Realizadas (Fase 4)

### 1. 📂 Publicação do Mapa Interativo no GitHub Pages
*   **[index.html](file:///C:/Users/Administrador/Documents/Projeto-SINOP/index.html)**: Criada cópia do mapa interativo Folium na raiz do projeto para publicação automática via GitHub Pages.

---

## 🔬 Verificação e Validação (Fase 4)

- **Hospedagem Web**: O mapa interativo passa a ser publicado no GitHub Pages a partir da branch `main` e da pasta `/ (root)`.

