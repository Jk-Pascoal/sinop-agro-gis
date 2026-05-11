# 📥 Guia de Download — Fontes de Dados

Este guia contém os links exatos e instruções de download para todos os dados utilizados no projeto.

---

## 1. 🗺️ Limite Municipal — IBGE

**O que baixar:** Shapefile do município de Sinop-MT (ou Mato Grosso completo)

**Link direto:**
https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/MT/MT_Municipios_2022.zip

**Instruções:**
1. Baixe o ZIP acima
2. Extraia em `data/limite_municipal/`
3. No QGIS: Arraste o arquivo `.shp` para o painel de camadas
4. Filtre pelo código IBGE de Sinop: **5107909**

---

## 2. 🌿 Uso do Solo — MapBiomas

**O que baixar:** Coleção 8 — Mosaico Anual de Uso e Cobertura do Solo

**Link:**
https://mapbiomas.org/colecoes-mapbiomas-1

**Instruções:**
1. Acesse o [Workspace do MapBiomas no GEE](https://code.earthengine.google.com/?scriptPath=users/mapbiomas/user-toolkit:mapbiomas-user-toolkit-download.js)
2. Ou use o [MapBiomas User Toolkit](https://mapbiomas.org/ferramentas)
3. Selecione: Estado = MT, Município = Sinop, Anos = 2000, 2010, 2020, 2023
4. Exporte como GeoTIFF para `data/uso_solo_mapbiomas/`

**Alternativa mais fácil:**
- Acesse: https://plataforma.brasil.mapbiomas.org/
- Vá em "Downloads" > "Baixar por município"
- Selecione Sinop-MT

---

## 3. 🛣️ Malha Viária — DNIT / OpenStreetMap

### Opção A — DNIT (Rodovias Federais Oficiais)
**Link:**
https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/dnit-geo/shapefiles/sistema-nacional-de-viacao

### Opção B — OpenStreetMap via GeoFabrik (mais completo)
**Link:**
https://download.geofabrik.de/south-america/brazil/centro-oeste.html

**Arquivo:** `centro-oeste-latest-free.shp.zip`
- Extraia e use a camada `roads`
- Filtre pela região de Sinop no QGIS

---

## 4. 📊 Produção Agrícola — IBGE/SIDRA

**O que baixar:** Produção Agrícola Municipal (PAM) — Lavouras Temporárias

**Link:**
https://sidra.ibge.gov.br/tabela/5457

**Instruções:**
1. Acesse o link
2. Selecione: 
   - Variáveis: Área plantada, Quantidade produzida, Valor da produção
   - Produtos: Soja, Milho, Algodão
   - Períodos: 2000 a 2023
   - Nível territorial: Municípios > MT > Sinop
3. Baixe como CSV e salve em `data/producao_agricola/`

---

## 5. 🛰️ Imagens de Satélite — Copernicus/Sentinel

**Link:**
https://browser.dataspace.copernicus.eu/

**Instruções:**
1. Crie uma conta gratuita
2. Selecione: Sentinel-2 L2A
3. Área: desenhe um bounding box sobre Sinop-MT
4. Período: escolha um mês sem muitas nuvens (junho/julho)
5. Baixe como GeoTIFF

---

## Resumo dos Arquivos Esperados

```
data/
├── limite_municipal/
│   ├── MT_Municipios_2022.shp   ← IBGE
│   └── sinop_recorte.shp        ← Filtrado no QGIS
│
├── uso_solo_mapbiomas/
│   ├── sinop_2000_uso_solo.tif  ← MapBiomas
│   ├── sinop_2010_uso_solo.tif
│   ├── sinop_2020_uso_solo.tif
│   └── sinop_2023_uso_solo.tif
│
├── malha_viaria/
│   └── rodovias_mt.shp          ← DNIT ou OSM
│
└── producao_agricola/
    └── pam_sinop_2000_2023.csv  ← IBGE SIDRA
```
