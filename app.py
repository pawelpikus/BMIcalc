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
        html.Div("Calculating patient's Body Mass Index",
                 style={"margin": "auto", "padding-bottom": 60})
    ]),
    dbc.Row([

        dbc.Col([
            dcc.RadioItems(
                options=[
                    {'label': 'Male', 'value': 'M'},
                    {'label': 'Female', 'value': 'F'}
                ],
                value='M'

            )
        ],
            style={'margin': 'auto', 'padding-bottom': 30},
            md=4,
        ),

        dbc.Col([
            dcc.Dropdown(
                options=(
                    {'label': '19 - 24 years old', 'value': '19-24'},
                    {'label': '25 - 34 years old', 'value': '25-34'},
                    {'label': '35 - 44 years old', 'value': '35-44'},
                    {'label': '45 - 54 years old', 'value': '45-54'},
                    {'label': '55 - 64 years old', 'value': '55-64'},
                    {'label': 'over 64 years old', 'value': 'over64'}
                ),
                placeholder="Select patient's age"
            )
        ],
            style={'margin': 'auto', 'padding-bottom': 30},
            md=3,

        )

    ]),
    dbc.Row([
        dbc.Col(
            html.Div("Set patient's weight:"),
            width={"size": 6, "offset": 2}
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
                    marks={40: "40kg", 180: "180kg"},
                    updatemode='drag'
                )

            ],
            md=4,
            style={"margin": "auto"}
        ),
        dbc.Col(
            [
                dcc.Input(
                    id="bmi_weight",
                    type="number",
                    min=40,
                    max=180,
                    step=0.5,
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
            width={"size": 6, "offset": 2}
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
                    marks={100: "100cm", 220: "220cm"},
                    updatemode='drag'
                )

            ],
            md=4,
            style={"margin": "auto", "padding-bottom": 60}
        ),
        dbc.Col(
            [
                dcc.Input(
                    id="bmi_height",
                    size=5,
                    min=100,
                    max=220,
                    step=0.5,
                    type="number",
                    placeholder="Enter height in [cm]")
            ],
            md=4

        )
    ],
        style={"padding-bottom": 30}
    ),
    # dbc.Row([
    #     dbc.Col(
    #         dbc.Button("Calculate BMI", color="primary", size="lg")
    #     )],
    #     style={"margin": "auto", "padding-bottom": 30},
    #     className="text-center"
    #   ),
    dbc.Row([
        dbc.Col(
            dbc.Label("Patient's BMI is: ", id='bmi-label', style={'font-weight': 'bold', 'font-size': 30}))
    ],
        className="text-center"),

    dbc.Row([
        dbc.Col([
            daq.Gauge(
                id='bmi-gauge',
                size=400,
                min=0,
                max=24,

                units="BMI",
                color={"ranges": {"darkblue": [0, 6],
                                  "green": [6, 12],
                                  "orange": [12, 17],
                                  "red": [17, 24],

                                  }
                       },

                scale={'custom': {0: 'underweight',
                                  6: 'optimal weight',
                                  12: 'overweight',
                                  17: 'obese',
                                  24: 'ridiculously fat'},
                       },
                value=0
            )

        ])
    ],
        className="text-center")

],

)

# dash constructor
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], assets_folder='assets', include_assets_files=True)
# dash layout
app.layout = html.Div([navbar, body])


@app.callback(
    Output('bmi_weight', 'value'),
    [Input('weight-slider', 'value')])
def update_weight(weight_value):
    return weight_value


@app.callback(
    Output('bmi_height', 'value'),
    [Input('height-slider', 'value')])
def update_height(height_value):
    return height_value


@app.callback(
    Output('bmi-label', 'children'),
    [Input('bmi_weight', 'value'), Input('bmi_height', 'value')])
def update_label(w_value, h_value):
    w_value = w_value * 10000
    return "Your BMI is: {:.2f}".format(w_value / (h_value * h_value))


@app.callback(
    Output('bmi-gauge', 'value'),
    [Input('bmi_weight', 'value'),
     Input('bmi_height', 'value')]
)
def update_output(wval, hval):
    wval = wval * 10000
    return (wval / (hval * hval)) - 16


# running server
if __name__ == '__main__':
    app.run_server()
