"""
export_chart_png.py
───────────────────
Exporta o gráfico de Uso do Solo (Sinop-MT) como PNG de alta resolução.
Usa Plotly Python + Kaleido — sem necessidade de browser ou Playwright.

Requisitos (instale se ainda não tiver):
    pip install plotly kaleido

Saída:
    maps/exportados/02_uso_solo_sinop_2024.png  (2400 × 1600 px)

Uso:
    python scripts/export_chart_png.py
"""

from pathlib import Path

# ── Verificação de dependências ────────────────────────────────────────────────
try:
    import plotly.graph_objects as go
except ImportError:
    raise SystemExit("❌ plotly não instalado. Execute: pip install plotly kaleido")

try:
    import kaleido  # noqa: F401
except ImportError:
    raise SystemExit("❌ kaleido não instalado. Execute: pip install kaleido")

# ── Caminhos ──────────────────────────────────────────────────────────────────
ROOT       = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "maps" / "exportados"
OUTPUT_PNG = OUTPUT_DIR / "02_uso_solo_sinop_2024.png"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Dados (espelho exato do HTML) ─────────────────────────────────────────────
TOTAL_AREA = 399_085.86  # ha

inner = [
    {"label": "Floresta",       "value": 144_652.29, "color": "#1a7a3c"},
    {"label": "Herb./Arbustiva","value":   1_337.57, "color": "#45c2a5"},
    {"label": "Agropecuária",   "value": 229_136.56, "color": "#E974ED"},
    {"label": "Área não veg.",  "value":  10_573.40, "color": "#d4271e"},
    {"label": "Água",           "value":  13_386.03, "color": "#2532E4"},
]

outer = [
    # Floresta
    {"label": "Floresta Nativa",   "value": 129_179.01, "color": "#1F8D49"},
    {"label": "Floresta Aluvial",  "value":  15_470.66, "color": "#519799"},
    {"label": "Savana Arbórea",    "value":       2.63, "color": "#7DC975"},
    # Herb./Arbustiva
    {"label": "Campo Natural",     "value":      31.08, "color": "#d6bc74"},
    {"label": "Área Úmida",        "value":   1_306.50, "color": "#45C2A5"},
    # Agropecuária
    {"label": "Soja",              "value": 169_851.83, "color": "#E974ED"},
    {"label": "Algodão",           "value":     122.93, "color": "#c27ba0"},
    {"label": "Outras Lavouras",   "value":  28_619.36, "color": "#e8c3e8"},
    {"label": "Plantio Florestal", "value":     410.34, "color": "#7a5c58"},
    {"label": "Pastagem",          "value":  30_132.11, "color": "#BBB35A"},
    # Área não veg.
    {"label": "Área Urbana",       "value":   8_938.24, "color": "#DB4040"},
    {"label": "Outras Áreas",      "value":   1_635.16, "color": "#b0a090"},
    # Água
    {"label": "Rios e Lagos",      "value":  13_386.03, "color": "#2532E4"},
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def fmt_ha(v):
    return f"{v/1000:.1f}k ha" if v >= 1000 else f"{v:.0f} ha"

def fmt_pct(v):
    return f"{v / TOTAL_AREA * 100:.1f}%"

# ── Traces Plotly ─────────────────────────────────────────────────────────────
inner_trace = go.Pie(
    hole=0.55,
    values=[d["value"] for d in inner],
    labels=[d["label"] for d in inner],
    marker=dict(
        colors=[d["color"] for d in inner],
        line=dict(color="#0d0d0d", width=3),
    ),
    textinfo="none",
    hovertemplate="<b>%{label}</b><br>%{value:,.0f} ha<br>%{percent}<extra></extra>",
    domain=dict(x=[0.15, 0.85], y=[0.02, 0.98]),
    sort=False,
    direction="clockwise",
    name="",
)

outer_trace = go.Pie(
    hole=0.72,
    values=[d["value"] for d in outer],
    labels=[d["label"] for d in outer],
    marker=dict(
        colors=[d["color"] for d in outer],
        line=dict(color="#0d0d0d", width=2),
    ),
    textinfo="none",
    hovertemplate="<b>%{label}</b><br>%{value:,.0f} ha<br>%{percent}<extra></extra>",
    domain=dict(x=[0.05, 0.95], y=[0, 1]),
    sort=False,
    direction="clockwise",
    name="",
)

# ── Layout ────────────────────────────────────────────────────────────────────
layout = go.Layout(
    paper_bgcolor="#0d0d0d",
    plot_bgcolor="#0d0d0d",
    showlegend=True,
    legend=dict(
        font=dict(color="#aaaaaa", size=13, family="Arial"),
        bgcolor="rgba(0,0,0,0)",
        x=1.01, y=0.5,
        xanchor="left",
        yanchor="middle",
    ),
    annotations=[
        # Centro do donut — área total
        dict(
            text=f"<b>{TOTAL_AREA/1000:.0f}k ha</b><br><span style='color:#666;font-size:11px'>ÁREA TOTAL</span>",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=22, color="#ffffff", family="Arial"),
            xanchor="center",
            yanchor="middle",
            align="center",
        ),
        # Título principal
        dict(
            text="<b>Uso e Cobertura do Solo — Sinop, MT</b>",
            x=0.5, y=1.08,
            showarrow=False,
            font=dict(size=22, color="#ffffff", family="Arial"),
            xanchor="center",
            yanchor="bottom",
            xref="paper",
            yref="paper",
        ),
        # Subtítulo
        dict(
            text="Distribuição da área municipal por classe de uso do solo · Ano base 2024<br>"
                 "<span style='color:#555'>MapBiomas Collection 10.1 · Resolução 30m · IBGE 2022</span>",
            x=0.5, y=1.035,
            showarrow=False,
            font=dict(size=13, color="#888888", family="Arial"),
            xanchor="center",
            yanchor="bottom",
            xref="paper",
            yref="paper",
        ),
        # Fonte
        dict(
            text="Fonte: MapBiomas Collection 10.1 · Limites: IBGE Malha Municipal 2022 · Projeto: sinop-agro-gis  |  @Jk-Pascoal",
            x=0.5, y=-0.05,
            showarrow=False,
            font=dict(size=11, color="#444444", family="Arial"),
            xanchor="center",
            yanchor="top",
            xref="paper",
            yref="paper",
        ),
    ],
    margin=dict(t=120, b=80, l=20, r=220),
    height=800,
    width=1200,
)

# ── Cards de stats (anotações inferiores) ─────────────────────────────────────
card_x_positions = [0.08, 0.27, 0.46, 0.65, 0.84]
for i, d in enumerate(inner):
    layout.annotations += (
        dict(
            text=(
                f"<span style='color:{d['color']}'>●</span> "
                f"<b style='color:#888;font-size:10px'>{d['label'].upper()}</b><br>"
                f"<b style='color:#fff;font-size:17px'>{fmt_ha(d['value'])}</b><br>"
                f"<span style='color:#555;font-size:11px'>{fmt_pct(d['value'])}</span>"
            ),
            x=card_x_positions[i],
            y=-0.18,
            showarrow=False,
            font=dict(size=12, color="#aaaaaa", family="Arial"),
            xanchor="center",
            yanchor="top",
            xref="paper",
            yref="paper",
            align="center",
            bgcolor="#141414",
            bordercolor="#222222",
            borderwidth=1,
            borderpad=10,
        ),
    )

# ── Gerar figura e exportar ───────────────────────────────────────────────────
fig = go.Figure(data=[inner_trace, outer_trace], layout=layout)

print(f"📊 Gerando PNG de alta resolução...")
print(f"   Saída: {OUTPUT_PNG}")

fig.write_image(
    str(OUTPUT_PNG),
    format="png",
    width=1200,
    height=800,
    scale=2,          # → 2400 × 1600 px final
    engine="kaleido",
)

size_kb = OUTPUT_PNG.stat().st_size / 1024
print(f"\n✅ Exportado com sucesso!")
print(f"   📁 {OUTPUT_PNG}")
print(f"   📐 Resolução: 2400 × 1600 px")
print(f"   📦 Tamanho: {size_kb:.0f} KB")
print(f"\n💡 Pronto para usar no LinkedIn!")
