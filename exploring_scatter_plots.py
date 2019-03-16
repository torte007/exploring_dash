# This is to keep code for future reference. 
# Not from the tutorial but from the reference page. 
# We only focus on the important parts of each element and I might add some css to show how to change some things in the page. 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # This is just the css code from codepen
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) # Other parameters that can be passed to a Dash object are listed below:
# dash.Dash(Dash(name='__main__', 
# server=None, 
# static_folder='static', 
# assets_folder='assets', 
# assets_url_path='/assets', 
# assets_ignore='', 
# include_assets_files=True, 
# url_base_pathname=None, 
# assets_external_path=None, 
# requests_pathname_prefix=None, 
# routes_pathname_prefix=None, 
# compress=True, 
# meta_tags=None, 
# index_string=_default_index, 
# external_scripts=None, 
# external_stylesheets=None, 
# suppress_callback_exceptions=None, 
# components_cache_max_age=None, **kwargs: object))

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

if __name__ == '__main__':
    app.run_server(debug=True)