# Plano de Implementação — Integração Logística e Dinamização de Dados

Este plano propõe modificações para corrigir os downloads automatizados, tornar as análises do IBGE dinâmicas através de arquivos CSV e adicionar o processamento geoespacial da infraestrutura de logística (malha viária e pontos de armazenamento) para o município de Sinop-MT.

---

## Alterações Propostas

### 1. 📂 Dinamização dos Dados de Produção (IBGE PAM)

#### [NOVO] [producao_ibge.csv](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/producao_agricola/producao_ibge.csv)
Criar um arquivo CSV com os dados da produção de soja e milho (2010–2023) que estavam hardcoded no notebook 05.

#### [MODIFICAR] [05_producao_ibge_sidra.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/05_producao_ibge_sidra.ipynb)
Substituir a declaração manual do dicionário de dados pela importação dinâmica via pandas.

---

### 2. 🛣️ Correção do Download de Malha Viária

#### [MODIFICAR] [download_dados.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/download_dados.py)
Corrigir a URL da malha viária do Centro-Oeste no Geofabrik (adicionando o sufixo `-free` que está faltando):
*   De: `https://download.geofabrik.de/south-america/brazil/centro-oeste-latest.shp.zip`
*   Para: `https://download.geofabrik.de/south-america/brazil/centro-oeste-latest-free.shp.zip`

---

### 3. 🗺️ Processamento da Infraestrutura Logística de Sinop

#### [NOVO] [processa_logistica.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/processa_logistica.py)
Criar um script Python que automatiza o processamento e recorte da malha logística (rodovias, ferrovias e possíveis silos) para Sinop.

---

## Plano de Verificação

### Testes Automatizados
- Executar `python scripts/download_dados.py` para verificar o sucesso do download do shapefile da malha viária corrigido.
- Executar `python scripts/processa_logistica.py` para certificar-se de que os shapefiles de rodovias e silos de Sinop foram recortados e gerados sem erros de CRS ou topologia.
- Rodar o notebook `05_producao_ibge_sidra.ipynb` usando os dados importados do CSV e conferir se os gráficos gerados coincidem com as imagens exportadas.
