#!/usr/bin/env python3
"""
check_project_structure.py
──────────────────────────
Script de verificação para validar a padronização e integridade
da estrutura de pastas, arquivos e documentações do projeto Sinop Agro-GIS.
"""

import sys
from pathlib import Path

# Raiz do projeto (uma pasta acima de scripts/)
ROOT = Path(__file__).resolve().parent.parent

# Pastas obrigatórias
REQUIRED_DIRS = [
    "data/raw",
    "data/processed",
    "data/external",
    "docs",
    "maps/exportados",
    "notebooks",
    "scripts",
    "qgis_project",
    "assets",
]

# Arquivos essenciais obrigatórios
REQUIRED_FILES = [
    "requirements.txt",
    "README.md",
    "index.html",
    ".gitignore",
    "qgis_project/Projeto-SINOP.qgz",
    "docs/methodology.md",
    "docs/data_dictionary.md",
    "docs/reproducibility.md",
    "docs/limitations.md",
    "data/processed/metricas_finais_template.csv",
]

def main():
    print("=" * 70)
    print(" VERIFICADOR DE ESTRUTURA - SINOP AGRO-GIS ")
    print("=" * 70)
    print(f"Raiz do Projeto: {ROOT}\n")

    errors = 0
    warnings = 0

    print("--- Verificando Diretorios Principais ---")
    for dir_rel in REQUIRED_DIRS:
        dir_path = ROOT / dir_rel
        if dir_path.is_dir():
            print(f"  [OK] Diretorio existe: {dir_rel}")
        else:
            print(f"  [ERRO] Diretorio AUSENTE: {dir_rel}")
            errors += 1
            
    print("\n--- Verificando Arquivos Mandatorios ---")
    for file_rel in REQUIRED_FILES:
        file_path = ROOT / file_rel
        if file_path.is_file():
            print(f"  [OK] Arquivo existe: {file_rel}")
        else:
            print(f"  [ERRO] Arquivo AUSENTE: {file_rel}")
            errors += 1

    # Verificações adicionais
    print("\n--- Validacoes Adicionais ---")
    
    # 1. Verificar se Projeto-SINOP.qgz está na raiz
    qgz_root = ROOT / "Projeto-SINOP.qgz"
    if qgz_root.exists():
        print("  [AVISO] Projeto-SINOP.qgz localizado na raiz! Deveria estar em qgis_project/")
        warnings += 1
    else:
        print("  [OK] Projeto-SINOP.qgz nao esta na raiz.")

    # 2. Verificar se gitignore ignora docs
    gitignore = ROOT / ".gitignore"
    if gitignore.is_file():
        content = gitignore.read_text(encoding="utf-8")
        if "docs/" in content and not "# docs/" in content:
            lines = [l.strip() for l in content.splitlines() if l.strip()]
            if any(l == "docs" or l == "docs/" for l in lines):
                print("  [ERRO] O arquivo .gitignore esta ignorando docs/")
                errors += 1
            else:
                print("  [OK] O arquivo .gitignore nao ignora docs/.")
        else:
            print("  [OK] O arquivo .gitignore nao ignora docs/.")

    # Resumo final
    print("\n" + "=" * 70)
    print(" RELATORIO FINAL DA VERIFICACAO ")
    print("=" * 70)
    print(f"  Total de Erros criticos: {errors}")
    print(f"  Total de Avisos: {warnings}")
    print("-" * 70)
    
    if errors == 0:
        print("  PARABENS! O projeto cumpre todos os criterios de portfolio profissional!")
        print("  Pronto para publicacao, reproduzivel e bem documentado.")
        sys.exit(0)
    else:
        print("  FALHA! Algumas inconsistencias estruturais foram identificadas.")
        print("  Revise a lista de erros e mova/crie os arquivos necessarios.")
        sys.exit(1)

if __name__ == "__main__":
    main()
