import dash
from dash import html
import dash_bootstrap_components as dbc

##import frontend
from Frontend.Explorador.Explorador import Encabezado

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(Encabezado, md=12, style={'background-color':'red'}),
                dbc.Col('Mapa', md=12, style={'background-color':'blue'}),
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)