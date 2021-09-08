import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
#Data Pre processing
df = pd.read_csv('supermarket_sales - Sheet1.csv')
available_indicators = df['Gender'].unique()
available_indicators2 = df['City'].unique()
#Making figure
graphline = px.line(df, x='Tax 5%', y='Total')


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Customer Behavior to Drive Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='What quantities at which gender-specific customers generate more gross income and'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_gender',
                    options=[
                       {'label': gender, 'value': gender} for gender in available_indicators
                    ],
                    value='Female',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='box-graph'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='bar-graph'
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=graphline
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': city, 'value': city} for city in available_indicators2
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='pie-graph'
                )
            )
        ]),
        html.H2(children='Overall analysis'),
        html.P('The graph shows that male customers tend to give higher satisfaction ratings for shopping experience when they pay using e-wallets or credit cards. Female customers, contrarily, tend to give higher satisfaction ratings for shopping experience when paying in cash.'),
        html.P('Food and beverage gross income is the biggest'),
        html.P('The product line that are frequently bought in Yangon city are home and lifestyle product, in Naypyitaw are food and beverages product, and in Mandalay city are sport and lifestyle product'),
        html.Br(),
        html.H2(children = 'Hypothesis Testing'),
        html.H4(children=
        'Hubungan antara "City" dengan "Product line"'
        ),
        html.P(children='Setelah dilakukan uji chi square, didapatkan nilai chi square sebesar 48164.4208, sehingga dapat disimpulkan adanya hubungan antara kota dengan produk yang dibeli')  
    ])
])
 
@app.callback(
    Output('box-graph', 'figure'),
    Output('bar-graph', 'figure'),
    Output('pie-graph', 'figure'),
    Input('selected_gender','value'),
    Input('selected_city', 'value')
)
def update_chart(gender,city):
    dfgender = df[df['Gender'] == gender]
    dfcity = df[df['City'] == city]
    fig = px.box(dfgender, x='Payment', y="Rating",color='Payment')
    fig2 = px.bar(dfgender, x='Product line', y="gross income", color='Product line')
    fig3 = px.bar(dfcity, x='Product line', y='Quantity',color='Product line')
    return fig,fig2,fig3