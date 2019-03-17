# This is to keep code for future reference. 
# We only focus on the important parts of each element and I might add some css to show how to change some things in the page. 
import dash
import pandas as pd 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# There are also other attributes in the Dash object from the dash library such as the _dev_tools dictionary
# to see more you can place breakpoint after this point and go into the app variable 
app._dev_tools['hot_reload'] = True # It might not do anythign but I'm trying it anyways. 

# Maybe is better to have a list of the html components and then pass it to layout 
# This way you can divide things into two or three divs at the top level and then add things to the children list of each div as necessary
dashboard_layout = {
    'top' : html.Div(children=[], id='top'),
    'main_graphs' : html.Div(children=[], id='main-graphs'),
    'middle' : html.Div(children=[], id='middle-graphs'),
    'end' : html.Div(children=[], id='end-of-dashboard'),
}

# Now we can add to the children list at the top of the dashboard
user_input = [
    dcc.Input(id='myInput', value='Initial value', type='text'),
    html.Div(id='my-div') 
]
dashboard_layout['top'].children = user_input

# Let's explore the scatter plot from plotly 
# The interesting parts are in the callback create_first_test_graph()

test_graph = html.Div([
        html.Div([
           html.H2('hoverinfo'),
           html.P('can be "x", "y", "z", "text", "name" or any combination joined with "+" or "all" ', style={'display' : 'inline'}),
           dcc.Input(id='hoverinfo', value='x+y', style={'display' : 'inline'}), 
        ]),

        html.H2('hoverlabel'),
        html.P('is a dictionary that can contain: bgcolor, bordercolor, namelength'),
        html.Div([
            html.P('bgcolor: Sets the background color ', style={'display' : 'inline'}),
            dcc.Input(id='hoverlabel_bgcolor', value='red', style={'display' : 'inline'}) 
        ]),
        html.Div([
            html.P('bordercolor: Sets the border color of the hover labels ', style={'display' : 'inline'}),
            dcc.Input(id='hoverlabel_bordercolor', value='red', style={'display' : 'inline'}) 
        ]),
        html.Div([
            html.P('namelength: Sets the length (in number of characters) of the trace name in the hover labels for this trace. -1 shows the whole name regardless of length. 0-3 shows the first 0-3 characters, and an integer >3 will show the whole name if it is less than that many characters, but if it is longer, will truncate to `namelength - 3` characters and add an ellipsis. ', style={'display' : 'inline'}),
            dcc.Input(id='hoverlabel_namelength', value='-1', style={'display' : 'inline'}) 
        ]),

        html.Div([
            html.H2('hoveron'),
            html.P('any combination of "points", "fills" joined with a "+" ', style={'display' : 'inline'}),
            dcc.Input(id='hoveron', value='fills', style={'display' : 'inline'}) 
        ]),

        html.Button(id='render_button', children='Submit'),
        dcc.Graph(id='test-hover-graph')
])
dashboard_layout['main_graphs'].children.append(test_graph)


# We need to put our html components in the layout attribute of the Dash object. 
app.layout = html.Div(
    children=list(dashboard_layout.values())
)

# First we start with a callback for user input to test everything is running correctly. 
@app.callback(Output(component_id='my-div', component_property='children'),
            [Input(component_id='myInput', component_property='value')])
def show_input_value(value):
    children = [html.H1(value)]
    return children

# In this first graph I'm going to explore the hover functionality. 
@app.callback(Output(component_id='test-hover-graph', component_property='figure'),
            [Input(component_id='render_button', component_property='n_clicks')],
            [State(component_id='hoverinfo', component_property='value'),
            State(component_id='hoverlabel_bgcolor', component_property='value'),
            State(component_id='hoverlabel_bordercolor', component_property='value'),
            State(component_id='hoverlabel_namelength', component_property='value'),
            State(component_id='hoveron', component_property='value')])
def create_first_test_graph(hoverinfo_click, hoverinfo, hoverlabel_bgcolor, hoverlabel_bordercolor, hoverlabel_namelength, hoveron):
    # In this graph we are going to explore the hover functionality
    # There are 4 main ones and 3 for specifying the source in plotly
    # hoverinfo, hoverlabel, hoveron, hovertemplate, hovertext, hovertextsrc, hoverinfosrc, hovertemplatesrc.
    _hover = {} # Dictionary to store the hover properties. 

    # hoverinfo is a string that can be "x", "y", "z", "text", "name" or any combination joined with "+" or "all"
    _hover['hoverinfo'] = hoverinfo

    # hoverlabel is a dictionary that can contain the keys bgcolor, bordercolor, font, namelength, bgcolorsrc, bordercolorsrc, namelengthsrc. 
    # font is a dictionary that can contain family, size, color, familysrc, sizesrc, colorsrc. 
    _hover['hoverlabel'] = {
        'bgcolor' : hoverlabel_bgcolor,
        'bordercolor' : hoverlabel_bordercolor,
        'namelength' : int(hoverlabel_namelength)
    }

    df = pd.read_csv('./ARIMA_result_for_senior_project.csv')
    graph = [go.Scatter(
        x=df['DATE'],
        y=df['FARE'],
        **_hover
    )]
    return {'data' : graph}


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)