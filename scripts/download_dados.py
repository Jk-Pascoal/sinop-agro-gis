#!/usr/bin/env python3
"""
download_dados.py
─────────────────
Script para baixar automaticamente os dados geoespaciais do projeto SINOP Agro-GIS.

Dados baixados:
  1. Limites Municipais (IBGE) — shapefiles de MT
  2. Malha Viária (OpenStreetMap/Geofabrik) — rodovias e ferrovias
  3. Guia para MapBiomas (requer download manual ou GEE)

Uso:
    python scripts/download_dados.py
"""

import os
import sys
import zipfile
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Criar estrutura de diretórios
DIRS_TO_CREATE = [
    DATA_DIR / "limite_municipal",
    DATA_DIR / "uso_solo_mapbiomas",
    DATA_DIR / "malha_viaria",
    DATA_DIR / "producao_agricola",
]

DOWNLOADS = [
    {
        "name": "Limites Municipais — Mato Grosso (IBGE 2022)",
        "url": "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/MT/MT_Municipios_2022.zip",
        "target_dir": DATA_DIR / "limite_municipal",
        "extract": True,
    },
    {
        "name": "Malha Viária — Centro-Oeste (OpenStreetMap via Geofabrik)",
        "url": "https://download.geofabrik.de/south-america/brazil/centro-oeste-latest-free.shp.zip",
        "target_dir": DATA_DIR / "malha_viaria",
        "extract": True,
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÕES
# ─────────────────────────────────────────────────────────────────────────────

def create_directories():
    """Cria estrutura de diretórios."""
    print("\n📁 Criando diretórios...\n")
    for dir_path in DIRS_TO_CREATE:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {dir_path.relative_to(ROOT)}")

def download_file(url, output_path):
    """Baixa um arquivo com barra de progresso."""
    try:
        print(f"  Conectando a {url.split('/')[2]}...")
        with urlopen(url) as response:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            chunk_size = 1024 * 1024  # 1 MB
            
            with open(output_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        mb = downloaded / (1024 * 1024)
                        print(f"    ↳ {mb:.1f} MB ({percent:.0f}%)", end='\r')
        
        print(f"\n  ✓ Baixado: {output_path.name}")
        return True
    
    except URLError as e:
        print(f"\n  ❌ Erro ao conectar: {e}")
        return False
    except Exception as e:
        print(f"\n  ❌ Erro: {e}")
        return False

def extract_zip(zip_path, target_dir):
    """Extrai arquivo ZIP."""
    try:
        print(f"  Extraindo {zip_path.name}...")
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(target_dir)
        print(f"  ✓ Extraído para {target_dir.relative_to(ROOT)}")
        return True
    except Exception as e:
        print(f"  ❌ Erro ao extrair: {e}")
        return False

def download_datasets():
    """Baixa todos os datasets."""
    print("\n🌍 Iniciando downloads...\n")
    
    for i, dataset in enumerate(DOWNLOADS, 1):
        print(f"[{i}/{len(DOWNLOADS)}] {dataset['name']}")
        
        target_dir = dataset["target_dir"]
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Nome do arquivo temporário
        zip_filename = dataset["url"].split('/')[-1]
        zip_path = target_dir / zip_filename
        
        # Pula se já baixado
        if zip_path.exists():
            print(f"  ⚠️  Arquivo já existe: {zip_filename}")
            if dataset["extract"]:
                extract_zip(zip_path, target_dir)
            continue
        
        # Baixa o arquivo
        if download_file(dataset["url"], zip_path):
            if dataset["extract"]:
                extract_zip(zip_path, target_dir)
                # Opcionalmente remove o ZIP após extrair
                # zip_path.unlink()
        
        print()

def create_mapbiomas_guide():
    """Cria guia para download manual de MapBiomas."""
    guide_path = DATA_DIR / "MAPBIOMAS_DOWNLOAD.txt"
    
    guide_content = """🌿 MAPBIOMAS — DOWNLOAD MANUAL
═════════════════════════════════════════════════════════════════════

O MapBiomas exige autenticação ou acesso via Google Earth Engine.
Siga UMA das opções abaixo:

OPÇÃO 1️⃣ — MAIS FÁCIL (Plataforma Brasil MapBiomas)
──────────────────────────────────────────────────────
1. Acesse: https://plataforma.brasil.mapbiomas.org/
2. Clique em "Downloads"
3. Selecione "Baixar por município"
4. Escolha: Estado = MT, Município = Sinop
5. Selecione anos: 2000, 2010, 2020, 2023
6. Baixe os arquivos GeoTIFF
7. Extraia em: data/uso_solo_mapbiomas/

OPÇÃO 2️⃣ — GOOGLE EARTH ENGINE (Mais dados, requer conta Google)
────────────────────────────────────────────────────────────────
1. Crie conta gratuita: https://code.earthengine.google.com/
2. Acesse o Toolkit: https://bit.ly/mapbiomas-toolkit
3. Selecione:
   - Estado: Mato Grosso
   - Município: Sinop
   - Anos: 2000, 2010, 2020, 2023
4. Clique em "Export"
5. Baixe os arquivos
6. Extraia em: data/uso_solo_mapbiomas/

OPÇÃO 3️⃣ — VIA SCRIPT (Para especialistas)
──────────────────────────────────────────
Use o repositório: https://github.com/mapbiomas-brazil/user-toolkit
Siga as instruções do README para Python/R

📝 DEPOIS DE BAIXAR:
───────────────────
1. Abra o QGIS
2. Menu: Camada > Adicionar camada > Raster
3. Selecione os arquivos GeoTIFF
4. Organize as camadas por ano

═════════════════════════════════════════════════════════════════════
"""
    
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print(f"\n📋 Guia criado: {guide_path.relative_to(ROOT)}")

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("📥 SINOP AGRO-GIS — DOWNLOAD DE DADOS GEOESPACIAIS")
    print("=" * 70)
    
    try:
        # Cria diretórios
        create_directories()
        
        # Baixa datasets
        download_datasets()
        
        # Cria guia para MapBiomas
        create_mapbiomas_guide()
        
        print("\n" + "=" * 70)
        print("✅ DOWNLOAD CONCLUÍDO!")
        print("=" * 70)
        print("\n📍 Próximos passos:")
        print("  1. Baixe MapBiomas manualmente (veja guia em data/)")
        print("  2. Abra QGIS: Projeto-SINOP.qgz")
        print("  3. Adicione as camadas em: Camada > Adicionar camada")
        print("  4. Organize na árvore de camadas do QGIS")
        print()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelado pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erro geral: {e}")
        sys.exit(1)
