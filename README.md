# 🌱 Sinop Agro-GIS — Análise Espacial da Expansão Agrícola em Mato Grosso

[![QGIS](https://img.shields.io/badge/QGIS-3.x-589632?style=for-the-badge&logo=qgis&logoColor=white)](https://qgis.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-GIS-139C5A?style=for-the-badge)](https://geopandas.org/)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)]()

> **Estudo de caso geoespacial** sobre a expansão agrícola, uso do solo e infraestrutura logística na mesorregião Norte de Mato Grosso, com foco no município de **Sinop-MT** — polo do agronegócio brasileiro.

---

## 📌 Sobre o Projeto

Sinop é o principal centro econômico do Norte de Mato Grosso e um dos municípios com maior produção de soja e milho do Brasil. Este projeto combina ferramentas de **GIS (QGIS)** e **análise de dados em Python** para mapear e analisar:

- 🌾 Evolução do uso do solo agrícola (2000–2023)
- 🌲 Desmatamento x avanço da fronteira agrícola
- 🛣️ Infraestrutura logística: rodovias, ferrovias e silos
- 📊 Produção agrícola por safra (dados IBGE/CONAB)

---

## 🗂️ Estrutura do Repositório

```
sinop-agro-gis/
│
├── 📁 data/
│   ├── limite_municipal/       # Shapefiles IBGE — limites de Sinop e MT
│   ├── uso_solo_mapbiomas/     # Rasters MapBiomas — uso e cobertura do solo
│   ├── malha_viaria/           # Shapefiles DNIT/OSM — rodovias e ferrovias
│   └── producao_agricola/      # CSVs IBGE/CONAB — produção por safra
│
├── 📁 maps/
│   └── exportados/             # Mapas exportados do QGIS (PNG/PDF)
│
├── 📁 notebooks/
│   ├── 01_processamento.ipynb  # Carregamento e limpeza dos dados
│   ├── 02_analise_espacial.ipynb # Análise com GeoPandas
│   └── 03_visualizacao.ipynb   # Mapas interativos com Folium
│
├── 📁 qgis_project/            # Arquivo .qgz do projeto QGIS
│
├── 📁 assets/                  # Imagens e recursos para documentação
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Uso |
|---|---|
| **QGIS 3.x** | Processamento geoespacial, criação de layouts de mapas |
| **Python 3.10+** | Scripts de análise e automação |
| **GeoPandas** | Manipulação de dados vetoriais e rasters |
| **Shapely** | Operações geométricas espaciais |
| **Folium** | Mapas interativos no browser |
| **Plotly** | Visualizações e dashboards |
| **Rasterio** | Processamento de imagens raster (MapBiomas) |

---

## 📦 Fontes de Dados

Todos os dados utilizados são **públicos e gratuitos**:

| Dataset | Fonte | Link |
|---|---|---|
| Limites Municipais | IBGE | [Malha Municipal](https://www.ibge.gov.br/geociencias/downloads-geociencias.html) |
| Uso e Cobertura do Solo | MapBiomas | [mapbiomas.org](https://mapbiomas.org/) |
| Malha Viária Federal | DNIT | [dnit.gov.br](https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/dnit-geo) |
| Produção Agrícola Municipal | IBGE/SIDRA | [sidra.ibge.gov.br](https://sidra.ibge.gov.br/) |
| Imagens de Satélite | Copernicus/Sentinel | [Copernicus Browser](https://browser.dataspace.copernicus.eu/) |

---

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/Jk-Pascoal/sinop-agro-gis.git
cd sinop-agro-gis
```

### 2. Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 3. Abra o projeto no QGIS
- Abra o QGIS
- Vá em `Projeto > Abrir` e selecione `qgis_project/Projeto-SINOP.qgz`

### 4. Execute os notebooks
```bash
jupyter notebook notebooks/
```

---

## 📊 Análises e Resultados

### Mapa 1 — Limite Municipal de Sinop-MT
> Fronteira municipal sobre imagem de satélite de alta resolução (ESRI World Imagery). É possível observar nitidamente o contraste entre os fragmentos de **floresta nativa** (verde escuro) e os **talhões agrícolas** (bege) que dominam a paisagem do município.

![Limite Municipal de Sinop-MT](maps/exportados/01_sinop_limite_municipal.png)

*Fonte: IBGE — Malha Municipal 2022 | Imagem: ESRI World Imagery*

---

### Mapa 2 — Uso do Solo (MapBiomas 2024)
> *Em desenvolvimento*

### Mapa 3 — Expansão Agrícola 2000–2024
> *Em desenvolvimento*

### Mapa 4 — Malha Viária e Pontos Logísticos
> *Em desenvolvimento*

---

## 🎯 Objetivos de Aprendizado

- [x] Configurar projeto QGIS com sistema de coordenadas SIRGAS 2000
- [ ] Importar e reprojetar shapefiles do IBGE
- [ ] Classificar uso do solo com dados MapBiomas
- [ ] Criar layout de mapa profissional no QGIS
- [ ] Integrar QGIS com Python via PyQGIS ou GeoPandas
- [ ] Publicar mapa interativo online com Folium

---

## 👤 Autor

**Jakson Pascoal**
- GitHub: [@Jk-Pascoal](https://github.com/Jk-Pascoal)
- Localização: Sinop, Mato Grosso — Brasil 🌱

---

## 📄 Licença

Este projeto está sob a licença MIT. Os dados utilizados estão sujeitos às licenças de suas respectivas fontes.

---

*Projeto desenvolvido como parte do portfólio de Ciência de Dados e Análise Geoespacial.*
