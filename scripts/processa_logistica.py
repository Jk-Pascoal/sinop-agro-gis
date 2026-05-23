#!/usr/bin/env python3
"""
processa_logistica.py
─────────────────────
Script para processar, recortar e filtrar dados de infraestrutura logística
(rodovias, ferrovias e armazéns/silos) para o município de Sinop-MT.

Requisitos:
    - Executar scripts/download_dados.py previamente
    - Bibliotecas geopandas, shapely e pandas instaladas
"""

import os
import sys
from pathlib import Path
import geopandas as gpd
import pandas as pd

# ── Caminhos ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LIMITE_DIR = DATA_DIR / "limite_municipal"
MALHA_DIR = DATA_DIR / "malha_viaria"

# Arquivos de Entrada (OSM Geofabrik)
ROADS_SHP = MALHA_DIR / "gis_osm_roads_free_1.shp"
RAILWAYS_SHP = MALHA_DIR / "gis_osm_railways_free_1.shp"
POIS_SHP = MALHA_DIR / "gis_osm_pois_free_1.shp"

# Arquivo de Limite de Sinop
SINOP_SHP = LIMITE_DIR / "sinop_recorte.shp"

# Arquivos de Saída
OUTPUT_ROADS = MALHA_DIR / "sinop_rodovias.shp"
OUTPUT_RAILS = MALHA_DIR / "sinop_ferrovias.shp"
OUTPUT_SILOS = MALHA_DIR / "sinop_silos.shp"

def main():
    print("=" * 70)
    print("🛣️  SINOP AGRO-GIS — PROCESSAMENTO DE INFRAESTRUTURA LOGÍSTICA")
    print("=" * 70)

    # 1. Verificar se o limite de Sinop existe
    if not SINOP_SHP.exists():
        print(f"❌ Limite de Sinop não encontrado: {SINOP_SHP}")
        print("💡 Execute os notebooks 01 e 02 para gerar o limite municipal de Sinop.")
        sys.exit(1)

    print("📍 Carregando limite municipal de Sinop...")
    sinop_gdf = gpd.read_file(SINOP_SHP)
    
    # 2. Verificar se os dados do Geofabrik estão disponíveis
    if not ROADS_SHP.exists():
        print(f"❌ Shapefile de rodovias não encontrado em: {ROADS_SHP}")
        print("💡 Por favor, execute primeiro: python scripts/download_dados.py")
        sys.exit(1)

    print("✓ Arquivos de dados OSM localizados.")

    # 3. Processar Rodovias (Clip)
    print("\n🚗 Processando Rodovias (isto pode levar alguns segundos)...")
    try:
        roads_gdf = gpd.read_file(ROADS_SHP)
        print(f"  - Total no Centro-Oeste: {len(roads_gdf):,} feições")
        
        # Alinhar CRS se necessário
        if roads_gdf.crs != sinop_gdf.crs:
            roads_gdf = roads_gdf.to_crs(sinop_gdf.crs)
            
        print("  - Recortando para o território de Sinop...")
        sinop_roads = gpd.clip(roads_gdf, sinop_gdf)
        print(f"  - Rodovias em Sinop: {len(sinop_roads):,} segmentos")
        
        # Salvar
        sinop_roads.to_file(OUTPUT_ROADS)
        print(f"  ✓ Salvo: {OUTPUT_ROADS.relative_to(ROOT)}")
    except Exception as e:
        print(f"  ❌ Erro ao processar rodovias: {e}")

    # 4. Processar Ferrovias (Clip)
    if RAILWAYS_SHP.exists():
        print("\n🚂 Processando Ferrovias...")
        try:
            rails_gdf = gpd.read_file(RAILWAYS_SHP)
            if rails_gdf.crs != sinop_gdf.crs:
                rails_gdf = rails_gdf.to_crs(sinop_gdf.crs)
                
            sinop_rails = gpd.clip(rails_gdf, sinop_gdf)
            print(f"  - Ferrovias em Sinop: {len(sinop_rails):,} segmentos")
            
            # Salvar
            sinop_rails.to_file(OUTPUT_RAILS)
            print(f"  ✓ Salvo: {OUTPUT_RAILS.relative_to(ROOT)}")
        except Exception as e:
            print(f"  ❌ Erro ao processar ferrovias: {e}")
    else:
        print("\n⚠️ Shapefile de ferrovias não encontrado no ZIP do Geofabrik.")

    # 5. Processar Armazéns/Silos de Grãos (Filtragem espacial + semântica de POIs)
    if POIS_SHP.exists():
        print("\n🫘 Processando Armazéns e Silos de Grãos...")
        try:
            pois_gdf = gpd.read_file(POIS_SHP)
            if pois_gdf.crs != sinop_gdf.crs:
                pois_gdf = pois_gdf.to_crs(sinop_gdf.crs)
                
            print("  - Recortando POIs para Sinop...")
            sinop_pois = gpd.clip(pois_gdf, sinop_gdf)
            
            # Filtro por nomes de tradings e palavras-chave de armazenagem
            keywords = (
                "silo|armazé|armaze|grão|grao|cooperativa|cargill|bunge|"
                "amaggi|cofco|ldc|adm|fiagril|caramuru|cereal|granjeiro|agraria|coop"
            )
            
            # Filtrar por fclass industrial/farm ou pelo nome
            mask_keywords = sinop_pois["name"].str.contains(keywords, case=False, na=False)
            mask_fclass = sinop_pois["fclass"].isin(["industrial", "farm"])
            
            sinop_silos = sinop_pois[mask_keywords | (mask_fclass & sinop_pois["name"].notna())]
            
            print(f"  - Silos e Armazéns identificados em Sinop: {len(sinop_silos)}")
            if len(sinop_silos) > 0:
                print("  - Exemplo de armazéns encontrados:")
                sample_names = sinop_silos["name"].dropna().unique()[:5]
                for name in sample_names:
                    print(f"    • {name}")
                
                # Salvar
                sinop_silos.to_file(OUTPUT_SILOS)
                print(f"  ✓ Salvo: {OUTPUT_SILOS.relative_to(ROOT)}")
            else:
                print("  ⚠️ Nenhum silo identificado com os critérios de busca.")
        except Exception as e:
            print(f"  ❌ Erro ao processar silos: {e}")
    else:
        print("\n⚠️ Shapefile de POIs (Pontos de Interesse) não localizado.")

    print("\n" + "=" * 70)
    print("✅ PROCESSAMENTO DE INFRAESTRUTURA CONCLUÍDO!")
    print("=" * 70)
    print("📍 Próximos passos:")
    print("  1. Abra o QGIS: Projeto-SINOP.qgz")
    print("  2. Adicione as novas camadas geradas em: data/malha_viaria/")
    print("     - sinop_rodovias.shp")
    print("     - sinop_ferrovias.shp")
    print("     - sinop_silos.shp")
    print()

if __name__ == "__main__":
    main()
