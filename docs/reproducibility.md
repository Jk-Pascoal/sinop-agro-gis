# Guia de Reprodutibilidade — Sinop Agro-GIS

Este documento fornece as instruções passo a passo para configurar o ambiente de desenvolvimento, instalar as dependências necessárias, executar os notebooks de análise e abrir o projeto geoespacial no QGIS de forma consistente no sistema operacional **Windows**.

---

## 🐍 1. Configurando o Ambiente Virtual Python (Windows)

Para evitar conflitos de versões e garantir o isolamento das bibliotecas geoespaciais, é recomendada a criação de um ambiente virtual (`venv`):

1. Abra o terminal (PowerShell ou CMD) na pasta raiz do projeto:
   ```powershell
   cd C:\Users\Administrador\Documents\Projeto-SINOP
   ```

2. Crie o ambiente virtual:
   ```powershell
   python -m venv .venv
   ```

3. Ative o ambiente virtual no Windows:
   - **No PowerShell:**
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **No Prompt de Comando (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```

   *Nota:* Se receber uma mensagem de erro de restrição de execução de scripts no PowerShell, execute antes: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.

---

## 📦 2. Instalação de Dependências

Com o ambiente virtual ativado, instale todas as dependências requeridas utilizando o arquivo [requirements.txt](file:///C:/Users/Administrador/Documents/Projeto-SINOP/requirements.txt):

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

> [!IMPORTANT]
> As bibliotecas GIS como `geopandas`, `shapely`, `fiona` e `rasterio` exigem binários específicos de C++ (como GDAL, GEOS e PROJ). No Windows, a instalação via `pip` geralmente baixa rodas binárias (*wheels*) pré-compiladas automaticamente. Se encontrar problemas ao compilar algum pacote, certifique-se de que possui o Microsoft Visual C++ Build Tools instalado ou utilize o ambiente Anaconda/Miniconda como alternativa.

---

## 📓 3. Execução dos Notebooks de Análise

Os notebooks estão numerados cronologicamente na pasta `notebooks/`. Para executá-los:

1. Inicie a interface do Jupyter:
   ```powershell
   jupyter notebook
   ```

2. O navegador padrão será aberto na interface do Jupyter. Navegue até a pasta `notebooks/` e execute-os na seguinte ordem recomendada:
   - [01_processamento.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/01_processamento.ipynb): Limpeza preliminar e validação.
   - [02_analise_espacial.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/02_analise_espacial.ipynb): Recorte territorial e geração do shapefile de Sinop.
   - [03_visualizacao.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/03_visualizacao.ipynb): Renderização do mapa interativo interativo web.
   - [04_dados_reais_mapbiomas.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/04_dados_reais_mapbiomas.ipynb): Leitura de estatísticas de cobertura do solo.
   - [05_producao_ibge_sidra.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/05_producao_ibge_sidra.ipynb): Análise histórica das safras de soja e milho.
   - [06_analise_temporal.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/06_analise_temporal.ipynb): Correlação espacial, taxas de expansão agrícola e desmatamento.
   - [07_logistica_infraestrutura.ipynb](file:///C:/Users/Administrador/Documents/Projeto-SINOP/notebooks/07_logistica_infraestrutura.ipynb): Métricas viárias e densidade de escoamento logístico.

---

## 🗺️ 4. Abrindo o Projeto no QGIS

O arquivo de projeto do QGIS está localizado em `qgis_project/Projeto-SINOP.qgz`.

1. Abra o software **QGIS** (versão 3.22 LTR ou superior recomendada).
2. Vá ao menu superior `Projeto` > `Abrir...` (ou atalho `Ctrl + O`).
3. Navegue até a pasta [qgis_project/](file:///C:/Users/Administrador/Documents/Projeto-SINOP/qgis_project/) e selecione o arquivo `Projeto-SINOP.qgz`.
4. As camadas de vetores municipais e rasters do MapBiomas serão carregadas automaticamente.
   *Nota:* As camadas estão configuradas com caminhos relativos ao arquivo do projeto. Como movemos o projeto para a pasta `qgis_project/`, o QGIS resolverá os caminhos apontando corretamente para as subpastas em `../data/`.

---

## 💾 5. Dados Grandes e Versionamento (Git)

> [!WARNING]
> Arquivos raster de alta resolução (`.tif`) e shapefiles pesados de malha regional (`.zip` e `.shp`) possuem tamanhos elevados e não são versionados por completo no repositório Git para evitar estouro de limite de cota do GitHub.
> 
> Caso clone o repositório em outra máquina e as pastas de dados estejam sem os arquivos fontes básicos:
> 1. Execute o script automatizado para recuperar dados de limites e redes básicas:
>    ```powershell
>    python scripts/download_dados.py
>    ```
> 2. Para obter os recortes raster originais do MapBiomas e as séries detalhadas do IBGE, siga as instruções em [scripts/guia_download_manual.py](file:///C:/Users/Administrador/Documents/Projeto-SINOP/scripts/guia_download_manual.py) ou execute:
>    ```powershell
>    python scripts/guia_download_manual.py
>    ```
