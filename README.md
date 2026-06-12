# 🌱 Sinop Agro-GIS

## Resumo executivo
Análise geoespacial da expansão agrícola em Sinop-MT, integrando uso do solo, produção agropecuária e infraestrutura logística.

---

## 📌 Sobre o Projeto

Este projeto consiste em um estudo de caso geoespacial detalhado sobre a evolução do uso do solo, o avanço da fronteira agrícola e a capacidade de atendimento da malha logística no município de **Sinop-MT** — reconhecido polo agroindustrial da região Norte de Mato Grosso. 

Integrando ferramentas de Sistemas de Informação Geográfica (**QGIS**) e análise avançada de dados (**Python/GeoPandas/Plotly**), analisamos o comportamento territorial do município nos últimos 24 anos (2000–2024) sob o viés da consolidação da soja e do milho como motores econômicos e a consequente alteração da cobertura vegetal nativa.

---

## ❓ Perguntas de Pesquisa

O pipeline analítico foi estruturado para responder a quatro questionamentos centrais:
1. **Como a expansão agrícola reconfigurou o território de Sinop-MT?**
2. **Quanto a soja avançou em relação às demais classes de uso do solo?**
3. **A produção cresceu por expansão territorial, produtividade ou ambos?**
4. **A infraestrutura logística acompanha a expansão agrícola?**

---

## 🏆 Principais Achados

* **Dominância da Soja:** A cultura da soja expandiu aceleradamente, ocupando mais de **169.852 ha (42,6%)** do território municipal em 2024, consolidando-se como a classe de uso do solo dominante em Sinop.
* **Redução da Cobertura Florestal:** A floresta nativa remanescente recuou para **129.179 ha (32,4%)**, evidenciando um padrão histórico de substituição de bioma por lavouras temporárias e pastagens antes de sua posterior conversão agrícola.
* **Crescimento de Produção de Grãos (2010–2023):**
  - **Soja:** Expansão de **+112% em área** e **+128% em produção**, sugerindo que o ganho produtivo decorreu tanto da expansão da área física quanto de pequenos incrementos tecnológicos.
  - **Milho Safrinha:** Aumento expressivo de **+278% em área** e **+341% em produção**, impulsionado pela consolidação da rotação de culturas na segunda safra.
* **Gargalo Logístico RURAL:** A extensão total da malha viária principal filtrada é de **1.842,15 km** (densidade viária de **0,462 km/km²**). Nota-se que a malha viária bruta total do OSM é de **3.640,42 km** (incluindo ruelas residenciais e acessos de serviço). Contudo, **66,7% (1.228,15 km)** de toda a rede filtrada é composta por estradas não pavimentadas de terra (*tracks*), gerando severos custos operacionais de transporte internos e dependência crítica do eixo federal pavimentado da **BR-163 (72,82 km)** (eixo simplificado, correspondendo a **81,21 km** no total de feições OSM devido a pistas duplas e marginais paralelas).

---

## 🗂️ Estrutura do Repositório

O repositório está organizado de forma modular e reprodutível seguindo as melhores práticas de engenharia de dados e GIS:

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

## 📦 Fontes de Dados

| Dataset | Fonte Primária | Tipo de Dado | Finalidade |
| :--- | :--- | :--- | :--- |
| **Limites Municipais** | IBGE (2022) | Vetor (Shapefile) | Definição da fronteira e delimitação regional. |
| **Uso e Cobertura do Solo** | MapBiomas Col. 10.1 (2024) | Raster (GeoTIFF 30m) | Mapeamento multitemporal das classes de solo. |
| **Produção Agrícola (PAM)** | IBGE SIDRA - Tabela 5457 | Tabular (CSV) | Séries históricas de área, produção e rendimento. |
| **Malha Rodoviária e POIs** | OpenStreetMap (OSM) / DNIT | Vetor (Shapefile/Overpass) | Mapeamento viário e identificação de silos/armazéns. |

---

## ⚙️ Metodologia Resumida

O projeto realiza o processamento espacial por meio de:
1. **Recorte Territorial:** Delimitação dos rasters estaduais do MapBiomas e shapefiles do OpenStreetMap usando a máscara de limite político-administrativo de Sinop.
2. **Reprojeção Métrica:** Transformação do CRS geográfico para o sistema projetado **SIRGAS 2000 / UTM Zone 21S (EPSG:31981)** para realização de medições físicas precisas.
3. **Cálculo Espacial e Agrupamento:** Quantificação em hectares de coberturas por pixel e contagem de extensão viária por categoria.
4. **Cruzamento Estatístico:** Integração espacial dos buffers de silos e estradas com as séries produtivas e de desmatamento vegetal.

*Para uma explicação técnica exaustiva, consulte o arquivo [docs/methodology.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/methodology.md).*

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
*Consulte o guia interativo [scripts/guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) para o download das tabelas de dados agrícolas e rasters do MapBiomas.*

### 3. Rodar as Análises
Abra o Jupyter e execute os notebooks na ordem numérica:
```powershell
jupyter notebook notebooks/
```

### 4. Abrir no QGIS
Inicie o QGIS e carregue o arquivo de projeto [qgis_project/Projeto-SINOP.qgz](file:///C:/Users/Administrador/Documents/Projeto-SINOP/qgis_project/Projeto-SINOP.qgz).

---

## 📊 Resultados

O projeto disponibiliza os seguintes mapas e infográficos na pasta `maps/exportados/`:
- **Mapa 1:** Limite Municipal de Sinop-MT sobre imagem aérea (ESRI World Imagery).
- **Mapa 2:** Distribuição do Uso do Solo de 2024 por classes (MapBiomas).
- **Gráfico 3:** Evolução temporal comparativa da perda florestal vs avanço de soja.
- **Gráfico 4:** Evolução produtiva de soja e milho safrinha (Área vs Produção).
- **Mapa 5:** Rede logística viária e distribuição espacial de armazéns/silos de grãos.

---

## 🔍 Pontos a Validar e Consolidações

Existem pequenas divergências estatísticas entre as fontes integradas no projeto. Elas são inerentes às metodologias de captura e foram consolidadas com base nas seguintes diretrizes:

1. **Divergência na Área de Soja (2023):**
   - **MapBiomas (Sensoriamento Remoto):** 169.400 ha de soja mapeados espectralmente.
   - **IBGE SIDRA (Estatística Declaratória - Tabela 5457):** 176.000 ha de área de soja declarados pelos produtores.
   - **Diferença:** ~6.600 ha (~3,8% de variação). Reflete a diferença metodológica padrão entre imagens de satélite e cadastros declarados.

2. **Divergência na Área de Milho (2023):**
   - **MapBiomas (Classificação Anual):** O milho safrinha (segunda safra) é plantado na mesma área física após a soja, sendo classificado na categoria secundária "Outras Lavouras" (28.619 ha em 2024).
   - **IBGE SIDRA (Tabela 5457):** Área declarada de 68.000 ha para o milho em 2023.
   - **Explicação:** O MapBiomas calcula a área física do solo uma única vez (soja como cultura primária), enquanto o IBGE soma o plantio acumulado de ambas as safras, resultando em uma área plantada total acumulada maior.

3. **Critérios de Malha Viária e Extensão da BR-163:**
   - **Eixo Principal BR-163:** Padronizado em **72,82 km** de extensão linear (travessia simples), registrando-se que a soma das feições no OSM totaliza **81,21 km** devido à duplicidade de pistas e vias marginais paralelas mapeadas individualmente.
   - **Extensão Rodoviária Total:** Mantido o padrão de **1.842,15 km** de malha logística principal filtrada para escoamento agrícola no dashboard e README. O valor bruto de **3.640,42 km** no Notebook 07 compreende a malha municipal OSM total incluindo pequenas ruelas urbanas e vias de serviço internas.

---

## ⚠️ Limitações

- **Resolução de pixel (30m):** Pequenos canais de drenagem ou estradas rurais estreitas podem apresentar pixels mistos e classificação ruidosa.
- **Dependência de Dados Comunitários:** A malha viária municipal depende da completude e mapeamento voluntário no OpenStreetMap.
- **Projeções de Tendência:** As análises preditivas nos notebooks são tendências estatísticas lineares básicas e não incorporam variáveis macroeconômicas complexas (preço de commodities, barreiras ambientais como a moratória da soja, etc.).

*Consulte [docs/limitations.md](file:///C:/Users/Administrador/Documents/Projeto-SINOP/docs/limitations.md) para detalhes adicionais.*

---

## 🔮 Próximos Passos

1. **Validação Temporal Ampliada:** Atualizar o pipeline de dados para incluir os novos dados consolidados das coleções anuais futuras do MapBiomas.
2. **Modelagem de Risco de Desmatamento:** Aplicar algoritmos de Machine Learning (como Random Forest ou XGBoost) para prever áreas de vegetação nativa com maior susceptibilidade à conversão para lavouras com base na proximidade da BR-163.
3. **Cálculo da Capacidade dos Silos:** Cruzar dados da CONAB para estimar o déficit ou superávit de capacidade estática de armazenagem municipal frente ao ritmo de expansão produtiva.

---

## 👤 Autor

**Jakson Pascoal**
- GitHub: [@Jk-Pascoal](https://github.com/Jk-Pascoal)
- Localização: Sinop, Mato Grosso — Brasil 🇧🇷

---

## 📄 Licença

Este projeto é disponibilizado sob a licença **MIT**. Os dados utilizados estão vinculados às restrições e termos de uso de suas respectivas instituições fornecedoras (IBGE, MapBiomas, OpenStreetMap).
