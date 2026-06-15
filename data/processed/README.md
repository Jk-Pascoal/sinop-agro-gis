# 📊 Modelos e Dados Processados

Esta pasta contém conjuntos de dados espaciais e tabulares consolidados, após o processamento das rotinas analíticas do projeto Sinop Agro-GIS.

---

## 📋 Modelo de Controle de Métricas (`metricas_finais_template.csv`)

O arquivo [metricas_finais_template.csv](file:///C:/Users/Administrador/Documents/Projeto-SINOP/data/processed/metricas_finais_template.csv) padroniza a exportação final dos dados de cobertura do solo (MapBiomas) e das estatísticas de produção agrícola municipal (IBGE/SIDRA).

### Estrutura do Cabeçalho:
`ano,classe_uso_solo,area_ha,area_pct,cultura,area_plantada_ha,producao_t,rendimento,fonte,data_processamento,observacoes`

### Exemplo de Preenchimento (Comentado):
```csv
# Exemplo 1: Registro de Uso do Solo (MapBiomas)
2023,Soja,169400.00,42.45,,,,"MapBiomas Col. 10.1",2026-06-12T10:30:00Z,"Área física classificada por sensoriamento remoto"

# Exemplo 2: Registro de Produção Agrícola (IBGE SIDRA)
2023,,,,,68000.00,476000.00,7.00,"IBGE SIDRA PAM T.5457",2026-06-12T10:30:00Z,"Milho safrinha (segunda safra) declarada"
```

---

## 🗺️ Arquivos Espaciais Processados

Os seguintes arquivos são gerados dinamicamente na execução dos notebooks:
* **`sinop_recorte.shp`**: Delimitação espacial do limite municipal de Sinop-MT, recortado a partir da malha municipal oficial de Mato Grosso do IBGE.
* **`coverage_by_class_2024.csv`**: Estatísticas consolidadas de uso do solo extraídas do raster do MapBiomas.
