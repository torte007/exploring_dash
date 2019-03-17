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

# Graph has the following attributes: 
# id, clickData, clickAnnotationData, hoverData, clear_on_unhover (boolean), selectedData, relayoutData, 
# config: 'staticPlot', 'editable', 'edits', 'autosizable', 'queueLength', 'fillFrame', 
#       'frameMargins', 'scrollZoom', 'doubleClick', 'showTips', 'showAxisDragHandles', 
#       'showAxisRangeEntryBoxes', 'showLink', 'sendData', 'linkText', 'displayModeBar', 
#       'modeBarButtonsToRemove', 'modeBarButtonsToAdd', 'modeBarButtons', 'displaylogo', 
#       'plotGlPixelRatio', 'topojsonURL', 'mapboxAccessToken'.
#       The types of these keys are: staticPlot(boolean), editable(boolean), 
#           edits(dict): contains the keys: a set of editable properties. edits has the following type: dict containing keys 
#           'annotationPosition', 'annotationTail', 'annotationText', 'axisTitleText', 'colorbarPosition', 'colorbarTitleText', 
#           'legendPosition', 'legendText', 'shapePosition', 'titleText'.
#   
#           Most of the keys are booleans except for: frameMargins(number), doubleClick(a value equal to: false, 'reset', 'autosize', 'reset+autosize'; optional)
#           displayModeBar (a value equal to: true, false, 'hover'; optional), 
#           modeBarButtonsToAdd (list; optional): add mode bar button using config object,
#           plotGlPixelRatio (number; optional)
#           modeBarButtonsToRemove (list): the buttons are 
#               |  - (2D): zoom2d, pan2d, select2d, lasso2d, zoomIn2d, zoomOut2d, autoScale2d, resetScale2d
#               |  - (Cartesian): hoverClosestCartesian, hoverCompareCartesian
#               |  - (3D): zoom3d, pan3d, orbitRotation, tableRotation, handleDrag3d, resetCameraDefault3d, resetCameraLastSave3d, hoverClosest3d
#               |  - (Geo): zoomInGeo, zoomOutGeo, resetGeo, hoverClosestGeo
#               |  - hoverClosestGl2d, hoverClosestPie, toggleHover, resetViews
#           
app.layout = html.Div([
    test_graph
])

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)