import plotly.graph_objs as go
import pandas as pd
import dash
import dash_core_components as dcc 
import dash_html_components as html 

df = pd.read_csv('./ARIMA_result_for_senior_project.csv')
data = [
    go.Scattergl(
        x=df['DATE'],
        y=df['FARE']
    )
]
app = dash.Dash(__name__)

test_graph = dcc.Graph(id='test', figure={'data' : data})

app.layout = html.Div([
    test_graph
])

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)