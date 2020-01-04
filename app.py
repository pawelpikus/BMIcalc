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
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Set patient's weight:", html_for="weight-slider"),
                    dcc.Slider(
                        id="weight-slider",
                        min=40,
                        max=180,
                        step=0.5,
                        value=68,
                        marks={40: "40kg", 180: "180kg"},
                        updatemode='drag'

                    ),
                    dbc.Label("Set patient's height:", html_for="height-slider", style={'padding-top': 10}),
                    dcc.Slider(
                        id="height-slider",
                        min=100,
                        max=220,
                        step=0.5,
                        value=178,
                        marks={100: "100cm", 220: "220cm"},
                        updatemode='drag'

                    )

                ],
            ),
            width=6

        ),
        dbc.Col([
            dbc.FormGroup([
                html.Div(
                    dbc.Input(
                        id="bmi_weight",
                        type="number",
                        min=40,
                        max=180,
                        step=0.5,
                        placeholder="Enter weight in [kg]"),
                    style={'margin': 35}),
                html.Div(
                    dbc.Input(
                        id="bmi_height",
                        size=5,
                        min=100,
                        max=220,
                        step=0.5,
                        type="number",
                        placeholder="Enter height in [cm]"),
                    style={'margin': 35})
            ])],

            width=4)
    ],
        justify='center'),
    dbc.Row([
        dbc.Col(
            dbc.Label("Patient's BMI is: ", id='bmi-label', style={'font-weight': 'bold', 'font-size': 30}))
    ],
        className="text-center"),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='bmi_dropdown',
                options=(
                    {'label': '19 - 24 years old', 'value': '19-24'},
                    {'label': '25 - 34 years old', 'value': '25-34'},
                    {'label': '35 - 44 years old', 'value': '35-44'},
                    {'label': '45 - 54 years old', 'value': '45-54'},
                    {'label': '55 - 64 years old', 'value': '55-64'},
                    {'label': 'over 64 years old', 'value': 'over64'}
                ),
                placeholder="Select patient's age",
                style={'margin-bottom': 20, 'margin-top': 20},

            ),
            width=5)

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            daq.Gauge(
                id='bmi-gauge',
                size=300,
                min=0,
                max=24,

                units="BMI",
                color={"ranges": {"darkblue": [0, 2.5],
                                  "green": [2.5, 8.5],
                                  "orange": [8.5, 14],
                                  "red": [14, 24],

                                  }
                       },

                scale={'custom': {0: 'underweight',
                                  2.5: 'optimal weight',
                                  8.5: 'overweight',
                                  14: 'obese I',
                                  19: 'obese II',
                                  24: 'obese III'},
                       },
                value=0
            )

        ])
    ],
        className="text-center")
], style={'box-shadow': '15px 17px 34px -1px rgba(189,183,189,1)',
          'max-width': '800px'})

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
    return "Patient's BMI is: {}".format(int(w_value / (h_value * h_value)))


@app.callback(
    Output('bmi-gauge', 'value'),
    [Input('bmi_weight', 'value'),
     Input('bmi_height', 'value'),
     Input('bmi_dropdown', 'value')])
def update_output(wval, hval, age):
    wval = wval * 10000
    bmi = (wval / (hval * hval))
    if age == '19-24':
        return bmi - 16.6
    elif age == '25-34':
        return bmi - 17.4
    elif age == '35-44':
        return bmi - 18.58
    elif age == '45-54':
        return bmi - 19.5
    elif age == '55-64':
        return bmi - 20.5
    elif age == 'over64':
        return bmi - 21.5


# running server
if __name__ == '__main__':
    app.run_server()
