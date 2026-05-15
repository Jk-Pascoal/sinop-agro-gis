#!/usr/bin/env python3
"""
Instruções de Download Manual — Dados Complementares
"""

import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

DATASETS_MANUAL = {
    "1_mapbiomas": {
        "nome": "🌿 MapBiomas — Uso e Cobertura do Solo",
        "opcoes": [
            {
                "titulo": "MAIS FÁCIL: Plataforma Brasil MapBiomas",
                "url": "https://plataforma.brasil.mapbiomas.org/",
                "passos": [
                    "1. Clique em 'Downloads'",
                    "2. Selecione 'Baixar por município'",
                    "3. Estado: MT, Município: Sinop",
                    "4. Anos: 2000, 2010, 2020, 2023",
                    "5. Extraia em: data/uso_solo_mapbiomas/",
                ]
            },
            {
                "titulo": "Google Earth Engine (mais dados)",
                "url": "https://code.earthengine.google.com/",
                "passos": [
                    "1. Crie conta gratuita no Earth Engine",
                    "2. Acesse: https://bit.ly/mapbiomas-toolkit",
                    "3. Selecione MT, Sinop, anos 2000-2023",
                    "4. Clique 'Export'",
                    "5. Extraia em: data/uso_solo_mapbiomas/",
                ]
            }
        ]
    },
    "2_producao_agricola": {
        "nome": "📊 Produção Agrícola — IBGE/CONAB",
        "opcoes": [
            {
                "titulo": "SIDRA — Banco de Dados IBGE",
                "url": "https://sidra.ibge.gov.br/",
                "passos": [
                    "1. Acesse https://sidra.ibge.gov.br/",
                    "2. Busque tabela 1613 (Produção Agrícola Municipal)",
                    "3. Filtros:",
                    "   - Variável: Produção (t), Área (ha)",
                    "   - Município: Sinop/MT",
                    "   - Produto: Soja, Milho, Algodão",
                    "   - Anos: 2000-2023",
                    "4. Exporte como CSV",
                    "5. Salve em: data/producao_agricola/producao_ibge.csv",
                ]
            },
            {
                "titulo": "CONAB — Série Histórica",
                "url": "https://www.conab.gov.br/",
                "passos": [
                    "1. Acesse: https://www.conab.gov.br/info-agro",
                    "2. Seção: 'Safras e Conjuntura'",
                    "3. Busque dados históricos de Sinop/MT",
                    "4. Exporte como CSV ou Excel",
                    "5. Salve em: data/producao_agricola/",
                ]
            }
        ]
    },
    "3_malha_viaria": {
        "nome": "🛣️ Malha Viária — DNIT/OSM",
        "opcoes": [
            {
                "titulo": "DNIT — Sistema Nacional de Viação",
                "url": "https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/dnit-geo",
                "passos": [
                    "1. Acesse o site DNIT-GEO",
                    "2. Seção: Shapefiles / Download",
                    "3. Selecione: Malha Viária Federal",
                    "4. Baixe para: data/malha_viaria/",
                ]
            },
            {
                "titulo": "OpenStreetMap — Alternativa Livre",
                "url": "https://wiki.openstreetmap.org/wiki/Downloading_data",
                "passos": [
                    "1. Use Overpass Turbo: https://overpass-turbo.eu/",
                    "2. Template: 'Way highway' para MT",
                    "3. Ou use QGIS Plugin: 'QuickOSM'",
                    "4. Salve em: data/malha_viaria/",
                ]
            }
        ]
    }
}

def print_guide():
    """Imprime guia interativo."""
    print("\n" + "="*70)
    print("📥 GUIA DE DOWNLOAD MANUAL — DADOS COMPLEMENTARES")
    print("="*70)
    
    for key, dataset in DATASETS_MANUAL.items():
        print(f"\n{dataset['nome']}")
        print("─" * 70)
        
        for i, opcao in enumerate(dataset['opcoes'], 1):
            print(f"\n  Opção {i}: {opcao['titulo']}")
            print(f"  Link: {opcao['url']}")
            print("\n  Passos:")
            for passo in opcao['passos']:
                print(f"    {passo}")
    
    print("\n" + "="*70)
    print("\n📍 PRÓXIMAS ETAPAS NO QGIS:")
    print("─" * 70)
    print("""
  1. No QGIS, vá em: Camada > Adicionar Camada > Raster
  2. Selecione os arquivos .tif do MapBiomas
  3. Configure transparência e paleta de cores
  4. Crie layouts de mapa temáticos
  5. Exporte como PNG/PDF
    """)
    
    print("="*70)

if __name__ == "__main__":
    print_guide()
