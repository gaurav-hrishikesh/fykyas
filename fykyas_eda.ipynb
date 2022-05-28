{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e0896cd2-b938-4f85-9914-d1cca74dcd2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import plotly.express as px  # (version 4.7.0 or higher)\n",
    "import plotly.graph_objects as go\n",
    "#from dash import Dash\n",
    "from jupyter_dash import JupyterDash\n",
    "#from dash import dcc\n",
    "import dash_core_components as dcc \n",
    "#from dash import html\n",
    "import dash_html_components as html\n",
    "from dash.dependencies import Input, Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "24dbe5c4-f01b-4ecf-9342-97ce8c7aa48b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame()\n",
    "df['time']=np.arange(0,2000,5)\n",
    "df['System ON in Auto Mode']= np.random.randint(0,2,400)\n",
    "df['Operating Mode']= np.random.randint(0,2,400)\n",
    "df['Billet Size']= np.random.randint(120,121,400)\n",
    "df['Soaking Zone Temp']= np.random.normal(1185,2,400)\n",
    "df['Heating Zone Temp']= np.random.normal(985,2,400)\n",
    "df['Furnace pressure']= np.random.normal(0.8,1.5,400)\n",
    "df['Oxygen %']= np.random.normal(0.02,1.5,400)\n",
    "df['Soaking Zone Set Point']= np.random.randint(1185,1186,400)\n",
    "df['Heating Zone Set Point']= np.random.randint(985,986,400)\n",
    "df['Furnace pressure Set Point']= np.random.random(400)\n",
    "df['Oxygen % Set Point']= np.random.randint(2,3,400)\n",
    "df['Soaking Zone Coal Motor RPM']= np.random.randint(1175,1491,400)\n",
    "df['Air Motor RPM']= np.random.randint(1200,1476,400)\n",
    "df['Pressure PID  Output %']= np.random.randint(95,96,400)\n",
    "df['Furnace Damper Opening']= np.random.randint(95,96,400)\n",
    "df['Flue Gas temp before Rec']= np.random.randint(712,752,400)\n",
    "df['Flue Gas temp aftre Rec']= np.random.randint(255,290,400)\n",
    "df['Combustion Air temp before Rec']= np.random.randint(45,52,400)\n",
    "df['Combustion Air temp After Rec']= np.random.randint(325,350,400)\n",
    "df['Combustion Air Pressure Before Rec']= np.random.randint(1475,1486,400)\n",
    "df['Combustion Air Pressure After Rec']= np.random.randint(1478,1501,400)\n",
    "df['Coal Motor1 RPM set point Min']= np.random.randint(1175,1176,400)\n",
    "df['Coal Motor1 RPM set point Max']= np.random.randint(1430,1431,400)\n",
    "df['Air Motor RPM set point Min']= np.random.randint(1200,1201,400)\n",
    "df['Air Motor RPM set point Max']= np.random.randint(1475,1476,400)\n",
    "df['Furnace Damper Opening Set Min']= np.random.randint(50,51,400)\n",
    "df['Furnace Damper Opening Set Max']= np.random.randint(95,96,400)\n",
    "df['Air Motor Current ']= np.random.randint(35,43,400)\n",
    "df['Coal Consumption (Cumulative-Sum)']= np.linspace(55,55+399,num=400)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "377916e8-5c46-473f-afba-5bec41128681",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('fykyas_drive.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0200005d-dd61-40fe-b76f-430d2312f45c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(400, 10)\n",
      "Index(['Soaking Zone Temp', 'Heating Zone Temp', 'Furnace pressure',\n",
      "       'Soaking Zone Coal Motor RPM', 'Oxygen %', 'Air Motor RPM',\n",
      "       'Combustion Air temp before Rec', 'Combustion Air temp After Rec',\n",
      "       'Combustion Air Pressure Before Rec',\n",
      "       'Combustion Air Pressure After Rec'],\n",
      "      dtype='object')\n",
      "(10, 10)\n",
      "Soaking Zone Temp                     1.000000\n",
      "Heating Zone Temp                     0.008033\n",
      "Furnace pressure                     -0.006420\n",
      "Soaking Zone Coal Motor RPM           0.069216\n",
      "Oxygen %                              0.032491\n",
      "Air Motor RPM                        -0.039356\n",
      "Combustion Air temp before Rec       -0.050743\n",
      "Combustion Air temp After Rec         0.090362\n",
      "Combustion Air Pressure Before Rec   -0.012085\n",
      "Combustion Air Pressure After Rec     0.017808\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "X = df[['Soaking Zone Temp', 'Heating Zone Temp', 'Furnace pressure', 'Soaking Zone Coal Motor RPM','Oxygen %','Air Motor RPM','Combustion Air temp before Rec','Combustion Air temp After Rec','Combustion Air Pressure Before Rec','Combustion Air Pressure After Rec']]\n",
    "print(X.shape)\n",
    "print(X.columns)\n",
    "corr_df= X.corr()\n",
    "print(corr_df.shape)\n",
    "print((X.corrwith(X['Soaking Zone Temp'])))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "14fc4bb0-cd60-4320-a96b-e11cfe3064c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "c=pd.DataFrame(corr_df.columns.values.tolist(),columns=['column_name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6fce216c-807a-4404-b7de-ddf95ad9cced",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['column_name'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.columns.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ab3c0fbc-5594-405c-b79b-806302ec7473",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                    Soaking Zone Temp  Heating Zone Temp  \\\n",
      "Soaking Zone Temp                            1.000000           0.008033   \n",
      "Heating Zone Temp                            0.008033           1.000000   \n",
      "Furnace pressure                            -0.006420           0.078561   \n",
      "Soaking Zone Coal Motor RPM                  0.069216           0.068344   \n",
      "Oxygen %                                     0.032491           0.025204   \n",
      "Air Motor RPM                               -0.039356          -0.053445   \n",
      "Combustion Air temp before Rec              -0.050743          -0.002661   \n",
      "Combustion Air temp After Rec                0.090362          -0.105991   \n",
      "Combustion Air Pressure Before Rec          -0.012085          -0.017834   \n",
      "Combustion Air Pressure After Rec            0.017808          -0.024655   \n",
      "\n",
      "                                    Furnace pressure  \\\n",
      "Soaking Zone Temp                          -0.006420   \n",
      "Heating Zone Temp                           0.078561   \n",
      "Furnace pressure                            1.000000   \n",
      "Soaking Zone Coal Motor RPM                 0.041201   \n",
      "Oxygen %                                   -0.030447   \n",
      "Air Motor RPM                               0.015595   \n",
      "Combustion Air temp before Rec              0.034814   \n",
      "Combustion Air temp After Rec               0.027679   \n",
      "Combustion Air Pressure Before Rec          0.008013   \n",
      "Combustion Air Pressure After Rec          -0.150466   \n",
      "\n",
      "                                    Soaking Zone Coal Motor RPM  Oxygen %  \\\n",
      "Soaking Zone Temp                                      0.069216  0.032491   \n",
      "Heating Zone Temp                                      0.068344  0.025204   \n",
      "Furnace pressure                                       0.041201 -0.030447   \n",
      "Soaking Zone Coal Motor RPM                            1.000000  0.007322   \n",
      "Oxygen %                                               0.007322  1.000000   \n",
      "Air Motor RPM                                          0.024560 -0.015468   \n",
      "Combustion Air temp before Rec                        -0.003626  0.044567   \n",
      "Combustion Air temp After Rec                         -0.018484  0.039746   \n",
      "Combustion Air Pressure Before Rec                    -0.020569 -0.052886   \n",
      "Combustion Air Pressure After Rec                     -0.088733  0.053667   \n",
      "\n",
      "                                    Air Motor RPM  \\\n",
      "Soaking Zone Temp                       -0.039356   \n",
      "Heating Zone Temp                       -0.053445   \n",
      "Furnace pressure                         0.015595   \n",
      "Soaking Zone Coal Motor RPM              0.024560   \n",
      "Oxygen %                                -0.015468   \n",
      "Air Motor RPM                            1.000000   \n",
      "Combustion Air temp before Rec          -0.046237   \n",
      "Combustion Air temp After Rec            0.077045   \n",
      "Combustion Air Pressure Before Rec      -0.069961   \n",
      "Combustion Air Pressure After Rec       -0.020861   \n",
      "\n",
      "                                    Combustion Air temp before Rec  \\\n",
      "Soaking Zone Temp                                        -0.050743   \n",
      "Heating Zone Temp                                        -0.002661   \n",
      "Furnace pressure                                          0.034814   \n",
      "Soaking Zone Coal Motor RPM                              -0.003626   \n",
      "Oxygen %                                                  0.044567   \n",
      "Air Motor RPM                                            -0.046237   \n",
      "Combustion Air temp before Rec                            1.000000   \n",
      "Combustion Air temp After Rec                             0.022494   \n",
      "Combustion Air Pressure Before Rec                       -0.061538   \n",
      "Combustion Air Pressure After Rec                        -0.057737   \n",
      "\n",
      "                                    Combustion Air temp After Rec  \\\n",
      "Soaking Zone Temp                                        0.090362   \n",
      "Heating Zone Temp                                       -0.105991   \n",
      "Furnace pressure                                         0.027679   \n",
      "Soaking Zone Coal Motor RPM                             -0.018484   \n",
      "Oxygen %                                                 0.039746   \n",
      "Air Motor RPM                                            0.077045   \n",
      "Combustion Air temp before Rec                           0.022494   \n",
      "Combustion Air temp After Rec                            1.000000   \n",
      "Combustion Air Pressure Before Rec                      -0.009460   \n",
      "Combustion Air Pressure After Rec                        0.024670   \n",
      "\n",
      "                                    Combustion Air Pressure Before Rec  \\\n",
      "Soaking Zone Temp                                            -0.012085   \n",
      "Heating Zone Temp                                            -0.017834   \n",
      "Furnace pressure                                              0.008013   \n",
      "Soaking Zone Coal Motor RPM                                  -0.020569   \n",
      "Oxygen %                                                     -0.052886   \n",
      "Air Motor RPM                                                -0.069961   \n",
      "Combustion Air temp before Rec                               -0.061538   \n",
      "Combustion Air temp After Rec                                -0.009460   \n",
      "Combustion Air Pressure Before Rec                            1.000000   \n",
      "Combustion Air Pressure After Rec                             0.017708   \n",
      "\n",
      "                                    Combustion Air Pressure After Rec  \n",
      "Soaking Zone Temp                                            0.017808  \n",
      "Heating Zone Temp                                           -0.024655  \n",
      "Furnace pressure                                            -0.150466  \n",
      "Soaking Zone Coal Motor RPM                                 -0.088733  \n",
      "Oxygen %                                                     0.053667  \n",
      "Air Motor RPM                                               -0.020861  \n",
      "Combustion Air temp before Rec                              -0.057737  \n",
      "Combustion Air temp After Rec                                0.024670  \n",
      "Combustion Air Pressure Before Rec                           0.017708  \n",
      "Combustion Air Pressure After Rec                            1.000000  \n"
     ]
    }
   ],
   "source": [
    "print(X.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9659e180-624b-4216-b7a2-2d1a3286913e",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = JupyterDash(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c64e9105-c1f4-4613-a05a-9b17f5c4c0f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout= html.Div(children=[\n",
    "                      html.H1(\"Dashboards with Dash\",style={'text-align':'center'}),\n",
    "                      dcc.Dropdown(id='select_x',\n",
    "                                   options=[{'label':i, 'value':i} for i in X.columns.values],\n",
    "                                   value= corr_df.columns.values[0],#col1, #x2_df#x2_values.values(),#corr_df.columns.to_list(),\n",
    "                                   style={\"width\":\"50%\"}\n",
    "                                   ),\n",
    "                      #html.Div(id='output_container',children=[]),\n",
    "                      html.Br(),\n",
    "                      dcc.Graph(id='correlation_bar_graph',figure={})\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cb2ca1a4-3c83-467e-800d-c394c1a258c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect the Plotly graphs with Dash Components\n",
    "@app.callback(\n",
    "\n",
    "    #Output(component_id='output_container', component_property='children'),\n",
    "    Output(component_id='correlation_bar_graph', component_property='figure'),\n",
    "    [Input(component_id='select_x', component_property='value')]\n",
    ")\n",
    "def update_graph(value_chosen):\n",
    "    \n",
    "    dff = corr_df#.iloc[value_chosen]\n",
    "    #dff['column_name']=dff.columns.values\n",
    "    data = {'x':dff.columns.values,'y':dff[value_chosen]}\n",
    "    #[20, 21, 19, 18]}\n",
    "    #cols = dff[\"column_name\"] == value_chosen\n",
    "        \n",
    "    figure = px.bar(\n",
    "          data_frame=data, #corr_df,\n",
    "          x=\"x\",#dff.index.values.tolist(),\n",
    "          y=\"y\",#yy,\n",
    "          \n",
    "          template=\"plotly_dark\"\n",
    "    )\n",
    "    #figure.update_xaxes(type='category')\n",
    "    figure.update_layout(xaxis_type='category')\n",
    "    return (figure)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4da5b283-3a2f-407a-8d51-9bc733beec61",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8052/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [25/May/2022 15:20:01] \"GET /_alive_e9c09be6-3090-4e8f-bc8b-34536d3612db HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash app running on http://127.0.0.1:8052/\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_renderer/polyfill@7.v1_9_0m1653279883.8.7.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_renderer/react@16.v1_9_0m1653279883.14.0.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_renderer/prop-types@15.v1_9_0m1653279883.7.2.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_renderer/react-dom@16.v1_9_0m1653279883.14.0.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_html_components/dash_html_components.v1_1_2m1653279884.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_core_components/dash_core_components-shared.v1_15_0m1653279884.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_core_components/dash_core_components.v1_15_0m1653279884.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_renderer/dash_renderer.v1_9_0m1653279883.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-layout HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-dependencies HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_core_components/async-dropdown.v1_15_0m1611086576.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:16] \"GET /_dash-component-suites/dash_core_components/async-graph.v1_15_0m1611086576.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:17] \"GET /_favicon.ico?v=1.19.0 HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:17] \"POST /_dash-update-component HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:17] \"GET /_dash-component-suites/dash_core_components/async-plotlyjs.v1_15_0m1611086576.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:22] \"POST /_dash-update-component HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [25/May/2022 15:20:26] \"POST /_dash-update-component HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "app.run_server(mode='external', debug=False, port=8052)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa645a25-27e8-4be7-a22c-31c1c0610c1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
