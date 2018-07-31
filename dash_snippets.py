# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

df2 = df.groupby('state')['total exports'].sum().reset_index(name='total_exports_sum')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns[1:]])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns[1:]
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()

markdown_text = 'hello there'
### Dash and Markdown

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H1(children='Live Sales Dashboard'),
    
    dcc.Markdown(children=markdown_text),
    
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df2['state'], 'y': df2['total_exports_sum'], 'type': 'bar', 'name': 'SF'}
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df),

])

if __name__ == '__main__':
    app.run_server(debug=True)
