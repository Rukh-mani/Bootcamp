import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

"""
this is where the backend goes
"""
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")


# Define the layout
app.layout = html.Div([
    html.H1("Simple Dash App"),
    dcc.Graph(figure = fig),
    html.Button("Press Me", id='my-button'),
    dbc.Button("Press me but pretty", color="primary", className="me-1"),
])

# Run the app in Jupyter Notebook
if __name__ == '__main__':
    app.run_server(debug='true')