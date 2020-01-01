import dash
import dash_daq as daq
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
body = dbc.Container([
    dbc.Row([
        html.H1("BMI Calculator", style={"font-weight": "bold",
                                         "padding-top": 50,
                                         "margin": "auto"}),

    ]),
    dbc.Row([
        html.Div("Calculating patient's Body Mass Index based on their weight and height",
                 style={"margin": "auto", "padding-bottom": 60})
    ]),
    dbc.Row([
        dbc.Col(
            html.Div("Set patient's weight:"),
            width={"size": 6, "offset": 1}
        )
    ]),
    dbc.Row([
        dbc.Col(
            [
                dcc.Slider(
                    id="weight-slider",
                    min=40,
                    max=180,
                    step=0.5,
                    value=90,
                    marks={40: "40kg", 180: "180kg"}
                )

            ],
            md=6,
            style={"margin": "auto"}
        ),
        dbc.Col(
            [
                dcc.Input(
                    id="bmi_weight",
                    type="number",
                    placeholder="Enter weight in [kg]")
            ],
            md=4

        )
    ],
        style={"padding-bottom": 60}
    ),
    dbc.Row([
        dbc.Col(
            html.Div("Set patient's height:"),
            width={"size": 6, "offset": 1}
        )
    ]),
    dbc.Row([
        dbc.Col(
            [
                dcc.Slider(
                    id="height-slider",
                    min=100,
                    max=220,
                    step=1,
                    value=180,
                    marks={100: "100cm", 220: "220cm"}
                )

            ],
            md=6,
            style={"margin": "auto", "padding-bottom": 60}
        ),
        dbc.Col(
            [
                dcc.Input(
                    id="bmi_height",
                    type="number",
                    placeholder="Enter height in [cm]")
            ],
            md=4

        )
    ],
        style={"padding-bottom": 30}
    ),
    dbc.Row([
        dbc.Col(
            dbc.Button("Calculate BMI", color="primary", size="lg")
        )],
        style={"margin": "auto", "padding-bottom": 30},
        className="text-center"
    ),

    dbc.Row([
        dbc.Col([
            daq.Gauge(
                id='bmi-gauge',
                size=400,
                min=0,
                max=50,
                showCurrentValue=True,
                units="BMI",
                color={"gradient": False, "ranges": {"darkblue": [0, 16],
                                                     "lightblue": [16, 17],
                                                     "green": [17, 18.5],
                                                     "lightgreen": [18.5, 25],
                                                     "yellow": [25, 30],
                                                     "orange": [30, 35],
                                                     "red": [35, 40],
                                                     "purple": [40, 50]
                                                     }
                       },
                label="Your BMI",
                scale={'start': 0, 'interval': 1, 'labelInterval': 5},

                value=25
            )

        ])
    ])
],
    fluid=True
)

# dash constructor
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], assets_folder='assets', include_assets_files=True)
# dash layout
app.layout = html.Div([navbar, body])
# running server
if __name__ == '__main__':
    app.run_server()
