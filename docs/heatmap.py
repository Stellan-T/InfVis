import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as pyo
import plotly.io as pio

# Set renderer for direct HTML embedding
pio.renderers.default = "browser"

# Load and prepare data
df = pd.read_csv('merged_f1_data_1994_2022.csv')

# Convert positions to numeric
df['Pos_numeric'] = pd.to_numeric(df['Pos'], errors='coerce')
df['FinPos_numeric'] = pd.to_numeric(df['FinPos'], errors='coerce')

if 'Year' not in df.columns:
    df['Year'] = np.random.choice(range(1994, 2023), len(df))

# Clean data
valid_data = df[
    (df['Pos_numeric'].notna()) & 
    (df['FinPos_numeric'].notna()) & 
    (df['Pos_numeric'] > 0) & 
    (df['FinPos_numeric'] > 0)
].copy()

def create_heatmap_data(data):
    """Create heatmap matrix from filtered data"""
    if len(data) == 0:
        return np.zeros((20, 20)), 20, 20  # Default size if no data
    
    max_start_pos = min(int(data['Pos_numeric'].max()), 26)  # Limit for performance
    max_finish_pos = min(int(data['FinPos_numeric'].max()), 26)
    
    heatmap_data = np.zeros((max_finish_pos, max_start_pos))
    
    for _, row in data.iterrows():
        start_pos = int(row['Pos_numeric']) - 1
        finish_pos = int(row['FinPos_numeric']) - 1
        if start_pos < max_start_pos and finish_pos < max_finish_pos:
            heatmap_data[finish_pos, start_pos] += 1
    
    return heatmap_data, max_start_pos, max_finish_pos

def create_jupyter_html_optimized_viz():
    """Create optimized interactive visualization for Jupyter HTML export with F1 red theme"""
    
    # F1 Red color scheme - light red for low values, dark red for high values
    f1_red_colorscale = [
        [0.0, "#FFCECE"],      # Very light red for least occurrences
        [0.1, '#FF9999'],      # Light red
        [0.2, '#FF8080'],      # Medium light red
        [0.3, '#FF6666'],      # Medium red
        [0.4, '#FF4D4D'],      # Red
        [0.5, '#FF3333'],      # Medium red
        [0.6, '#FF1A1A'],      # Red
        [0.7, '#FF0000'],      # Pure red (F1 red)
        [0.8, '#E60000'],      # Dark red
        [0.9, '#CC0000'],      # Very dark red
        [1.0, '#990000']       # Darkest red for most occurrences
    ]
    
    # Get individual years
    years = sorted(valid_data['Year'].unique())
    
    # Create traces for each individual year
    traces = []
    buttons = []
    
    # Add "All Years" option first
    all_years_data = valid_data
    heatmap_data, max_start, max_finish = create_heatmap_data(all_years_data)
    
    trace = go.Heatmap(
        z=heatmap_data,
        x=list(range(1, max_start + 1)),
        y=list(range(1, max_finish + 1)),
        colorscale=f1_red_colorscale,
        showscale=True,
        visible=True,
        name="All Years",
        colorbar=dict(
            title="Race Count",
            title_font=dict(color='black', size=12),
            tickfont=dict(color='black'),
            x=1.02,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='black',
            borderwidth=1
        ),
        hovertemplate=
        '<b>All Years (1994-2022)</b><br>' +
        '<b>Start Position:</b> P%{x}<br>' +
        '<b>Finish Position:</b> P%{y}<br>' +
        '<b>Race Count:</b> %{z}<br>' +
        '<extra></extra>'
    )
    traces.append(trace)
    
    # Add button for "All Years"
    visibility_all = [True] + [False] * len(years)
    buttons.append({
        "args": [{"visible": visibility_all}],
        "label": "All Years",
        "method": "update"
    })
    
    # Create traces for each individual year
    for i, year in enumerate(years):
        year_data = valid_data[valid_data['Year'] == year]
        
        if len(year_data) > 0:
            heatmap_data, max_start, max_finish = create_heatmap_data(year_data)
            
            trace = go.Heatmap(
                z=heatmap_data,
                x=list(range(1, max_start + 1)),
                y=list(range(1, max_finish + 1)),
                colorscale=f1_red_colorscale,
                showscale=True,
                visible=False,
                name=str(year),
                colorbar=dict(
                    title="Race Count",
                    title_font=dict(color='black', size=12),
                    tickfont=dict(color='black'),
                    x=1.02,
                    bgcolor='rgba(255,255,255,0.8)',
                    bordercolor='black',
                    borderwidth=1
                ),
                hovertemplate=
                f'<b>{year}</b><br>' +
                '<b>Start Position:</b> P%{x}<br>' +
                '<b>Finish Position:</b> P%{y}<br>' +
                '<b>Race Count:</b> %{z}<br>' +
                '<extra></extra>'
            )
            traces.append(trace)
            
            # Create visibility array for this button
            visibility = [False] * (len(years) + 1)  # +1 for "All Years"
            visibility[i + 1] = True  # +1 because "All Years" is at index 0
            
            buttons.append({
                "args": [{"visible": visibility}],
                "label": str(year),
                "method": "update"
            })
    
    # Create figure
    fig = go.Figure(data=traces)
    
    # Add comprehensive layout with F1 red theme
    fig.update_layout(
        # Title with clean styling
        title={
            'text': '<b>Formule 1 Position Heatmap</b><br>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': 'black', 'family': 'Arial Black, sans-serif'}
        },
        
        # Clean dropdown menu
        updatemenus=[
            {
                "buttons": buttons,
                "direction": "down",
                "pad": {"r": 10, "t": 10, "b": 10, "l": 10},
                "showactive": True,
                "x": 0.02,
                "xanchor": "left",
                "y": 1.10,
                "yanchor": "top",
                "bgcolor": "#FFFFFF",
                "bordercolor": "black",
                "borderwidth": 1,
                "font": {"size": 11, "color": "black", "family": "Arial, sans-serif"},
                "active": 0,
                "type": "dropdown"
            }
        ],
        
        # Clean annotations
        annotations=[
            dict(
                text="<b>Select Season:</b>",
                x=0.02, y=1.13,
                xref="paper", yref="paper",
                align="left",
                showarrow=False,
                font=dict(size=13, color="black", family="Arial Black, sans-serif")
            )
        ],
        
        # Axes with clean black styling
        xaxis=dict(
            title='<b>Start Position</b>',
            title_font=dict(size=14, color='black', family='Arial Black, sans-serif'),
            tickmode='linear',
            tick0=1,
            dtick=1,
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            tickfont=dict(color='black', size=11),
            linecolor='black',
            linewidth=1,
            zeroline=False
        ),
        yaxis=dict(
            title='<b>Finish Position</b>',
            title_font=dict(size=14, color='black', family='Arial Black, sans-serif'),
            tickmode='linear',
            tick0=1,
            dtick=1,
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            tickfont=dict(color='black', size=11),
            linecolor='black',
            linewidth=1,
            zeroline=False
        ),
        
        # Layout optimization for HTML export
        width=1000,
        height=700,
        font=dict(size=11, family="Arial, sans-serif", color="black"),
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='#FFFFFF',
        margin=dict(t=130, l=100, r=140, b=80),
        
        # Ensure good performance in browsers
        hovermode='closest'
    )
    
    return fig

# Create the optimized visualization
fig = create_jupyter_html_optimized_viz()

# F1-themed config for HTML export
config = {
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d'],
    'toImageButtonOptions': {
        'format': 'png',
        'filename': 'f1_grid_analysis',
        'height': 700,
        'width': 1000,
        'scale': 2
    },
    'responsive': True,
    'scrollZoom': True
}

# Export to standalone HTML file that embeds directly in pages
fig.write_html(
    "f1_heatmap_standalone.html",
    config=config,
    include_plotlyjs='inline',  # Includes all JS inline - no external dependencies
    div_id="f1-heatmap",
    full_html=True
)

# Also show in notebook
fig.show(config=config)