#!/usr/bin/env python3
"""
processa_logistica_overpass.py
──────────────────────────────
Script alternativo e otimizado para baixar e processar a infraestrutura logística
(rodovias, ferrovias e armazéns/silos) diretamente da API Overpass do OpenStreetMap.
Isso evita o download do arquivo de 478MB do Geofabrik, executando em poucos segundos.

Uso:
    python scripts/processa_logistica_overpass.py
"""

import sys
from pathlib import Path
import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString

# ── Caminhos ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
LIMITE_DIR = DATA_DIR / "limite_municipal"
MALHA_DIR = DATA_DIR / "malha_viaria"
MALHA_DIR.mkdir(parents=True, exist_ok=True)

# Limite de Sinop
SINOP_SHP = LIMITE_DIR / "sinop_recorte.shp"

# Arquivos de Saída
OUTPUT_ROADS = MALHA_DIR / "sinop_rodovias.shp"
OUTPUT_RAILS = MALHA_DIR / "sinop_ferrovias.shp"
OUTPUT_SILOS = MALHA_DIR / "sinop_silos.shp"

def main():
    print("=" * 70)
    print("🛣️  SINOP AGRO-GIS — PROCESSAMENTO VIA OVERPASS API (OSM)")
    print("=" * 70)

    # 1. Verificar se o limite de Sinop existe
    if not SINOP_SHP.exists():
        print(f"❌ Limite de Sinop não encontrado: {SINOP_SHP}")
        print("💡 Execute os notebooks 01 e 02 para gerar o limite municipal de Sinop.")
        sys.exit(1)

    print("📍 Carregando limite municipal de Sinop...")
    sinop_gdf = gpd.read_file(SINOP_SHP)
    
    # Obter bounding box de Sinop
    # Formato total_bounds: [minx, miny, maxx, maxy]
    bounds = sinop_gdf.total_bounds
    # Formato Overpass bbox: (miny, minx, maxy, maxx)
    bbox_str = f"{bounds[1]:.8f},{bounds[0]:.8f},{bounds[3]:.8f},{bounds[2]:.8f}"
    print(f"✓ Bounding box de Sinop: {bbox_str}")

    # 2. Montar query Overpass
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json][timeout:180];
    (
      way["highway"]({bbox_str});
      way["railway"]({bbox_str});
      node["man_made"="silo"]({bbox_str});
      node["name"~"silo|armazem|armazé|cargill|bunge|amaggi|cofco|adm|fiagril|caramuru",i]({bbox_str});
    );
    out body;
    >;
    out skel qt;
    """

    print("\n🌐 Conectando à Overpass API e baixando dados (isso leva poucos segundos)...")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.post(overpass_url, data={'data': overpass_query}, headers=headers, timeout=60)
        if response.status_code != 200:
            print(f"❌ Erro na API Overpass: Código {response.status_code}")
            sys.exit(1)
            
        data = response.json()
        print(f"✓ Dados baixados com sucesso. Total de elementos: {len(data.get('elements', [])):,}")
    except Exception as e:
        print(f"❌ Erro de conexão com a API Overpass: {e}")
        sys.exit(1)

    # 3. Mapear nós por ID
    print("\n🔍 Processando coordenadas e geometrias...")
    nodes = {}
    for element in data.get('elements', []):
        if element['type'] == 'node':
            nodes[element['id']] = (element['lon'], element['lat'])

    # 4. Criar listas de feições para GeoPandas
    roads_list = []
    rails_list = []
    silos_list = []

    for element in data.get('elements', []):
        if element['type'] == 'way':
            way_nodes = element.get('nodes', [])
            coords = [nodes[node_id] for node_id in way_nodes if node_id in nodes]
            if len(coords) < 2:
                continue
            geom = LineString(coords)
            tags = element.get('tags', {})
            
            if 'highway' in tags:
                roads_list.append({
                    'geometry': geom,
                    'name': tags.get('ref', tags.get('name', 'Estrada sem nome')),
                    'highway': tags.get('highway', ''),
                    'surface': tags.get('surface', 'unpaved'),
                    'ref': tags.get('ref', '')
                })
            elif 'railway' in tags:
                rails_list.append({
                    'geometry': geom,
                    'name': tags.get('name', 'Ferrovia'),
                    'railway': tags.get('railway', '')
                })
                
        elif element['type'] == 'node':
            tags = element.get('tags', {})
            if tags:
                geom = Point(element['lon'], element['lat'])
                silos_list.append({
                    'geometry': geom,
                    'name': tags.get('name', 'Silo/Armazém'),
                    'man_made': tags.get('man_made', ''),
                    'amenity': tags.get('amenity', ''),
                    'operator': tags.get('operator', '')
                })

    # 5. Converter e recortar (Clip) para Sinop
    print("\n✂️ Aplicando recorte espacial (Clip) no polígono de Sinop...")
    
    # Rodovias
    if roads_list:
        roads_gdf = gpd.GeoDataFrame(roads_list, crs="EPSG:4326")
        if roads_gdf.crs != sinop_gdf.crs:
            roads_gdf = roads_gdf.to_crs(sinop_gdf.crs)
        sinop_roads = gpd.clip(roads_gdf, sinop_gdf)
        
        # Salvar
        sinop_roads.to_file(OUTPUT_ROADS)
        print(f"  ✓ Rodovias salvas ({len(sinop_roads)} trechos): {OUTPUT_ROADS.relative_to(ROOT)}")
    else:
        print("  ⚠️ Nenhuma rodovia encontrada.")

    # Ferrovias
    if rails_list:
        rails_gdf = gpd.GeoDataFrame(rails_list, crs="EPSG:4326")
        if rails_gdf.crs != sinop_gdf.crs:
            rails_gdf = rails_gdf.to_crs(sinop_gdf.crs)
        sinop_rails = gpd.clip(rails_gdf, sinop_gdf)
        
        if len(sinop_rails) > 0:
            sinop_rails.to_file(OUTPUT_RAILS)
            print(f"  ✓ Ferrovias salvas ({len(sinop_rails)} trechos): {OUTPUT_RAILS.relative_to(ROOT)}")
        else:
            print("  ⚠️ Nenhuma ferrovia cruza o limite de Sinop.")
    else:
        print("  ⚠️ Nenhuma ferrovia encontrada na bounding box.")

    # Silos
    if silos_list:
        silos_gdf = gpd.GeoDataFrame(silos_list, crs="EPSG:4326")
        if silos_gdf.crs != sinop_gdf.crs:
            silos_gdf = silos_gdf.to_crs(sinop_gdf.crs)
        sinop_silos = gpd.clip(silos_gdf, sinop_gdf)
        
        if len(sinop_silos) > 0:
            sinop_silos.to_file(OUTPUT_SILOS)
            print(f"  ✓ Silos/Armazéns salvos ({len(sinop_silos)} pontos): {OUTPUT_SILOS.relative_to(ROOT)}")
            print("  - Exemplos encontrados:")
            names = sinop_silos["name"].dropna().unique()[:5]
            for n in names:
                print(f"    • {n}")
        else:
            print("  ⚠️ Nenhum silo identificado com os critérios dentro de Sinop.")
    else:
        print("  ⚠️ Nenhum silo encontrado na bounding box.")

    print("\n" + "=" * 70)
    print("✅ INTEGRAÇÃO LOGÍSTICA VIA OVERPASS CONCLUÍDA!")
    print("=" * 70)

if __name__ == "__main__":
    main()
