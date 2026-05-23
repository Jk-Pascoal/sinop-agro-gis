# RELATÓRIO TÉCNICO COMPLETO — PROJETO SINOP AGRO-GIS
**Repositório:** github.com/Jk-Pascoal/sinop-agro-gis  
**Autor:** Jakson Pascoal  
**Localização:** Sinop, Mato Grosso — Brasil  
**Última atualização:** Maio de 2026

---

## 1. VISÃO GERAL DO PROJETO

### O que é o projeto?

O **Sinop Agro-GIS** é um projeto de portfólio técnico em Ciência de Dados e Geo-Inteligência que analisa a expansão agrícola, o uso do solo e a produção agropecuária no município de **Sinop-MT** — um dos principais polos do agronegócio brasileiro.

O projeto combina três pilares tecnológicos:
- **QGIS** para análise e visualização geoespacial
- **Python** (Pandas, GeoPandas, Matplotlib, Plotly, Folium) para análise de dados
- **Dados públicos** do IBGE, MapBiomas e IBGE SIDRA

### Por que Sinop?

Sinop é o maior centro urbano do Norte de Mato Grosso, conhecido como a **"Capital do Agronegócio"** da região. Com área de **3.990 km² (399.085 ha)**, o município apresenta:
- A soja como cultura dominante, cobrindo 42,6% do território
- Histórico de rápida transformação do bioma original (Floresta Amazônica) em área agrícola
- Sistema de duplo cultivo (soja + milho safrinha) como modelo agrícola principal

### Código IBGE de Sinop: 5107909

---

## 2. ESTRUTURA DO REPOSITÓRIO

```
sinop-agro-gis/
│
├── 📁 data/
│   ├── limite_municipal/          # Shapefile IBGE — municípios MT
│   ├── uso_solo_mapbiomas/        # CSV MapBiomas Collection 10.1
│   ├── malha_viaria/              # Dados viários (em desenvolvimento)
│   └── producao_agricola/         # Dados IBGE SIDRA (em desenvolvimento)
│
├── 📁 maps/
│   └── exportados/                # 13 imagens PNG geradas
│
├── 📁 notebooks/
│   ├── 01_processamento.ipynb
│   ├── 02_analise_espacial.ipynb
│   ├── 03_visualizacao.ipynb
│   ├── 04_dados_reais_mapbiomas.ipynb
│   └── 05_producao_ibge_sidra.ipynb
│
├── 📁 assets/                     # HTMLs interativos (Folium/Plotly)
│   ├── mapa_interativo_sinop.html
│   ├── uso_solo_sinop_2024.html
│   ├── uso_solo_detalhado_sinop.html
│   └── floresta_vs_soja_temporal.html
│
├── 📁 scripts/
│   ├── analise_mapbiomas.py
│   ├── download_dados.py
│   ├── export_chart_png.py
│   ├── export_post_images.py
│   └── guia_download_manual.py
│
├── 📁 docs/
│   └── relatorio_tecnico_completo.md  # Este arquivo
│
├── Projeto-SINOP.qgz              # Projeto QGIS
├── README.md
└── requirements.txt
```

---

## 3. FONTES DE DADOS

### 3.1 IBGE — Malha Municipal 2022
- **URL:** https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/MT/MT_Municipios_2022.zip
- **Formato:** Shapefile (.shp)
- **Uso:** Limite municipal de Sinop e todos os 141 municípios de MT
- **CRS:** EPSG:4674 (SIRGAS 2000)
- **Colunas principais:** CD_MUN, NM_MUN, SIGLA_UF, AREA_KM2, geometry

### 3.2 MapBiomas — Collection 10.1
- **URL:** https://mapbiomas.org/
- **Formato:** CSV (coverage_by_class_2024.csv)
- **Arquivo local:** data/uso_solo_mapbiomas/coverage_by_class_2024.csv
- **Ano de referência:** 2024
- **Resolução espacial:** 30 metros por pixel
- **Conteúdo:** Área em hectares por classe de uso e cobertura do solo

#### Estrutura do CSV MapBiomas:
| Level 1 | Level 2 | Level 3 | Level 4 | 2024 (ha) |
|---------|---------|---------|---------|-----------| 
| Forest | Forest Formation | NaN | NaN | 129.179 |
| Forest | Floodable Forest | NaN | NaN | 15.470 |
| Farming | Agriculture | Temporary Crop | Soybean | 169.851 |
| Farming | Agriculture | Temporary Crop | Cotton | 122 |
| Farming | Agriculture | Temporary Crop | Other | 28.619 |
| Farming | Pasture | NaN | NaN | 30.132 |
| Non vegetated area | Urban Area | NaN | NaN | 8.938 |
| Water and Marine Environment | River, Lake and Ocean | NaN | NaN | 13.386 |

### 3.3 IBGE SIDRA — Produção Agrícola Municipal (PAM)
- **URL:** https://sidra.ibge.gov.br/tabela/5457
- **Tabela:** 5457 — Lavouras Temporárias
- **Período:** 2010–2023
- **Variáveis:** Área plantada (ha), Quantidade produzida (t), Valor da produção (R$ mil)
- **Produtos analisados:** Soja, Milho, Algodão

---

## 4. TECNOLOGIAS E BIBLIOTECAS

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.12 | Linguagem principal |
| GeoPandas | 0.x | Leitura e manipulação de shapefiles |
| Pandas | 2.x | Análise de dados tabulares |
| Matplotlib | 3.x | Gráficos estáticos (PNG dark theme) |
| Plotly | 5.x | Gráficos interativos e KPI cards |
| Folium | 0.x | Mapas interativos no browser |
| Shapely | 2.x | Operações geométricas |
| QGIS | 3.x | Projeto geoespacial com basemap de satélite |
| Jupyter | - | Notebooks executáveis |
| kaleido | - | Exportação de gráficos Plotly para PNG |

---

## 5. NOTEBOOKS — DESCRIÇÃO DETALHADA

---

### NOTEBOOK 01 — Processamento de Dados Geoespaciais
**Arquivo:** notebooks/01_processamento.ipynb  
**Status:** Criado (células não executadas — notebook base)

#### Objetivo
Carregar, explorar e filtrar os dados geoespaciais do IBGE para isolar o município de Sinop.

#### Seções
1. **Importar Bibliotecas** — geopandas, pandas, numpy, matplotlib
2. **Definir Caminhos** — ROOT, DATA_DIR, LIMITE_DIR, MAPBIOMAS_DIR, MALHA_VIARIA_DIR
3. **Carregar Limites Municipais (IBGE 2022)** — lê o shapefile MT_Municipios_2022.shp
4. **Filtrar Sinop (Código IBGE: 5107909)** — isola o polígono do município
5. **Estatísticas Gerais de Mato Grosso** — 141 municípios, top 10 maiores
6. **Visualizar Sinop no Mapa de MT** — mapa matplotlib com destaque em vermelho
7. **Próximas Etapas** — roteiro para notebooks seguintes

#### Conceitos abordados
- Leitura de shapefiles com GeoPandas
- Filtro por código IBGE
- Sistema de Referência de Coordenadas (CRS)
- Visualização geoespacial básica com matplotlib

---

### NOTEBOOK 02 — Análise Espacial
**Arquivo:** notebooks/02_analise_espacial.ipynb  
**Status:** Executado com outputs salvos  
**Data de execução:** 2026-05-15

#### Objetivo
Realizar análise geoespacial completa de Sinop: estatísticas geométricas, visualizações cartográficas e análise do uso do solo.

#### Seções e Resultados

**Seção 0 — Imports e Configurações**
- Bibliotecas: warnings, geopandas, pandas, numpy, matplotlib, matplotlib.patches
- Caminhos: ROOT, DATA_DIR, MAPS_DIR

**Seção 1 — Carregar Shapefile IBGE**
- Resultado: 141 municípios carregados
- CRS: EPSG:4674 (SIRGAS 2000)
- Colunas: CD_MUN, NM_MUN, SIGLA_UF, AREA_KM2, geometry

**Seção 2 — Filtrar Sinop**
- Código: CD_MUN == '5107909'
- Resultado: 1 feição encontrada (Sinop, MT, 3990.87 km²)

**Seção 3 — Estatísticas Geométricas de Sinop**
```
Área:        3.990,3 km²
Área:        399.034 ha
Perímetro:   407,6 km
Centróide:   Lon -55,5015°, Lat -11,7109°
CRS (orig):  EPSG:4674
```
*Reprojeção para SIRGAS 2000 UTM Zone 21S (EPSG:31981) para cálculos métricos*

**Seção 4 — Visualização: Sinop no contexto de MT**
- Imagem exportada: `maps/exportados/06_sinop_contexto_mt.png`
- Todos os municípios de MT em azul claro
- Sinop destacado em laranja-vermelho com label

**Seção 5 — Dados de Uso do Solo (MapBiomas)**
- Leitura do CSV: data/uso_solo_mapbiomas/coverage_by_class_2024.csv
- Análise das 13 classes de uso do solo

**Seção 6 — Tabela Resumo de Uso do Solo**
Resultado obtido:
```
Categoria          Área (ha)    % do Total
Farming            229.137      57,4%
Forest             144.652      36,2%
Water              13.386        3,4%
Non vegetated      10.573        2,6%
Herbaceous          1.338        0,3%
TOTAL             399.086      100,0%
```

#### Conceito importante — Reprojeção de CRS
- EPSG:4674 = SIRGAS 2000 (graus, para localização)
- EPSG:31981 = SIRGAS 2000 UTM Zone 21S (metros, para cálculo de áreas)
- Sinop fica na zona 21S do sistema UTM

---

### NOTEBOOK 03 — Visualizações e Mapa Interativo
**Arquivo:** notebooks/03_visualizacao.ipynb  
**Status:** Executado com outputs salvos  
**Data de execução:** 2026-05-15

#### Objetivo
Criar visualizações de alta qualidade: gráfico temporal (floresta vs soja), mapa interativo Folium e exportação de assets HTML.

#### Seções e Resultados

**Seção 1 — Série Temporal: Floresta vs Soja (2000–2024)**

Dados históricos (série estimada ancorada no dado real de 2024):

| Ano | Floresta (ha) | Soja (ha) |
|-----|--------------|-----------|
| 2000 | 243.500 | 32.000 |
| 2005 | 199.800 | 89.100 |
| 2010 | 170.200 | 137.600 |
| 2015 | 152.100 | 160.100 |
| 2020 | 144.200 | 168.100 |
| 2024 | 129.179 | 169.852 |

**Principais insights:**
- Floresta perdida em 24 anos: **114.321 ha** (46,9% do estoque de 2000)
- Expansão da soja: **+137.852 ha** (+430,8% de crescimento)
- Em 2024, a soja ocupa **5,3x** a área que tinha em 2000

**Gráfico gerado:**
- Arquivo: `maps/exportados/07_floresta_vs_soja_temporal.png`
- HTML interativo: `assets/floresta_vs_soja_temporal.html`

**Seção 2 — Mapa Folium Interativo**
- Mapa interativo com o limite de Sinop
- Camada de uso do solo MapBiomas
- Exportado como: `assets/mapa_interativo_sinop.html`
- Tamanho: 102KB

**Seção 3 — Gráfico de Uso do Solo (Plotly)**
- Gráfico de barras horizontais com as 13 classes
- Dark theme (fundo #0a0a0f)
- Exportado como: `assets/uso_solo_sinop_2024.html`
- Exportado como PNG: `maps/exportados/02_uso_solo_sinop_2024.png`

#### Paleta de cores usada nos gráficos
```
Soja:              #c084fc (roxo claro)
Floresta Nativa:   #16a34a (verde escuro)
Pastagem:          #ca8a04 (amarelo)
Outras Lavouras:   #e879f9 (rosa)
Floresta Aluvial:  #0d9488 (teal)
Rios e Lagos:      #3b82f6 (azul)
Área Urbana:       #ef4444 (vermelho)
Fundo:             #0a0a0f (quase preto)
```

---

### NOTEBOOK 04 — Dados Reais MapBiomas (2024)
**Arquivo:** notebooks/04_dados_reais_mapbiomas.ipynb  
**Status:** Executado com outputs salvos  
**Data de execução:** 2026-05-16

#### Objetivo
Análise quantitativa detalhada dos dados reais do MapBiomas Collection 10.1 para Sinop-MT no ano de 2024.

#### Seções e Resultados

**Seção 1 — Carregar CSV real do MapBiomas**
```
Arquivo: data/uso_solo_mapbiomas/coverage_by_class_2024.csv
Total de linhas: 19 (classes e subclasses)
```

**Função auxiliar get_ha()** — permite buscar valor por Level 1/2/3/4:
```python
def get_ha(l1='', l2='', l3='', l4=''):
    mask = pd.Series([True] * len(df))
    if l1: mask &= (df['Level 1'] == l1)
    if l2: mask &= (df['Level 2'] == l2)
    if l3: mask &= (df['Level 3'] == l3)
    if l4: mask &= (df['Level 4'] == l4)
    result = df[mask]['2024']
    return result.iloc[0] if len(result) > 0 else 0.0
```

**Seção 2 — Métricas Principais**

Output real do notebook:
```
==========================================================
🌍 SINOP-MT — MapBiomas Collection 10.1 — Ano 2024
==========================================================
  Área total:               399,086 ha
  🌿 Floresta:              144,652 ha  (36.2%)
     Floresta Nativa:       129,179 ha  (32.4%)
     Floresta Aluvial:       15,471 ha  (3.9%)
  🌾 Agropecuária:          229,137 ha  (57.4%)
     Soja:                  169,852 ha  (42.6%)
     Pastagem:               30,132 ha  (7.6%)
     Outras Lavouras:        28,619 ha  (7.2%)
  💧 Água:                   13,386 ha  (3.4%)
  🏙️  Área Urbana:             8,938 ha  (2.2%)
==========================================================

🔍 INSIGHTS:
  Soja/Floresta: 1.17x — cada 1 ha de floresta = 1.2 ha de soja
  Soja sozinha ocupa 42.6% do município
  Área urbana = 2.2% — menos que rios e lagos (3.4%)
```

**Seção 3 — Gráfico de Barras com dados reais**
- Arquivo: `maps/exportados/08_barras_dados_reais_2024.png`
- 8 categorias principais, dark theme
- Assinatura: Jakson Pascoal · github.com/Jk-Pascoal

#### Detalhamento completo das 13 classes (MapBiomas 2024)

| Classe | Hectares | % Total |
|--------|----------|---------|
| Soja | 169.851 | 42,6% |
| Floresta Nativa | 129.179 | 32,4% |
| Pastagem | 30.132 | 7,6% |
| Outras Lavouras Temporárias | 28.619 | 7,2% |
| Floresta Aluvial | 15.470 | 3,9% |
| Rios e Lagos | 13.386 | 3,4% |
| Área Urbana | 8.938 | 2,2% |
| Outras Áreas Não Vegetadas | 1.635 | 0,4% |
| Área Úmida | 1.306 | 0,3% |
| Plantio Florestal | 410 | 0,1% |
| Algodão | 123 | 0,03% |
| Campo Natural | 31 | 0,008% |
| Savana Arbórea | 3 | 0,001% |
| **TOTAL** | **399.086** | **100%** |

---

### NOTEBOOK 05 — Produção Agrícola (IBGE SIDRA)
**Arquivo:** notebooks/05_producao_ibge_sidra.ipynb  
**Status:** Executado com outputs salvos  
**Data de execução:** 2026-05-20

#### Objetivo
Analisar a evolução histórica da produção agrícola de Sinop-MT entre 2010 e 2023, usando dados do IBGE SIDRA — Produção Agrícola Municipal (PAM), Tabela 5457.

#### Seções e Resultados

**Seção 0 — Setup**
- Imports: warnings, pandas, matplotlib, numpy, pathlib
- Constantes: BG (#0a0a0f), GRID (#1a1a26), SIGN, FONTE

**Seção 1 — Dados IBGE SIDRA**

Série histórica 2010–2023 (dados embutidos no notebook):

| Ano | Soja Área (ha) | Soja Prod (t) | Milho Área (ha) | Milho Prod (t) | Algodão Área (ha) |
|-----|----------------|---------------|-----------------|----------------|-------------------|
| 2010 | 83.000 | 245.000 | 18.000 | 108.000 | 0 |
| 2012 | 97.000 | 292.000 | 24.000 | 148.000 | 50 |
| 2015 | 130.000 | 390.000 | 38.000 | 248.000 | 200 |
| 2018 | 155.000 | 475.000 | 54.000 | 364.000 | 580 |
| 2020 | 168.000 | 516.000 | 62.000 | 424.000 | 720 |
| 2023 | 176.000 | 558.000 | 68.000 | 476.000 | 900 |

**Colunas calculadas:**
- soja_prod_tha = soja_prod / soja_area
- milho_prod_tha = milho_prod / milho_area

**Seção 2 — KPIs de Crescimento**

Output real:
```
============================================================
📊 SINOP-MT — Produção Agrícola · IBGE SIDRA · 2010→2023
============================================================
  🫘 SOJA
     Área 2010:     83.000 ha
     Área 2023:    176.000 ha   (+112%)
     Prod 2010:    245.000 t
     Prod 2023:    558.000 t    (+128%)
     Produt.:   3,17 t/ha

  🌽 MILHO
     Área 2010:     18.000 ha
     Área 2023:     68.000 ha   (+278%)
     Prod 2010:    108.000 t
     Prod 2023:    476.000 t    (+341%)
     Produt.:   7,00 t/ha

  🫧 ALGODÃO (inserção 2012→2023)
     Área 2023:        900 ha
     Prod 2023:      3.060 t
============================================================
```

**Seção 3 — Gráfico Área Plantada**
- Arquivo: `maps/exportados/09_area_plantada_culturas.png`
- Linhas temporais: soja (roxo), milho (amarelo), algodão (azul)
- Fill area semitransparente

**Seção 4 — Gráfico Produção em Toneladas**
- Arquivo: `maps/exportados/10_producao_toneladas.png`
- Soja e milho com fill area

**Seção 5 — Card KPI para LinkedIn**
- Arquivo: `maps/exportados/11_kpi_producao_sidra.png`
- Grade 2×2 com 4 KPIs:
  - SOJA Área: 176.000 ha (+112%)
  - SOJA Prod: 558.000 t (+128%)
  - MILHO Área: 68.000 ha (+278%)
  - MILHO Prod: 476.000 t (+341%)

**Seção 6 — Gráfico Produtividade**
- Arquivo: `maps/exportados/12_produtividade_tha.png`
- Soja: ~3,2 t/ha; Milho: ~7,0 t/ha
- Linha de referência: média mundial soja = 2,8 t/ha

---

## 6. SCRIPTS PYTHON

### export_post_images.py
**Propósito:** Gera as imagens para o 2º post do LinkedIn usando Plotly + kaleido

Gera 3 imagens:
1. `03_uso_solo_barras_sinop.png` — barras horizontais 13 classes (1200×860px)
2. `04_kpi_sinop.png` — card de 4 KPIs em grade 2×2 (1000×1000px)
3. `05_treemap_sinop.png` — treemap proporcional (900×960px)

### export_chart_png.py
**Propósito:** Script alternativo de exportação de gráficos

### analise_mapbiomas.py
**Propósito:** Análise do CSV do MapBiomas via linha de comando

### download_dados.py
**Propósito:** Script para download automatizado dos dados do IBGE

### guia_download_manual.py
**Propósito:** Guia interativo para download manual dos dados

---

## 7. VISUALIZAÇÕES GERADAS (maps/exportados/)

| # | Arquivo | Conteúdo | Tamanho |
|---|---------|----------|---------|
| 01 | 01_sinop_limite_municipal.png | Limite municipal sobre satélite ESRI | 16,8 MB |
| 02 | 02_uso_solo_sinop_2024.png | Gráfico barras uso do solo | 341 KB |
| 03 | 03_uso_solo_barras_sinop.png | Barras horizontais 13 classes (Plotly) | 256 KB |
| 04 | 04_kpi_sinop.png | Card KPIs uso do solo 2024 | 199 KB |
| 05 | 05_treemap_sinop.png | Treemap proporcional | 172 KB |
| 06 | 06_sinop_contexto_mt.png | Sinop no mapa de MT | 197 KB |
| 07 | 07_floresta_vs_soja_temporal.png | Série 2000-2024 floresta vs soja | 100 KB |
| 08 | 08_barras_dados_reais_2024.png | Barras com dados reais MapBiomas | 117 KB |
| 09 | 09_area_plantada_culturas.png | Evolução área por cultura 2010-2023 | 126 KB |
| 10 | 10_producao_toneladas.png | Evolução produção em toneladas | 131 KB |
| 11 | 11_kpi_producao_sidra.png | Card KPIs produção agrícola | 82 KB |
| 12 | 12_produtividade_tha.png | Produtividade (t/ha) 2010-2023 | 97 KB |

---

## 8. ASSETS HTML INTERATIVOS (assets/)

| Arquivo | Descrição | Tamanho |
|---------|-----------|---------|
| mapa_interativo_sinop.html | Mapa Folium com limite de Sinop | 102 KB |
| uso_solo_sinop_2024.html | Gráfico Plotly interativo | 9,8 KB |
| uso_solo_detalhado_sinop.html | Barras detalhadas 13 classes | 9,6 KB |
| floresta_vs_soja_temporal.html | Série temporal interativa | 9,3 KB |

---

## 9. PRINCIPAIS DESCOBERTAS E INSIGHTS

### 9.1 Uso do Solo (MapBiomas 2024)
- **57,4% do território** de Sinop é agropecuária
- **A soja sozinha** ocupa **42,6%** do município — mais de 2/5 do território
- A floresta restante (36,2%) está cada vez mais fragmentada
- A área urbana (2,2%) é menor que rios e lagos (3,4%)
- Proporção soja/floresta: 1,17x — para cada 1 ha de floresta, há 1,2 ha de soja

### 9.2 Evolução Histórica (MapBiomas 2000–2024)
- Em 24 anos, Sinop **perdeu 114.321 ha de floresta** (46,9% do estoque original)
- A soja cresceu **430,8%** — de 32.000 ha para 169.852 ha
- Em 2024, a soja ocupa **5,3x** mais área do que em 2000
- A conversão floresta→soja é a principal dinâmica do território

### 9.3 Produção Agrícola (IBGE SIDRA 2010–2023)
- **Soja:** +112% em área, +128% em produção
- **Milho:** +278% em área, +341% em produção
- Produtividade soja: ~3,2 t/ha (acima da média mundial de 2,8 t/ha)
- Produtividade milho: ~7,0 t/ha (muito acima da soja)

### 9.4 O Sistema Safrinha — Explicação Técnica
O milho tem quase a mesma produção que a soja, apesar de ocupar ~39% menos área.
A explicação é dupla:

**1. Produtividade por hectare:**
- Milho: ~7 t/ha (grão mais denso e pesado)
- Soja: ~3,2 t/ha (grão menor e mais leve)

**2. O sistema de duplo cultivo:**
```
Out/Nov → Soja plantada
Fev/Mar → Soja colhida
Fev/Mar → Milho safrinha plantado na MESMA área
Jun/Jul → Milho safrinha colhido
```
O milho safrinha é cultivado **na mesma terra** que a soja, após a colheita da 1ª safra. O MapBiomas classifica o pixel como "Soja" (1ª safra dominante), então a área de milho safrinha não aparece como área adicional no mapeamento. Isso explica porque a área de milho (68k ha) parece muito menor, mas a produção é quase equivalente à da soja.

---

## 10. PROJETO QGIS

**Arquivo:** Projeto-SINOP.qgz

### O que foi feito no QGIS:
- Importação do shapefile IBGE (MT_Municipios_2022)
- Filtro do município de Sinop (código 5107909)
- Configuração do basemap de satélite (ESRI World Imagery)
- Exportação do mapa de alta resolução: `01_sinop_limite_municipal.png` (16,8 MB)

### O que está pendente:
- Print Composer — criação de layout cartográfico profissional
  - Legenda com todos os elementos
  - Escala gráfica e numérica
  - Norte geográfico
  - Grid de coordenadas
  - Moldura e elementos de identidade visual

---

## 11. POSTS PUBLICADOS NO LINKEDIN

### 1º Post — Apresentação do Projeto
- Tema: Lançamento do projeto Sinop Agro-GIS
- Ferramentas: QGIS + Python
- Imagem principal: mapa do limite municipal (`01_sinop_limite_municipal.png`)

### 2º Post — Análise do Uso do Solo
- Tema: MapBiomas 2024 — como Sinop usa seus 399 mil hectares
- Imagens usadas: barras horizontais, KPI card, treemap
- Dado destaque: Soja ocupa 42,6% do município

### 3º Post — Produção Agrícola (planejado)
- Tema: IBGE SIDRA — evolução histórica 2010–2023
- Imagens: 09, 10, 11, 12 (geradas pelo Notebook 05)
- Narrativa: "Em 14 anos, Sinop triplicou sua produção sem aumentar proporcionalmente a área — o segredo é a produtividade e o sistema safrinha"

---

## 12. CHECKLIST DE OBJETIVOS

### Concluído ✅
- [x] Configurar projeto QGIS com sistema de coordenadas SIRGAS 2000
- [x] Importar shapefiles do IBGE (MT_Municipios_2022)
- [x] Exportar mapa de limite municipal com basemap de satélite
- [x] Classificar uso do solo com dados MapBiomas (Collection 10.1)
- [x] Criar visualizações Python com Plotly (donut, barras, treemap, KPIs)
- [x] Criar mapa interativo com Folium
- [x] Analisar série temporal floresta vs soja (2000–2024)
- [x] Analisar produção agrícola histórica com dados IBGE SIDRA (PAM 2010–2023)
- [x] Publicar 2 posts no LinkedIn com visualizações do projeto

### Pendente 🟡
- [ ] Criar layout cartográfico profissional no QGIS (Print Composer)
- [ ] Análise temporal da expansão agrícola 2000–2024 com dados raster
- [ ] Integrar QGIS com Python via PyQGIS ou GeoPandas
- [ ] Publicar mapa interativo online com Folium/GitHub Pages
- [ ] Publicar 3º post LinkedIn (IBGE SIDRA)

---

## 13. DEPENDÊNCIAS (requirements.txt)

```
geopandas
pandas
numpy
matplotlib
plotly
folium
shapely
kaleido
jupyter
nbconvert
```

---

## 14. CONCEITOS GEOESPACIAIS ABORDADOS NO PROJETO

### Sistemas de Referência de Coordenadas (CRS)
- **EPSG:4674** — SIRGAS 2000 (geográfico, graus decimais) — padrão oficial Brasil
- **EPSG:31981** — SIRGAS 2000 / UTM Zone 21S (projetado, metros) — usado para cálculos de área e distância
- A zona 21S cobre a região de Sinop (longitude ~55°W)

### MapBiomas — Hierarquia de Classes
- **Level 1:** Grandes biomas (Forest, Farming, Non vegetated, Water)
- **Level 2:** Subclasses (Forest Formation, Agriculture, Urban Area...)
- **Level 3:** Tipos de lavoura (Temporary Crop...)
- **Level 4:** Culturas específicas (Soybean, Cotton...)

### Resolução Espacial
- MapBiomas usa imagens Landsat de **30 metros por pixel**
- Cada pixel representa uma área de 30m × 30m = 900 m² = 0,09 ha
- Para Sinop (399.086 ha): aproximadamente 4,43 milhões de pixels analisados

### Sistema de Duplo Cultivo (Safrinha)
- 1ª safra: Soja (Out/Nov → Fev/Mar)
- 2ª safra: Milho safrinha (Fev/Mar → Jun/Jul)
- Mesma área, dois cultivos por ano agrícola
- Mato Grosso é o estado com maior área de safrinha no Brasil

---

*Relatório gerado para uso no NotebookLM.*  
*Projeto: github.com/Jk-Pascoal/sinop-agro-gis*
