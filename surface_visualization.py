import numpy as np
import plotly.graph_objects as go

from black_scholes import blackScholes
from greeks import delta_value, gamma_value


ticker = "AAPL"

S0 = 34.03
K = 40.0
r = 0.0412
sigma = 0.35
days = 30

T0 = days / 365


s_range = np.linspace(28, 48, 160)
dte_range = np.linspace(1, 75, 160)

s_grid, dte_grid = np.meshgrid(s_range, dte_range)

z = np.zeros_like(s_grid)

for i in range(s_grid.shape[0]):
    for j in range(s_grid.shape[1]):

        current_s = s_grid[i, j]
        current_t = dte_grid[i, j] / 365

        result = blackScholes(
            r,
            current_s,
            K,
            current_t,
            sigma,
            "c"
        )

        z[i, j] = result["my_price"]


base_price = blackScholes(
    r,
    S0,
    K,
    T0,
    sigma,
    "c"
)["my_price"]

base_delta = delta_value(
    r,
    S0,
    K,
    T0,
    sigma,
    "c"
)[0]

base_gamma = gamma_value(
    r,
    S0,
    K,
    T0,
    sigma,
    "c"
)[0]


fig = go.Figure()

fig.add_trace(
    go.Surface(
        x=s_grid,
        y=dte_grid,
        z=z,
        colorscale="Hot",
        opacity=0.96,
        hovertemplate=
        "Stock Price: $%{x:.2f}<br>" +
        "Days to Expiry: %{y:.0f}<br>" +
        "Call Price: $%{z:.4f}<extra></extra>"
    )
)

fig.add_trace(
    go.Scatter3d(
        x=[S0],
        y=[days],
        z=[base_price],
        mode="markers+text",
        text=["Current Option"],
        textposition="top center",
        marker=dict(
            size=7,
            color="cyan"
        ),
        hovertemplate=
        f"S = ${S0:.2f}<br>" +
        f"K = ${K:.2f}<br>" +
        f"DTE = {days}<br>" +
        f"Price = ${base_price:.4f}<br>" +
        f"Delta = {base_delta:.4f}<br>" +
        f"Gamma = {base_gamma:.4f}<extra></extra>"
    )
)

fig.update_layout(
    title="Black-Scholes Option Pricing Surface",
    template="plotly_dark",
    scene=dict(
        xaxis_title="Stock Price",
        yaxis_title="Days to Expiration",
        zaxis_title="Call Price",
        camera=dict(
            eye=dict(x=1.6, y=1.7, z=1.1)
        )
    ),
    annotations=[
        dict(
            text=(
                f"<b>Model Inputs</b><br>"
                f"S = ${S0:.2f}<br>"
                f"K = ${K:.2f}<br>"
                f"DTE = {days}<br>"
                f"σ = {sigma:.2%}<br>"
                f"r = {r:.2%}<br>"
                f"Call = ${base_price:.4f}<br>"
                f"Delta = {base_delta:.4f}<br>"
                f"Gamma = {base_gamma:.4f}"
            ),
            x=0.02,
            y=0.98,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            bgcolor="rgba(0,0,0,0.70)",
            bordercolor="white",
            borderwidth=1
        )
    ],
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=45
    )
)

fig.write_html(
    "scholes_surface.html",
    auto_open=True
)

print("Opened new tab with visualization")