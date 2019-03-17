import dash
import pandas as pd 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='test-graph'),
    dcc.Input(id='my-input', value='initial value')
])

@app.callback(Output(component_id='test-graph', component_property='figure'),
            [Input(component_id='my-input', component_property='value')])
def create_first_test_graph(myInput):
    df = pd.read_csv('./ARIMA_result_for_senior_project.csv')
    data = [go.Scattergl(
        x=df['DATE'],
        y=df['FARE']
    )]
# Some parameters of the layout objs that could be important in this feature are:
#
# dragmode ("zoom" | "pan" | "select" | "lasso" | "orbit" | "turntable" | False)
# hoverdistance (-1 means no cutoff)
#
# hoverlabel is an instance of Hoverlabel or a dict with the properties: bgcolor, bordercolor, font, and namelength
#
# hovermode is an enumeration that may be specified as One of the following enumeration values: ['x', 'y', 'closest', False]
#       If 'clickmode' includes the "select" flag, 'hovermode' defaults to "closest". 
#       If 'clickmode' lacks the "select" flag, it defautls to "x" or "y" (depending on the trace's 'orientation' value) for plots based on cartesian coordinates. 
#       For anything else the default value is "closest".
#
# clickmode (Determines the mode of single click interactions.) 
#       It can be event, which is the default value and emits the 'plotly_click' event and the 'plotly_selected' event in drag modes "lasso" and "select".
#       Or it can be "select" which enables selecting single data points via clicks. 
#       The clickmode property is a string and can contain any combination of ['event', 'select'] joined with '+' character. 
#
# shapes a list of instances of go.layout.Shape look into go.layout.Shape
#       Shapes have the following attributes:
#       fillcolor: sets the color filling the shape's interior. 
#       layer: specifies whether shapes are drwn below or above traces. 
#       opacity: sets the opacity of the shape. 
#       path: a valid svg path 
#       type: specifies the shape to be drawn. it can be "line", "circle", "rect", "path".
#           In "line", a line is drawn from ('x0', 'y0') to ('x1', 'y1') with respect to the axes' sizing mode. 
#           In "circle", a circle is drawn from (   (`x0`+`x1`)/2 ,  (`y0`+`y1`)/2)   ) with radius (  | (`x0`+`x1`)/2  -  `x0` | , | (`y0`+`y1`)/2  - `y0`) |  ) with respect to the axes' sizing mode.
#           In "rect", a rectangle is drawn linking (`x0`,`y0`), (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect to the axes' sizing mode
#       visible: determines whether or not this shape is visible. 
#       x0: sets the shape's starting x position, see 'type' and 'xsizemode'
#       x1: sets the shape's end x position. 
#       xanchor: specifies the anchor point on the x axis to which 'x0', 'x1', and x coordinates within 'path' are relative to. 
#                only relevant in conjunction with 'xsizemode' set to "pixel". No effect when 'xsizemode' not set to "pixel".
#       xref: sets the shape's x coordinate axis. 
#           If set to an x axis id ("x" or "x2"... etc), the x position refers to an x coordinate. 
#           If set to "paper", the x position refers to the distance from the left side of the plotting area in normalized coordinates where 0(1) corresponds to the left(right) side. 
#       xsizemode: sets the shape's sizing mode along the x axis.
#           If set to "scaled", 'x0', 'x1' and x coordinates within 'path' refer to data values on the x axis or a fraction of the plot area's width.
#           If set to "pixel", 'xanchor' specifies the x position in terms of data or plot fraction but 'x0', 'x1' and x coordinates within 'ath' are pixels relative to 'xanchor'. 
#           This way, the shape can have a fixed width while maintaining a position relative to data or plot fraction. 
#       We also have y0, y1, yanchor, yref, and ysizemode. They work the same way as in their x counterparts. 
#
# selectdirection (when "dragmode" is set to "select", this limits the selection of the drag to horizontal, vertical or diagonal)
#       Is an enumeration that may be specified as: ['h', 'v', 'd', 'any'] the default is any. 
#
# spikedistance (-1 means no cutoff) Sets the default distance (in pixels) to look for data to draw spikelines to. some objects can be hovered on but will generate spikelines, such as scatter fills? 
#
# updatemenus
#
# xaxis look into go.layout.XAxis
#   type: ( enumerated : "-" | "linear" | "log" | "date" | "category" | "multicategory" ) 
#   anchor: "free" | "/^x([2-9]|[1-9][0-9]+)?$/" | "/^y([2-9]|[1-9][0-9]+)?$/"
#   automargin: Determines whether long tick labels automatically grow the figure margins.
#   autorange: determines whether or not the range of this axis is computed in relation to the input data. See 'rangemode' for more info. If 'range' is provided, then 'autorange' is set to False.
#   dtick: (step in-between ticks on this axis) If the axis `type` is "date", then you must convert the time to milliseconds. 
#       For example, to set the interval between ticks to one day, set `dtick` to 86400000.0. 
#       "date" also has special values "M<n>" gives ticks spaced by a number of months. `n` must be a positive integer. 
#       To set ticks on the 15th of every third month, set `tick0` to "2000-01-15" and `dtick` to "M3". To set ticks every 4 years, set `dtick` to "M48"
#   fixedrange: determines whether or not this axis is zoom-able. If true, then zoom is disabled. 
#   showgrid (boolean)
#   gridcolor: sets the color of the grid lines. 
#   gridwidth: sets the width (in px) of the grid lines. 
#   nticks: specifies the max number of ticks for the axis. has an effect only if tickmode is set to auto. 
#   position: Sets the position of this axis in the plotting space (in normalized coordinates). Only has an effect if `anchor` is set to "free".
#   hoverformat: sets the hover text formatting rule using d3 formatting mini-languages (not interesting) https://github.com/d3/d3-time-format/blob/master/README.md#locale_format
#   layer: sets the layer on which this axis is displayed. "above traces" | "below traces".  
#       If "above traces", this axis is displayed above all the subplot's traces 
#       If "below traces", this axis is displayed below all the subplot's traces, but above the grid lines. Useful when used together with scatter-like traces with `cliponaxis` set to "False" to show markers and/or text nodes above this axis.
#   showline (boolean), linecolor, linewidth, visible, color, title (is a dictionary), type ("-" | "linear" | "log" | "date" | "category" | "multicategory"), mirror (True | "ticks" | False | "all" | "allticks"), side, 
#   range: sets the range of this axis. If the axis `type` is "category", it should be numbers, using the scale where each category is assigned a serial number from zero in the order it appears.
#   scaleanchor: not important right now. 
#!! showspikes: determines whether or not spikes (aka droplines) are drawn for this axis. (it only takes affect when hovermode = closest WHY????? )
#   showticklabels: determines whether or not the tick labels are drawn. 
#   spikemode: (Any combination of "toaxis", "across", "marker" joined with a "+" )
#   spikesnap: Determines whether spikelines are stuck to the cursor or to the closest datapoints. ("data" or "cursor")
#   tickangle: sets the angle for the tick labels with respoect to the horizontal. 
#   title: is important to have a title!
#   
# yaxis look into go.layout.YAxis


# Also it might be interesting to play with: 
# colorway, height, paper_bgcolor (hex string), plot_bgcolor (hex string), scene is an instance off Scene (I'm guessing the it is go.layout.Scene), sliders (look into go.layout.Slider)
# Also look deeper into go.layout.xaxis.Rangeslider and go.layout.xaxis.Rangeslider. 
# 
    layout = go.Layout()
    return {'data' : data}


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)