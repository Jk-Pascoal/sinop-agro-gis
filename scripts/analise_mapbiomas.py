#!/usr/bin/env python3
"""
analise_mapbiomas.py
────────────────────
Script para análise rápida do MapBiomas Sinop 2023.
Gera estatísticas de cobertura do solo.
"""

import rasterio
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────────────────────────────────────

ROOT = Path.cwd().parent if Path.cwd().name == 'scripts' else Path.cwd()
RASTER_FILE = ROOT / "data" / "uso_solo_mapbiomas" / "MapBiomas_Sinop_2023.tif"

# Mapeamento de códigos MapBiomas para nomes legíveis
MAPBIOMAS_CLASSES = {
    1: "Floresta",
    2: "Savana",
    3: "Pastagem",
    4: "Área urbana",
    5: "Agricultura",
    6: "Corpo d'água",
    7: "Afloramento rochoso",
    8: "Não vegetado",
    9: "Campo",
    10: "Floresta plantada",
    11: "Zona úmida",
    12: "Mangue",
    13: "Praia/duna",
    14: "Delta",
    15: "Cultivo aquático",
}

# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÕES
# ─────────────────────────────────────────────────────────────────────────────

def analisar_raster(caminho_raster):
    """Analisa um raster GeoTIFF do MapBiomas."""
    
    if not caminho_raster.exists():
        print(f"❌ Arquivo não encontrado: {caminho_raster}")
        return None
    
    print(f"📊 Analisando: {caminho_raster.name}")
    print("─" * 70)
    
    with rasterio.open(caminho_raster) as src:
        # Informações básicas
        print(f"\n📋 Informações do Raster:")
        print(f"  Dimensões: {src.width} × {src.height} pixels")
        print(f"  Bandas: {src.count}")
        print(f"  CRS: {src.crs}")
        print(f"  Resolução: {src.res}")
        
        # Ler dados
        data = src.read(1)  # Banda 1
        
        # Estatísticas
        print(f"\n🔍 Estatísticas de Valores:")
        print(f"  Min: {data.min()}")
        print(f"  Max: {data.max()}")
        print(f"  Média: {data.mean():.2f}")
        print(f"  Mediana: {np.median(data):.2f}")
        
        # Contar frequência de valores
        valores_unicos = Counter(data.flatten())
        
        print(f"\n📊 Distribuição de Classes ({len(valores_unicos)} classes):")
        print("─" * 70)
        print(f"{'Código':<8} {'Classe':<30} {'Pixels':<15} {'%':<8}")
        print("─" * 70)
        
        total_pixels = data.size
        
        # DataFrame para tabela melhor
        dados_classe = []
        
        for codigo in sorted(valores_unicos.keys()):
            if codigo == 0:
                continue  # Pula NoData (0)
            
            pixels = valores_unicos[codigo]
            percentual = (pixels / total_pixels) * 100
            nome_classe = MAPBIOMAS_CLASSES.get(codigo, "Desconhecido")
            
            print(f"{codigo:<8} {nome_classe:<30} {pixels:<15} {percentual:>6.2f}%")
            
            dados_classe.append({
                'Código': codigo,
                'Classe': nome_classe,
                'Pixels': pixels,
                'Percentual (%)': round(percentual, 2),
                'Área (km²)': round((pixels * src.res[0] * src.res[1]) / 1e6, 2)
            })
        
        print("─" * 70)
        
        # Criar DataFrame
        df = pd.DataFrame(dados_classe)
        
        # Salvar como CSV
        output_csv = ROOT / "data" / "uso_solo_mapbiomas" / "estatisticas_sinop_2023.csv"
        df.to_csv(output_csv, index=False)
        print(f"\n✅ Estatísticas salvas: {output_csv.name}")
        
        # Gráfico resumido
        print(f"\n📈 Resumo de Cobertura:")
        print(f"  Total de pixels: {total_pixels:,}")
        print(f"  Classes mapeadas: {len(dados_classe)}")
        print(f"  Área total: {(total_pixels * src.res[0] * src.res[1]) / 1e6:.2f} km²")
        
        # Top 5 classes
        print(f"\n🏆 Top 5 classes:")
        for i, row in df.nlargest(5, 'Pixels').iterrows():
            print(f"  {i+1}. {row['Classe']}: {row['Percentual (%)']:.1f}%")
        
        return df

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("🌍 ANÁLISE MAPBIOMAS — SINOP 2023")
    print("=" * 70)
    
    df_stats = analisar_raster(RASTER_FILE)
    
    print("\n" + "=" * 70)
    print("✅ ANÁLISE CONCLUÍDA!")
    print("=" * 70)
    
    if df_stats is not None:
        print(f"\n💾 Dados salvos em: data/uso_solo_mapbiomas/estatisticas_sinop_2023.csv")
        print(f"\n📊 Use o notebook 01_processamento.ipynb para visualizações!")
