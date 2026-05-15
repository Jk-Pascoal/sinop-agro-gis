"""
export_post_images.py  —  3 imagens para o 2º post LinkedIn
  03_uso_solo_barras_sinop.png  — barras horizontais (13 classes)
  04_kpi_sinop.png              — infográfico de KPIs (canvas limpo)
  05_treemap_sinop.png          — treemap proporcional
Uso:  python scripts/export_post_images.py
"""
from pathlib import Path
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parent.parent
OUT  = ROOT / "maps" / "exportados"
OUT.mkdir(parents=True, exist_ok=True)

TOTAL   = 399_085.86
SIGN    = "Jakson Pascoal  ·  github.com/Jk-Pascoal  ·  Sinop-MT"
FONTE   = "Fonte: MapBiomas Collection 10.1  ·  IBGE Malha Municipal 2022  ·  Projeto: sinop-agro-gis"
BG      = "#0a0a0f"

def fmt(v):
    return f"{v/1000:.1f}k ha" if v >= 1000 else f"{v:.0f} ha"
def pct(v):
    return f"{v/TOTAL*100:.1f}%"
def ann(text, x, y, size=12, color="#aaa", **kw):
    return dict(text=text, x=x, y=y, xref="paper", yref="paper",
                showarrow=False, xanchor=kw.pop("xa","center"),
                yanchor=kw.pop("ya","middle"),
                font=dict(size=size, color=color, family="Arial"), **kw)

classes = [
    ("Soja",              169_851.83, "#c084fc"),
    ("Floresta Nativa",   129_179.01, "#16a34a"),
    ("Pastagem",           30_132.11, "#ca8a04"),
    ("Outras Lavouras",    28_619.36, "#e879f9"),
    ("Floresta Aluvial",   15_470.66, "#0d9488"),
    ("Rios e Lagos",       13_386.03, "#3b82f6"),
    ("Área Urbana",         8_938.24, "#ef4444"),
    ("Outras Áreas",        1_635.16, "#a8a29e"),
    ("Área Úmida",          1_306.50, "#2dd4bf"),
    ("Plantio Florestal",     410.34, "#78716c"),
    ("Algodão",               122.93, "#d8b4fe"),
    ("Campo Natural",          31.08, "#fde68a"),
    ("Savana Arbórea",          2.63, "#4ade80"),
]

# ══════════════════════════════════════════════════════════════════
# IMG 1 — Barras Horizontais (13 classes)
# ══════════════════════════════════════════════════════════════════
print("📊 [1/3] Barras horizontais...")

bar = go.Bar(
    orientation="h",
    y=[c[0] for c in classes],
    x=[c[1] for c in classes],
    marker=dict(color=[c[2] for c in classes],
                line=dict(color=BG, width=1.5)),
    text=[f"  {fmt(c[1])}  ({pct(c[1])})" for c in classes],
    textposition="outside",
    textfont=dict(size=13, family="Arial", color="#888"),
    cliponaxis=False,
)

fig1 = go.Figure(data=[bar])
fig1.update_layout(
    paper_bgcolor=BG, plot_bgcolor=BG,
    margin=dict(t=140, b=80, l=160, r=220),
    width=1200, height=860,
    showlegend=False,
    xaxis=dict(showgrid=True, gridcolor="#1a1a26", zeroline=False,
               showticklabels=False, showline=False, range=[0, 240000]),
    yaxis=dict(autorange="reversed",
               tickfont=dict(size=13, color="#ccc", family="Arial"),
               showgrid=False, showline=False, ticksuffix="  "),
    bargap=0.30,
    annotations=[
        ann("<b>Como Sinop usa seus 399 mil hectares</b>",
            0.5, 1.10, 21, "#fff"),
        ann("MapBiomas Collection 10.1  ·  Resolução 30m  ·  Ano base 2024  ·  Sinop, MT",
            0.5, 1.055, 12, "#555"),
        ann(f"<b style='color:#4ade80'>{SIGN}</b>",
            0.5, -0.07, 12, "#4ade80", ya="top"),
        ann(FONTE, 0.5, -0.10, 10, "#333", ya="top"),
    ],
)

o1 = OUT / "03_uso_solo_barras_sinop.png"
fig1.write_image(str(o1), format="png", width=1200, height=860, scale=2)
print(f"   ✅ {o1.name}  ({o1.stat().st_size/1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════════
# IMG 2 — Card de KPIs (canvas em branco, sem traces de dados)
# Layout: grade 2×2 com 4 KPIs grandes + barra de proporção
# ══════════════════════════════════════════════════════════════════
print("\n📊 [2/3] Card de KPIs...")

# Usamos scatter invisível apenas para definir o espaço do plot
dummy = go.Scatter(x=[0, 1], y=[0, 1], mode="markers",
                   marker=dict(opacity=0), showlegend=False)

# ── 4 KPI cards posicionados em grade 2x2 ─────────────────────
# Coordenadas em espaço de paper (0–1)
kpi_data = [
    # label,          valor,   sub,           cor,      x,    y
    ("🌿 FLORESTA",   "36,2%", "144.652 ha",  "#16a34a", 0.25, 0.72),
    ("🌾 AGROPEC.",   "57,4%", "229.137 ha",  "#c084fc", 0.75, 0.72),
    ("🫘 SOJA",       "42,6%", "169.852 ha",  "#a855f7", 0.25, 0.38),
    ("🏙️ URBANO",    " 2,2%", "8.938 ha",    "#ef4444", 0.75, 0.38),
]

kpi_annotations = []
for label, valor, sub, cor, x, y in kpi_data:
    kpi_annotations += [
        # Caixa de fundo — simulada com bgcolor na anotação
        ann(
            f"<b style='font-size:13px;color:{cor}'>{label}</b><br>"
            f"<b style='font-size:54px;color:#ffffff'>{valor}</b><br>"
            f"<span style='font-size:15px;color:#888'>{sub}</span>",
            x, y, size=13, color="#aaa",
            bgcolor="#111118", bordercolor=cor, borderwidth=2, borderpad=28,
        ),
    ]

# Linha divisória central (visual via anotações de linha)
# Barra de proporção na parte inferior do card
prop_ann = [
    ann("<b>Distribuição do território</b>", 0.5, 0.12, 11, "#444"),
]

all_ann = [
    # Título
    ann("<b>Sinop, MT — Uso do Solo 2024</b>", 0.5, 0.97, 28, "#fff"),
    ann("399.085 hectares mapeados pixel a pixel (30m/px) · MapBiomas", 0.5, 0.91, 13, "#555"),
] + kpi_annotations + [
    ann(f"<b style='color:#4ade80'>{SIGN}</b>", 0.5, 0.04, 13, "#4ade80"),
    ann(FONTE, 0.5, 0.01, 10, "#333"),
]

fig2 = go.Figure(data=[dummy])
fig2.update_layout(
    paper_bgcolor=BG, plot_bgcolor=BG,
    margin=dict(t=0, b=0, l=0, r=0),
    width=1000, height=1000,
    showlegend=False,
    xaxis=dict(visible=False, range=[0, 1]),
    yaxis=dict(visible=False, range=[0, 1]),
    annotations=all_ann,
)

# Adicionar shapes para linhas divisórias
fig2.update_layout(
    shapes=[
        # Linha vertical central
        dict(type="line", x0=0.5, x1=0.5, y0=0.20, y1=0.88,
             xref="paper", yref="paper",
             line=dict(color="#1a1a2e", width=1.5)),
        # Linha horizontal central
        dict(type="line", x0=0.08, x1=0.92, y0=0.545, y1=0.545,
             xref="paper", yref="paper",
             line=dict(color="#1a1a2e", width=1.5)),
        # Borda do card
        dict(type="rect", x0=0.04, x1=0.96, y0=0.08, y1=0.90,
             xref="paper", yref="paper",
             line=dict(color="#1a1a2e", width=1),
             fillcolor="rgba(0,0,0,0)"),
    ]
)

o2 = OUT / "04_kpi_sinop.png"
fig2.write_image(str(o2), format="png", width=1000, height=1000, scale=2)
print(f"   ✅ {o2.name}  ({o2.stat().st_size/1024:.0f} KB)")


# ══════════════════════════════════════════════════════════════════
# IMG 3 — Treemap Proporcional
# ══════════════════════════════════════════════════════════════════
print("\n📊 [3/3] Treemap...")

cats = [
    ("Soja",            169_851.83, "#a855f7"),
    ("Floresta Nativa", 129_179.01, "#16a34a"),
    ("Pastagem",         30_132.11, "#ca8a04"),
    ("Outras Lavouras",  28_619.36, "#e879f9"),
    ("Fl. Aluvial",      15_470.66, "#0d9488"),
    ("Rios e Lagos",     13_386.03, "#3b82f6"),
    ("Área Urbana",       8_938.24, "#ef4444"),
    ("Outros",            3_126.56, "#374151"),
]

tree = go.Treemap(
    labels=[c[0] for c in cats],
    parents=[""] * len(cats),
    values=[c[1] for c in cats],
    marker=dict(
        colors=[c[2] for c in cats],
        line=dict(width=4, color=BG),
    ),
    texttemplate="<b>%{label}</b><br>%{percentRoot:.1%}",
    textfont=dict(size=14, family="Arial", color="#fff"),
    pathbar=dict(visible=False),
    hoverinfo="skip",
)

fig3 = go.Figure(data=[tree])
fig3.update_layout(
    paper_bgcolor=BG,
    margin=dict(t=110, b=80, l=10, r=10),
    width=900, height=960,
    annotations=[
        ann("<b>Sinop, MT — Uso do Solo 2024</b>", 0.5, 1.10, 23, "#fff"),
        ann("399.085 ha  ·  MapBiomas Collection 10.1  ·  Resolução 30m",
            0.5, 1.055, 12, "#555"),
        ann(f"<b>{SIGN}</b>", 0.5, -0.06, 12, "#4ade80", ya="top"),
        ann(FONTE, 0.5, -0.085, 10, "#333", ya="top"),
    ],
)

o3 = OUT / "05_treemap_sinop.png"
fig3.write_image(str(o3), format="png", width=900, height=960, scale=2)
print(f"   ✅ {o3.name}  ({o3.stat().st_size/1024:.0f} KB)")


print(f"""
╔══════════════════════════════════════════════════════════╗
║  ✅  3 imagens geradas com sucesso!                      ║
╠══════════════════════════════════════════════════════════╣
║  📊  03_uso_solo_barras_sinop.png  — 13 classes          ║
║  🟦  04_kpi_sinop.png             — 4 KPIs (2×2)        ║
║  🟩  05_treemap_sinop.png         — treemap              ║
╠══════════════════════════════════════════════════════════╣
║  ✍️   Jakson Pascoal · github.com/Jk-Pascoal em todas  ║
╚══════════════════════════════════════════════════════════╝
Pasta: {OUT}
""")
