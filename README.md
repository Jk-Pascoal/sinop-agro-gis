# 🌱 Sinop Agro-GIS

## 📊 Ficha Técnica do Projeto
* **Município:** Sinop-MT (Código IBGE: 5107909)
* **Área Territorial:** 3.990,3 km² / 399.086 ha
* **Série Analisada (Uso do Solo):** 2000–2024
* **Produção Agrícola:** IBGE/SIDRA PAM 2010–2023
* **Fonte do Uso do Solo:** MapBiomas Collection 10.1 (Resolução: 30 m)
* **Projeção Cartográfica:** SIRGAS 2000 / UTM 21S (EPSG:31981)
* **Stack Principal:** Python 3.12, pandas, GeoPandas, Shapely, Plotly, Folium, Matplotlib, QGIS, MapBiomas Collection 10.1, IBGE/SIDRA, OpenStreetMap via Geofabrik, GitHub Pages
* **Status do Projeto:** Fases 1–7 concluídas; Fase 8 e Fase 9 planejadas.

---

## 🎯 Problema de Negócio
Como a expansão agrícola alterou o território de Sinop-MT entre 2000 e 2024, quais gargalos logísticos aparecem nesse processo e como dados geoespaciais podem apoiar decisões de produção, infraestrutura, sustentabilidade e planejamento territorial?

---

## 📝 Sumário Executivo
Em 24 anos, Sinop-MT consolidou uma transição territorial marcada pela substituição de floresta por soja. Em 2024, a soja ocupa 42,6% do território municipal, enquanto a floresta remanescente representa 36,2%. A correlação de Pearson entre floresta e soja é de -0,984, indicando uma dinâmica quase espelhada entre retração florestal e expansão agrícola. A análise logística também revela 1.842 km de malha viária mapeada, com forte dependência de estradas de terra, criando oportunidades para análises de rede, custo de escoamento e priorização de infraestrutura.

---

## 🏆 Principais Insights
* **Soja no território em 2024:** 42,6% (169.852 ha).
* **Floresta remanescente em 2024:** 36,2% (129.179 ha).
* **Correlação floresta × soja:** -0,984 (relação espelhada).
* **Floresta perdeu 114.321 ha** entre 2000 e 2024.
* **Soja cresceu 137.852 ha** entre 2000 e 2024.
* **Malha viária mapeada:** 1.842 km.
* **6.394 segmentos de via** identificados.
* **63,9 km da BR-163** dentro do município.
* **66,7% das vias** são estradas de terra.
* O milho safrinha cresce na mesma terra da soja após a primeira colheita, explicando a aparente diferença entre área mapeada e produção.

---

## ⚙️ Metodologia
A análise foi executada de acordo com as seguintes etapas estruturadas:
1. **Coleta dos dados públicos:**
   * MapBiomas Collection 10.1.
   * IBGE/SIDRA PAM.
   * IBGE Malha Municipal.
   * OpenStreetMap via Geofabrik.
2. **Recorte espacial:**
   * Limite municipal de Sinop-MT.
   * CRS SIRGAS 2000 / UTM 21S (EPSG:31981).
3. **Tratamento e classificação:**
   * Agrupamento das classes de uso do solo.
   * Cálculo de área por classe.
   * Série temporal 2000–2024.
4. **Análise estatística:**
   * Evolução floresta × soja.
   * Correlação de Pearson.
   * Proporção soja/floresta.
5. **Integração agroprodutiva:**
   * Área plantada.
   * Produção.
   * Produtividade.
   * Interpretação da safrinha.
6. **Análise logística:**
   * Malha viária.
   * Densidade de vias.
   * BR-163.
   * Segmentos e classificação das estradas.
7. **Visualização:**
   * Gráficos interativos (Plotly).
   * Mapa interativo (Folium).
   * Dashboard web publicado no GitHub Pages.

---

## 💡 Decisões que este projeto pode apoiar
* Planejamento logístico de escoamento agrícola.
* Priorização de infraestrutura viária.
* Monitoramento de expansão agrícola.
* Análise de pressão sobre áreas florestais remanescentes.
* Avaliação de risco logístico em estradas de terra.
* Planejamento territorial orientado por dados.
* Construção futura de modelos preditivos e prescritivos.

---

## 🛠️ Skills demonstradas
* Data Science aplicada a território real.
* Análise exploratória de dados.
* Geoprocessamento com Python.
* Manipulação de dados geoespaciais com GeoPandas e Shapely.
* Visualização de dados com Plotly, Matplotlib e Folium.
* Estatística aplicada com correlação temporal.
* Análise de dados públicos.
* GIS aplicado ao agronegócio.
* Storytelling analítico.
* Deploy de projeto em GitHub Pages.
* Pensamento de produto analítico.

---

## ⚠️ Limitações
* **Correlação não implica causalidade:** A correlação negativa de Pearson entre soja e floresta descreve a dinâmica de substituição de cobertura, mas a causalidade depende de fatores históricos e socioeconômicos.
* **Resolução espacial:** A resolução de 30 m do MapBiomas Collection 10.1 pode suavizar pequenas feições territoriais.
* **Classificação de pixels dominantes:** A classe dominante de uso em cada pixel de 30 m pode ocultar usos secundários, como no caso da safrinha (onde a soja é classificada como cultura primária anual).
* **Completude viária:** A malha viária do OpenStreetMap via Geofabrik depende de mapeamento comunitário e pode apresentar incompletudes regionais.
* **Fontes externas:** Os dados de produção agrícola dependem da disponibilidade e atualização do IBGE/SIDRA.
* **Escopo do projeto:** O projeto é uma análise de portfólio e não substitui estudos técnicos oficiais de licenciamento, fiscalização ou planejamento governamental.

---

## 🔮 Próximas Fases
* **Fase 8 — Rede Logística:**
  * Criar grafo viário com NetworkX.
  * Calcular rotas ótimas até a BR-163.
  * Criar mapa de fricção logística.
  * Identificar zonas produtivas mais dependentes de estradas de terra.
  * Criar índice de vulnerabilidade logística.
* **Fase 9 — Modelo Preditivo:**
  * Projetar expansão da soja até 2030.
  * Projetar perda florestal até 2030.
  * Usar intervalos de confiança.
  * Declarar limitações do modelo.
  * Comparar cenários conservador, tendência e acelerado.

---

## 🗂️ Estrutura do Repositório
```
sinop-agro-gis/
├── assets/                 # Imagens e recursos visuais para documentação
├── data/                   # Armazenamento estruturado de dados
│   ├── raw/                # Arquivos brutos (MapBiomas rasters, planilhas IBGE)
│   ├── processed/          # Arquivos processados (recortes consolidados, tabelas finais)
│   └── external/           # Dados de referência geográfica (shapes de limites e malhas viárias)
├── docs/                   # Documentação detalhada do projeto
│   ├── methodology.md      # Metodologia de análise e workflow de dados
│   ├── data_dictionary.md  # Dicionário de variáveis e campos estruturados
│   ├── reproducibility.md  # Instruções para ambiente virtual e execução de notebooks
│   └── limitations.md      # Limitações técnicas e inconsistências metodológicas
├── maps/
│   └── exportados/         # Mapas cartográficos e gráficos de alta resolução (PNG)
├── notebooks/              # Jupyter Notebooks ordenados de processamento a modelagem
├── qgis_project/
│   └── Projeto-SINOP.qgz   # Arquivo de projeto integrado do QGIS
├── scripts/                # Scripts Python utilitários para automação e extração
├── index.html              # Dashboard dinâmico em Vanilla JS e Chart.js
├── requirements.txt        # Dependências de bibliotecas de análise e GIS
└── .gitignore              # Configurações de versionamento Git
```

---

## 🚀 Como Executar

### 1. Preparar o Ambiente
Crie um ambiente virtual e instale as dependências:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Recuperar ou Baixar os Dados
Para recuperar as malhas viárias e limites geográficos automáticos:
```powershell
python scripts/download_dados.py
```
*Consulte o guia interativo [scripts/guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) para o download das tabelas de dados agrícolas e rasters do MapBiomas Collection 10.1.*

### 3. Rodar as Análises
Abra o Jupyter e execute os notebooks na ordem numérica:
```powershell
jupyter notebook notebooks/
```

### 4. Abrir no QGIS
Inicie o QGIS e carregue o arquivo de projeto [qgis_project/Projeto-SINOP.qgz](file:///C:/Users/Administrador/Documents/Projeto-SINOP/qgis_project/Projeto-SINOP.qgz).

---

## 👤 Autor
**Jakson Pascoal**
* GitHub: [@Jk-Pascoal](https://github.com/Jk-Pascoal)
* Localização: Sinop-MT, Brasil 🇧🇷

---

## 📄 Licença
Este projeto é disponibilizado sob a licença **MIT**. Os dados utilizados estão vinculados às restrições e termos de uso de suas respectivas instituições fornecedoras (IBGE/SIDRA, MapBiomas Collection 10.1, OpenStreetMap via Geofabrik).
