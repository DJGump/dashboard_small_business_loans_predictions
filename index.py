import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import server, app
from layouts import home_layout, predictions_layout
import callbacks

import pandas as pd 
import io
from flask import send_file

app.index_string = ''' 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>SBA Loan Predictions</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        
    </body>
</html>
'''
# <div>SBA Loan Predictions</div>

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/sba_loan_predictions/':
         return home_layout
    elif pathname == '/loan_prediction_tool/':
         return predictions_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)