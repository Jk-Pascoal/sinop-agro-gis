# Dicionário de Dados — Sinop Agro-GIS

Este documento descreve os principais campos e variáveis estruturadas que compõem o banco de dados e as análises integradas do projeto **Sinop Agro-GIS**.

---

## 📋 Campos Finais de Uso do Solo e Produção

Os campos abaixo padronizam o controle de métricas do projeto (utilizados na consolidação temporal de dados do MapBiomas e IBGE SIDRA):

| Campo | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| **`ano`** | Inteiro | Ano de referência do registro estatístico ou da cobertura espacial. | `2023` |
| **`classe_uso_solo`** | Texto | Classe de cobertura do solo identificada pelo mapeamento do MapBiomas. | `"Soja"` |
| **`area_ha`** | Decimal | Área total calculada para a respectiva classe de uso do solo, expressa em hectares (ha). | `169851.83` |
| **`area_pct`** | Decimal | Percentual de representatividade da classe de uso do solo sobre a área total do município. | `42.56` |
| **`cultura`** | Texto | Nome da cultura agrícola temporária analisada (dados IBGE PAM). | `"Milho"` |
| **`area_plantada_ha`** | Decimal | Área declarada de plantio para a respectiva cultura (PAM/IBGE), expressa em hectares (ha). | `68000.00` |
| **`producao_t`** | Decimal | Volume total de grãos colhidos para a cultura analisada, expressa em toneladas (t). | `476000.00` |
| **`rendimento`** | Decimal | Produtividade agrícola média da cultura, expressa em toneladas por hectare (t/ha). | `7.00` |
| **`fonte`** | Texto | Fonte primária de onde o dado foi extraído. | `"MapBiomas Col. 10.1"` |
| **`data_processamento`**| Texto | Data e hora em que a análise/processamento foi executado (formato ISO 8601). | `2026-06-12T10:30:00Z` |
| **`observacoes`** | Texto | Notas técnicas ou metadados adicionais sobre o registro. | `"Safra principal de soja"` |

---

## 🗺️ Campos Espaciais das Camadas de Logística

Campos específicos extraídos e processados da malha viária (OpenStreetMap/DNIT):

* **`fclass`**: Categoria da via de acordo com o OpenStreetMap (ex: `trunk` para rodovias federais principais como a BR-163, `track` para estradas de terra no interior das fazendas, `residential` para vias urbanas).
* **`name`**: Nome oficial ou identificador da rodovia/rua (ex: `"Rodovia Transamazônica"`, `"BR-163"`).
* **`comprimento_km`**: Extensão física calculada do segmento de via após reprojeção cartográfica métrica (EPSG:31981), expressa em quilômetros (km).
* **`geometry`**: Geometria espacial do elemento no sistema SIG (pode ser `LineString` para vias ou `Point` para a localização dos silos de grãos).
