import pandas as pd
import plotly.graph_objects as go
import os

# 1. Rutes dinàmiques
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
input_path = os.path.join(base_dir, 'Resultats', 'dataset_preprocesat.csv')
output_path = os.path.join(base_dir, 'Resultats', 'grafic_interactiu.html')

# 2. Càrrega de dades
df = pd.read_csv(input_path)

# 3. Inicialitzar la figura de Plotly
fig = go.Figure()

# 4. TRAÇA 1: Temperatura Mitjana
fig.add_trace(
    go.Scatter(
        x=df['year'], 
        y=df['temp_media'],
        mode='lines+markers',
        name='Temperatura Mitjana (ºC)',
        line=dict(color='#1f77b4', width=2),
        marker=dict(size=6),
        customdata=df[['categoria_objectiva']],
        hovertemplate='<b>Any: %{x}</b><br>Temperatura: %{y} ºC<br>Categoria: %{customdata[0]}<extra></extra>',
        visible=True
    )
)

# 5. TRAÇA 2: Línia de tendència 
fig.add_trace(
    go.Scatter(
        x=df['year'], 
        y=df['tendencia_10_anys'],
        mode='lines',
        name='Tendència (10 anys)',
        line=dict(color='red', width=2, dash='dot'),
        hoverinfo='skip',
        visible=True
    )
)

# 6. TRAÇA 3: Anomalia Oficial
fig.add_trace(
    go.Scatter(
        x=df['year'], 
        y=df['anomalia_oficial'],
        mode='lines+markers',
        name='Anomalia Oficial (ºC)',
        line=dict(color='#ff7f0e', width=2),
        marker=dict(size=6),
        customdata=df[['categoria_objectiva']],
        hovertemplate='<b>Any: %{x}</b><br>Anomalia: %{y} ºC<br>Categoria: %{customdata[0]}<extra></extra>',
        visible=False
    )
)

# 7. TRAÇA 4: Línia base per a l'anomalia (0 ºC)
fig.add_trace(
    go.Scatter(
        x=[df['year'].min(), df['year'].max()],
        y=[0, 0],
        mode='lines',
        name='Mitjana Climàtica (1991-2020)',
        line=dict(color='gray', width=1, dash='dash'),
        hoverinfo='skip',
        visible=False
    )
)

# 8. Implementació de la Interacció de Reconfiguració (Selector de mètriques) 
fig.update_layout(
    updatemenus=[dict(
        type="buttons", direction="right", x=0.5, y=1.15,
        xanchor="center", yanchor="top",
        buttons=list([
            dict(
                label="Mostrar Temperatura Mitjana", method="update",
                args=[{"visible": [True, True, False, False]},
                      {"yaxis.title.text": "Temperatura (ºC)", "yaxis.autorange": True}]
            ),
            dict(
                label="Mostrar Anomalia Tèrmica", method="update",
                args=[{"visible": [False, False, True, True]}, 
                      {"yaxis.title.text": "Anomalia Tèrmica (ºC)", "yaxis.autorange": True}]
            )
        ])
    )]
)

# 9. Formateig visual i ràtio Dades-Tinta (Tufte)
fig.update_layout(
    title="Evolució de la Temperatura Estival a l'Espanya Peninsular (1961-2026)",
    xaxis_title="Any",
    yaxis_title="Temperatura (ºC)", 
    template="simple_white", 
    hovermode="x unified",
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
)

# 10. Guardar i exportar el resultat
fig.write_html(output_path)
print(f"Gràfic interactiu actualitzat generat a: {output_path}")