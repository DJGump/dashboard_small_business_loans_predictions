import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
from components import header
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd
import sys


def table_type(df_column):
    # Function for getting dtypes for dash data table, with pandas
    # Note - this only works with Pandas >= 1.0.0

    if sys.version_info < (3, 0):  # Pandas 1.0.0 does not support Python 2
        return 'any'

    if isinstance(df_column.dtype, pd.DatetimeTZDtype):
        return 'datetime',
    elif (isinstance(df_column.dtype, pd.StringDtype) or
            isinstance(df_column.dtype, pd.BooleanDtype) or
            isinstance(df_column.dtype, pd.CategoricalDtype) or
            isinstance(df_column.dtype, pd.PeriodDtype)):
        return 'text'
    elif (isinstance(df_column.dtype, pd.SparseDtype) or
            isinstance(df_column.dtype, pd.IntervalDtype) or
            isinstance(df_column.dtype, pd.Int8Dtype) or
            isinstance(df_column.dtype, pd.Int16Dtype) or
            isinstance(df_column.dtype, pd.Int32Dtype) or
            isinstance(df_column.dtype, pd.Int64Dtype)):
        return 'numeric'
    else:
        return 'any'

# read in cleaned loan data
df = pd.read_csv('data/sba_loans_cleaned3.csv')

rename_dict = {
    "State": "State",
    "BankState": "Bank State",
    "ApprovalFY": "Approval Fiscal Year",
    "NoEmp": "Number of Employees",
    "NewExist": "New or Existing Business Status",
    "RevLineCr": "Revolving Line of Credit Status",
    "LowDoc": "Low Documentation Approved Status",
    "DisbursementGross": "Disbursement (Gross)",
    "MIS_Status": "MIS_Status (Outcome)",
    "twoDigNAICS": "Two Digit NAICS Industry Code",
    "is_franchise": "Franchise Status",
    "bank_out_of_state": "Bank Out of State Status",
    "Term_years": "Loan Term (Years)",
    "job_category": "Jobs Created Rank",
    "retained_category": "Jobs Retained Rank",
    "UrbanRural_cleaned": "Urban or Rural Status",
    "Disbr_year": "Year of Disbursement",
    "Disbr_Month_sin": "Disbr_Month_sin",
    "Disbr_Month_cos": "Disbr_Month_cos",
    "sba_pre_approv": "SBA Pre-Approval",
    "percent_SBA": "Loan Percentage SBA Committed",
    "bank_size": "Bank Size Rank",
    "Appv_Month_sin": "Appv_Month_sin",
    "Appv_Month_cos": "Appv_Month_cos",
}

df.rename(columns=rename_dict, inplace=True)
df = df.round(decimals=2)

# Build Components
inputs = [

]

home_layout = dbc.Container(
    fluid=True,
    children=[
        html.H1('SBA Loan Data: 2000-2014'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dash_table.DataTable(
                    id='datatable-home',
                    columns=[{'name': i, "id": i, 'type': table_type(df[i]) } for i in df.columns],
                    data=df.sample(10000).to_dict('records'),
                    sort_action='native',
                    fixed_rows={'headers': True, 'data': 0},
                    editable=False,
                    page_action='native',
                    filter_action='native',
                )
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='app-2-display-value'),
                dcc.Link('Go to Prediction Tool', href='/loan_prediction_tool/')
            ])
        ])
    ]
)
# input loan information, predict outcome, get k nearest loans from dataset
predictions_layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row([
           dbc.Col([dbc.Card(inputs, body='True')

           ])
        ]),
        dbc.Row([
            dbc.Col([
                html.Div(id='app-2-display-value'),
                dcc.Link('Go to Prediction Tool', href='/loan_prediction_tool/')
            ])
        ])
    ]
)


    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/sba_loan_predictions/')
])