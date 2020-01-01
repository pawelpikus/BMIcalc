import dash
import dash_daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3")
            ]),
        dbc.NavItem(dbc.NavLink("Author", href="#"))
    ],
    brand="BMI Calc",
    brand_href="#",
    sticky="top"
)
body = dbc.Container(
    [
        dbc.Row([
            dbc.Col(
                [
                    dcc.Slider(
                        min=0,
                        max=10,
                        step=None,
                        marks={0: '0', 3: '3', 5: '5', 7: '7', 10: '10'},
                        value=5

                    )

                ],
                md=8,
            ),
            dbc.Col(
                [
                    dcc.Input(
                        id="bmi_weight",
                        type="number",
                        placeholder="number")
                ]
            )


        ])
    ]
)


# dash constructor
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
# dash layout
app.layout = html.Div([navbar, body, html.Div(style={'margin-top': 20})])
# running server
if __name__ == '__main__':
    app.run_server()

print()