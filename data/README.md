# 📊 Dados do Projeto SINOP Agro-GIS

## Status de Datasets

### ✅ **Baixados e Prontos**

#### Limites Municipais (IBGE 2022)
- **Localização:** `limite_municipal/`
- **Arquivos:** Shapefiles (.shp, .dbf, .shx, .prj, .cpg)
- **Cobertura:** Todos os municípios de Mato Grosso
- **Como usar:** Carregue o arquivo `.shp` no QGIS
- **Filtro para Sinop:** Código IBGE = 5107909

---

### ⏳ **Requer Download Manual**

#### 1️⃣ MapBiomas — Uso e Cobertura do Solo
- **Localização:** `uso_solo_mapbiomas/`
- **Formato:** GeoTIFF (rasters anuais)
- **Anos Recomendados:** 2000, 2010, 2020, 2023
- **Download FÁCIL:** https://plataforma.brasil.mapbiomas.org/
- **Instruções:**
  1. Selecione MT > Sinop
  2. Escolha os anos desejados
  3. Exporte como GeoTIFF
  4. Extraia em `uso_solo_mapbiomas/`

#### 2️⃣ Malha Viária — Rodovias e Ferrovias
- **Localização:** `malha_viaria/`
- **Formato:** Shapefile
- **Fontes:**
  - DNIT: https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/dnit-geo
  - OpenStreetMap (QuickOSM no QGIS)
- **Para Sinop:** Rodovias federais (BR-163, BR-158) e estaduais

#### 3️⃣ Produção Agrícola — IBGE/CONAB
- **Localização:** `producao_agricola/`
- **Formato:** CSV/Excel
- **Fonte Recomendada:** https://sidra.ibge.gov.br/ (Tabela 1613)
- **Produtos:** Soja, Milho, Algodão
- **Anos:** 2000-2023
- **Salve como:** `producao_ibge.csv`

---

## 📥 Quick Start — Próximos Passos

### 1. No Computador (AGORA)
```bash
# Já foi executado:
python scripts/download_dados.py

# Próximo: abra os links acima e baixe MapBiomas, Malha Viária e Produção Agrícola
```

### 2. No QGIS (DEPOIS)
```
Camada > Adicionar Camada
├── Raster: MapBiomas GeoTIFFs
├── Vetor: Shapefiles de malha viária
└── Vetor: Já carregado - Limites municipais
```

### 3. Em Python (ANÁLISE)
```bash
# Scripts Python para análise:
jupyter notebook notebooks/

# Notebooks criados:
- 01_processamento.ipynb     (carregar e inspecionar dados)
- 02_analise_espacial.ipynb  (operações geoespaciais)
- 03_visualizacao.ipynb      (mapas interativos)
```

---

## 🗺️ Estrutura de Arquivos Esperada

```
data/
├── limite_municipal/
│   ├── MT_Municipios_2022.shp     ✅ (já tem)
│   ├── MT_Municipios_2022.dbf
│   ├── MT_Municipios_2022.shx
│   ├── MT_Municipios_2022.prj
│   └── MT_Municipios_2022.cpg
│
├── uso_solo_mapbiomas/            ⏳ (download manual)
│   ├── sinop_2000.tif
│   ├── sinop_2010.tif
│   ├── sinop_2020.tif
│   └── sinop_2023.tif
│
├── malha_viaria/                  ⏳ (download manual)
│   ├── br_malha_viaria.shp
│   ├── br_malha_viaria.dbf
│   └── br_malha_viaria.shx
│
└── producao_agricola/             ⏳ (download manual)
    └── producao_ibge.csv
```

---

## 📖 Referências

| Fonte | Link | Dados |
|-------|------|-------|
| **IBGE** | https://sidra.ibge.gov.br/ | Produção agrícola, censo |
| **MapBiomas** | https://mapbiomas.org/ | Uso/cobertura do solo |
| **CONAB** | https://www.conab.gov.br/ | Safras, série histórica |
| **DNIT** | https://www.gov.br/dnit/ | Infraestrutura viária |
| **Copernicus** | https://browser.dataspace.copernicus.eu/ | Imagens de satélite |

---

## ✨ Dica QGIS

Para carregar **múltiplos rasters** (MapBiomas por anos):

```
1. Camada > Adicionar Camada > Raster
2. Selecione: [Ctrl] para selecionar vários arquivos
3. Abra todos os GeoTIFFs de uma vez
4. No Painel de Camadas, organize cronologicamente
5. Use Timeline plugin para visualizar evolução temporal
```

