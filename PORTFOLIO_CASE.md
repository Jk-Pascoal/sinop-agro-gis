# Sinop Agro-GIS — Data Science Geoespacial aplicada à fronteira agrícola

Este documento apresenta o projeto **Sinop Agro-GIS** sob a perspectiva de um caso de portfólio profissional (Case Study), destacando o valor de negócios, as decisões de engenharia de dados, geoprocessamento e os impactos analíticos obtidos.

---

## 📌 Contexto
O município de **Sinop-MT** (código IBGE 5107909), localizado no norte do estado de Mato Grosso, é um dos maiores eixos de produção de grãos e um polo agroindustrial proeminente da Região Centro-Oeste do Brasil. Inserido originalmente no ecótono do bioma Amazônico, o município passou por um intenso processo de conversão do uso do solo nas últimas décadas. 

Neste cenário de forte expansão das lavouras de soja e milho, torna-se essencial mapear de forma integrada a evolução territorial do solo, os volumes de produção agrícola e a infraestrutura logística terrestre disponível para escoamento. Este projeto nasceu com o propósito de suprir essa demanda com análises espaciais de alta resolução temporal e métricas estatísticas robustas.

---

## 🎯 Problema de Negócio
Como a expansão agrícola alterou o território de Sinop-MT entre 2000 e 2024, quais gargalos logísticos aparecem nesse processo e como dados geoespaciais podem apoiar decisões de produção, infraestrutura, sustentabilidade e planejamento territorial?

Para solucionar esse problema, o projeto buscou responder:
1. Mapear a transição espacial e calcular a correlação de Pearson entre a retração da floresta nativa e a expansão da soja.
2. Identificar a disparidade entre a área física mapeada por sensoriamento remoto e os volumes reportados de milho (safrinha) em regime de rotação de culturas.
3. Quantificar a densidade e a qualidade da malha rodoviária interna do município, avaliando o percentual de estradas não pavimentadas frente ao escoamento agroindustrial.

---

## 💾 Dados Utilizados
O pipeline do projeto foi desenhado integrando múltiplos repositórios e bases públicas oficiais de dados:

| Conjunto de Dados | Fonte | Tipo de Dado | Finalidade no Case |
| :--- | :--- | :--- | :--- |
| **Uso e Cobertura da Terra** | MapBiomas Collection 10.1 | Raster (GeoTIFF) | Classificação anual (30 metros de resolução) no período 2000–2024. |
| **Produção Agrícola Municipal (PAM)** | IBGE/SIDRA | Tabular (CSV) | Séries históricas de área plantada, volume e rendimento no período 2010–2023. |
| **Limites Municipais Oficiais** | IBGE | Vetorial (Shapefile) | Definição da fronteira cartográfica de Sinop-MT (3.990,3 km² / 399.086 ha). |
| **Malha Rodoviária e Vias** | OpenStreetMap via Geofabrik | Vetorial (Shapefile) | Identificação das estradas rurais, estaduais e do eixo da BR-163. |

---

## ⚙️ Metodologia
A execução técnica do case seguiu sete fases principais estruturadas sob uma esteira de reprodutibilidade em Python e QGIS:

1. **Coleta de Dados Públicos:** Extração e download programático e manual das bases de dados raster (MapBiomas Collection 10.1) e vetoriais/estatísticas (IBGE/SIDRA e OpenStreetMap via Geofabrik).
2. **Recorte Espacial e Alinhamento:** Recorte das geometrias estaduais/nacionais usando a máscara do limite municipal de Sinop-MT. Reprojeção sistemática de todas as camadas para o CRS métrico local: **SIRGAS 2000 / UTM 21S (EPSG:31981)**.
3. **Tratamento e Classificação:** Agrupamento das classes originais do MapBiomas Collection 10.1 em categorias consolidadas (ex: Soja, Floresta Nativa, Pastagem, Área Urbana) e cálculo de áreas físicas anuais em hectares.
4. **Análise Estatística Temporal:** Modelagem matemática do comportamento das séries de dados de 2000–2024, calculando o coeficiente de correlação linear de Pearson para verificar a dinâmica espelhada entre floresta e soja.
5. **Integração Agroprodutiva:** Análise das séries históricas de produção agrícola (2010–2023), estabelecendo os ritmos de avanço de área vs. produção e a interpretação agronômica da rotação da soja com o milho safrinha.
6. **Análise de Infraestrutura Logística:** Filtragem e classificação hierárquica das vias do município, avaliando a extensão linear por tipo de pavimento, o isolamento do eixo da rodovia federal BR-163 e a densidade de rede logística.
7. **Visualização de Dados e Dashboard:** Construção de dashboards interativos em HTML5/CSS3/JavaScript usando Chart.js e mapas baseados em Folium, hospedados diretamente via GitHub Pages para consumo do usuário final.

---

## 🏆 Principais Insights
* **Soja no território em 2024:** 42,6% da área total (169.852 ha).
* **Floresta remanescente em 2024:** 36,2% (129.179 ha).
* **Correlação floresta × soja:** -0,984, demonstrando uma dinâmica quase perfeitamente espelhada de conversão direta de solo.
* **Retração Vegetal:** A floresta perdeu 114.321 ha entre 2000 e 2024.
* **Expansão Agrícola:** A soja cresceu 137.852 ha entre 2000 e 2024.
* **Malha Viária Mapeada:** 1.842 km, divididos em 6.394 segmentos de via.
* **Vetor Federal:** 63,9 km da BR-163 mapeados dentro do território de Sinop-MT.
* **Dependência do Solo:** 66,7% das vias são estradas de terra (Tracks). Isso significa que dois terços do escoamento dependem de infraestrutura vulnerável ao período chuvoso.
* **Dinâmica do Duplo Cultivo (Safrinha):** O milho safrinha é cultivado na mesma área de solo que a soja após a primeira colheita. Isso elucida o paradoxo de o milho produzir quase o mesmo volume que a soja ocupando 39% a menos de área no mapeamento espacial físico.

---

## 💡 Impacto Potencial
Os modelos analíticos e dados espaciais consolificados no Sinop Agro-GIS podem fundamentar tomadas de decisão de alto nível, tais como:
* **Planejamento Logístico e de Escoamento:** Auxiliar cooperativas e produtores no cálculo de rotas e custos de frete baseados no tipo de estrada (terra vs. asfalto).
* **Priorização de Infraestrutura Viária:** Subsidiar gestores públicos na identificação de estradas vicinais críticas para pavimentação com base no fluxo agrícola.
* **Monitoramento Ambiental:** Apoiar iniciativas de *ESG* e rastreabilidade da produção, avaliando o cumprimento da Moratória da Soja e do Código Florestal brasileiro.
* **Alocação de Armazenagem:** Identificar zonas com déficit ou superávit de capacidade de silos com base no avanço geográfico da soja e do milho.

---

## 🛠️ Stack Técnica
* **Linguagem:** Python 3.12
* **Manipulação de Dados:** pandas, numpy, GeoPandas, Shapely
* **Visualização Científica:** Matplotlib, Plotly, Folium
* **Ambiente GIS Desktop:** QGIS (Projeto integrado `.qgz`)
* **Bases e Classificações:** MapBiomas Collection 10.1, IBGE/SIDRA, OpenStreetMap via Geofabrik
* **Deploy e Web:** HTML5, CSS3, Vanilla JavaScript, Chart.js, GitHub Pages

---

## ⚠️ Limitações
* **Causalidade Estatística:** O cálculo de correlação de Pearson descreve associação matemática, mas não expressa necessariamente causalidade direta sem o suporte de variáveis regulatórias e econômicas.
* **Resolução do Sensoriamento:** A resolução de 30 metros por pixel (MapBiomas Collection 10.1) pode suavizar estradas muito estreitas ou pequenos fragmentos de APP (Área de Preservação Permanente).
* **Janela do Milho:** O mapeamento anual de uso do solo captura prioritariamente a soja (cultura primária do verão), ocultando o milho safrinha nos mapas anuais estáticos do MapBiomas.
* **Fidelidade da Rede OSM:** A base viária do OpenStreetMap via Geofabrik baseia-se em mapeamento voluntário colaborativo, podendo conter pequenas defasagens em áreas rurais isoladas.
* **Independência Técnica:** O projeto possui cunho acadêmico e de portfólio de Data Science, não devendo substituir laudos ou estudos oficiais para licenciamentos governamentais.

---

## 🔮 Próximas Fases

### Fase 8 — Rede Logística (Network Analysis):
* Mapeamento de grafo rodoviário com **NetworkX**.
* Cálculo de matriz de distâncias e rotas ótimas até os silos de recepção e a rodovia BR-163.
* Criação de mapas de fricção de tráfego baseados em pavimentação e precipitação média mensal.
* Geração de um índice municipal de vulnerabilidade logística para estradas de terra.

### Fase 9 — Modelagem Preditiva (Land Use Change Model):
* Simulações e projeções de conversão do solo (expansão agrícola e desmatamento) até 2030.
* Construção de modelos estatísticos e matemáticos com cenários variados (Tendência, Conservador e Acelerado).
* Delimitação de intervalos de confiança e documentação de incertezas.

---

## 🚀 Como Executar o Projeto

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/Jk-Pascoal/sinop-agro-gis.git
   cd sinop-agro-gis
   ```
2. **Ambiente Virtual e Dependências:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Download de Dados Dinâmicos:**
   ```bash
   python scripts/download_dados.py
   ```
4. **Execução de Jupyter Notebooks:**
   Rode os notebooks presentes em `notebooks/` de 01 a 07 para processar os dados brutos e reconstruir as tabelas analíticas.

---

## 🔗 Links Úteis
* **Código no GitHub:** [github.com/Jk-Pascoal/sinop-agro-gis](https://github.com/Jk-Pascoal/sinop-agro-gis)
* **Dashboard Publicado:** [Jk-Pascoal.github.io/sinop-agro-gis/](https://Jk-Pascoal.github.io/sinop-agro-gis/)
* **Mapa Interativo Integrado:** [Visualizar Mapa](mapa.html)
