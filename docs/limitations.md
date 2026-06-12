# Limitações da Análise — Sinop Agro-GIS

Este documento resume as principais limitações metodológicas, cartográficas e estatísticas identificadas no projeto **Sinop Agro-GIS**. Compreender estes limites é fundamental para a interpretação correta dos achados analíticos e tomada de decisão fundamentada em dados.

---

## 🔍 1. Diferenças Metodológicas entre Fontes de Dados

Há divergências numéricas conhecidas entre as áreas reportadas pelas fontes de dados primárias deste projeto:
- **MapBiomas:** Baseia-se na classificação automatizada de pixels de imagens de satélite Landsat (resolução de 30m). A área agrícola estimada refere-se à assinatura espectral dos talhões de plantio.
- **IBGE SIDRA (Produção Agrícola Municipal - PAM):** Baseia-se em pesquisas declaratórias e estimativas subjetivas fornecidas por agentes locais do setor agropecuário, agrônomos, cooperativas e órgãos municipais.
- *Inconsistência comum:* A soma de área mapeada por sensoriamento remoto (MapBiomas) e a área plantada declarada (IBGE) raramente coincide exatamente em virtude de sobreposições de safras (soja seguida de milho safrinha na mesma área física, o que pode duplicar a declaração de área no IBGE, mas mantém a mesma área espacial pixelizada).

---

## 🛰️ 2. Resolução Espacial e Espectral do MapBiomas

Os dados raster do MapBiomas são gerados a partir do processamento de imagens do satélite Landsat com resolução de **30 metros por pixel**.
- **Limitações decorrentes:**
  - Áreas pequenas de transição ou feições lineares estreitas (como matas ciliares degradadas, estradas rurais estreitas, pequenos canais d'água e plantios isolados menores que $900\ m^2$) podem ser erroneamente classificadas por conta do efeito do pixel misto.
  - Fragmentação florestal de pequena escala pode ser subestimada no mapeamento geral.

---

## ⏳ 3. Possíveis Inconsistências Temporais em Séries Históricas

Algoritmos de classificação espectral do MapBiomas evoluem entre as versões de coleções (atualmente Collection 10.1).
- **Limitações decorrentes:**
  - Em alguns anos específicos, mudanças repentinas na qualidade das imagens (cobertura excessiva de nuvens) ou ruídos espectrais podem induzir a falsas flutuações temporais no mapeamento da área de transição Floresta x Pastagem.
  - O projeto utiliza uma série consolidada suavizada, contudo flutuações pontuais de um único ano devem ser interpretadas como potenciais anomalias de sensores de satélite.

---

## 🔮 4. Limitações de Projeções Futuras e Modelagem Preditiva

Qualquer projeção temporal apresentada nos notebooks ou dashboard constitui extrapolação estatística simplificada baseada em regressões históricas (2000–2024).
- **Limitações decorrentes:**
  - Esses modelos lineares simples não consideram fatores geoeconômicos complexos como: variações no preço internacional da soja (commodities), restrições regulatórias severas (ex: moratória da soja), impactos climáticos severos (El Niño/La Niña), ou mudanças drásticas na legislação florestal nacional (Código Florestal).

---

## 🏛️ 5. Dependência Estrita de Dados Públicos e Open Source

O projeto é estruturado inteiramente sobre bases de dados abertas governamentais e comunitárias (IBGE, DNIT, OpenStreetMap, MapBiomas).
- **Limitações decorrentes:**
  - A frequência de atualização dos dados está fora do controle dos analistas.
  - A acurácia espacial das redes viárias do OpenStreetMap depende inteiramente da atuação da comunidade de mapeadores voluntários locais. Algumas rodovias rurais municipais podem estar ausentes ou classificadas incorretamente.

---

## 🚜 6. Necessidade de Validação de Campo (*Ground Truth*)

Toda a análise espacial e logística foi executada em ambiente laboratorial/computacional.
- **Limitações decorrentes:**
  - Mapeamentos geoespaciais necessitam de validação em campo para aferir a acurácia global.
  - Silos e armazéns mapeados via OSM devem ser confrontados com os cadastros ativos da CONAB (Companhia Nacional de Abastecimento) e validados localmente para garantir sua real capacidade operacional atualizada.

---

## 🛣️ 7. Critérios de Malha Viária e Extensão da BR-163

O projeto apresenta dois conjuntos distintos de métricas de infraestrutura rodoviária que representam diferentes níveis de tratamento dos dados espaciais:
- **Malha Viária Principal (Logística):** O valor de **1.842,15 km** (com densidade de **0,462 km/km²**) exibido no dashboard e no README representa a malha viária principal de escoamento e de conexão logística agroindustrial. Dela foram eliminadas as vias urbanas de tráfego estritamente residencial local, ciclovias, caminhos de pedestres e acessos rurais particulares menores que não influenciam no escoamento de safras.
- **Malha Geográfica Bruta (OSM):** O valor calculado de **3.640,42 km** (e densidade de **0,912 km/km²**) no Notebook 07 corresponde à totalidade absoluta de linhas viárias digitalizadas pela comunidade voluntária do OpenStreetMap.
- **Rodovia BR-163 (Múltiplas Extensões):** O comprimento do eixo simples da rodovia federal de escoamento BR-163 cruzando o município de sul a norte é de **72,82 km**. Contudo, o cálculo espacial no QGIS e no Notebook 07 totaliza **81,21 km** (e **81,30 km** agrupados na classe *trunk*). Esta diferença de ~8,4 km decorre do fato de o OSM mapear de forma independente as pistas duplas separadas de rodovia duplicada, trevos de acesso e vias marginais de desaceleração paralelas, cujos comprimentos de linha são integrados na soma geométrica vetorial bruta.
