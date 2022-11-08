from jupyter_dash import JupyterDash
import dash
from dash import dcc  
from dash import html  
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
from tkinter.ttk import Style
from xml.etree.ElementPath import ops

avocado= pd.read_csv('avocado.csv')
avocado= avocado.sort_values(by='Date')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config['suppress_callback_exceptions']= True

colors = {
    'white': '#FFFFFF',
    'black':'#000000',
    'yellow':'#ffad26',
    'grey':'#DADADA',
    'dark_grey':'#a1a1a1',    
    'green':'#00e79e',
    'light_blue':'#6d66f7',
    'blue':'#232a44',
    'dark_blue':'#161930',
    }

tab_unselected_style = {
    'width': '700px',
    'border': 'none',
    'boxShadow': 'inset 0px -1px 0px 0px lightgrey',
    'background': colors['grey'],
    'paddingTop': 5,
    'paddingBottom': 0,
    'height': '35px'
}
tab_selected_style = {
    'width': '700px',
    'boxShadow': 'none',
    'borderLeft': 'none',
    'borderRight': 'none',
    'borderTop': 'none',
    'borderBottom': '4px #DBAE58 solid',
    'background': colors['dark_grey'],
    'paddingTop': 5,
    'paddingBottom': 0,
    'height': '37px'
}

class Page_1():
    def Page_1_layout(self):
        tab_1_layout = html.Div([
                        html.Br(),
                        html.Div([
                            html.Div([
                                    html.H6('Choose a State:', style={'textAlign': 'left', 'color': colors['grey'], 'marginBottom': '10px'}),
                                    dcc.Dropdown(
                                            id='opt',
                                            options= avocado['region'].unique(),
                                            value=avocado['region'].unique()[0],
                                            style={'textAlign': 'center', 'marginBottom': '10px', "width": "60%"},
                                            ),
                        html.Br(),
                        html.P("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.html. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",style={"width": "100%", "aligntext": "justify", 'color': colors['grey'],})
                            ], className="six columns"),
                        html.Div([
                                dcc.Graph(
                                    id='dem-graph-0',
                                    figure={}
                                )
                            ], className="six columns"),
                        ], className="row", style={"margin": "1% 3%"}),
#------------------------------------------------------ Second Row --------------------------------------------
                    html.Div([
                            html.Div([
                                html.H6('Average Price Change in a Specific Time period', style={'textAlign': 'center', 'color': colors['white']}),
                                dcc.DatePickerRange(
                                    id='input_date',
                                    month_format='YYYY/MM/DD',
                                    show_outside_days=True,
                                    minimum_nights=0,
                                    initial_visible_month=avocado['Date'].min(),
                                    min_date_allowed=avocado['Date'].min(),
                                    max_date_allowed=avocado['Date'].max(),
                                    start_date=datetime.strptime("2015-01-04", "%Y-%m-%d").date(),
                                    end_date=datetime.strptime("2016-02-01", "%Y-%m-%d").date(),
                                    style={'textAlign': 'center', "vertical": "center", 'marginBottom': '10px', 'width': '100%'}
                                ),
                                dcc.Graph(
                                    id='dem-graph-1',
                                )
                            ], className="four columns"),
                            html.Div([
                                html.H6('Average Price Change Analysis for Different Types', style={'textAlign': 'center', 'color': colors['white']}),
                                dcc.RadioItems(
                                                id = 'input-radio-button',
                                                options = [dict(label = 'ORGANIC', value = 'organic'),
                                                            dict(label = 'CONVENTIONAL', value = 'conventional'),                                                               
                                                            ],
                                                value = 'organic', style={'textAlign': 'center', 'color': colors['grey']}, labelStyle={'display': 'inline-block'}
                                                ),
                                html.Br(),
                                dcc.Graph(
                                    id='dem-graph-2',
                                )
                            ], className="four columns"),
                            html.Div([
                                html.H6('Sales Volume Analysis', style={'textAlign': 'center', 'color': colors['white']}),
                                dcc.RangeSlider(min = 2015, max = 2018, step = 1, id = 'slider', value=[2015,2018], marks={ 2015: '2015', 2016: '2016', 2017: '2017', 2018: '2018'}),
                                dcc.Graph(
                                    id='dem-graph-3',
                                )
                            ], className="four columns")
                    ], className="row", style={"margin": "3% 3%"}),
#---------------------------------------------------------3rd Row ------------------------------------------------------
                    html.Div([
                    ], className="row", style={"margin": "1% 3%"}),
                    ],style={"margin": "1% 1%"})
        return tab_1_layout


class Page_2():
    def Page_2_layout(self):
        tab_2_layout = html.Div([
                        html.Br(), #One Empty Line Break
                        html.Div([
                            html.Div([
                                    html.H6('Choose a State:', style={'textAlign': 'left', 'color': colors['grey'], 'marginBottom': '10px'}),
                                    dcc.Dropdown(
                                            id='opt2',
                                            options= avocado['region'].unique(),
                                            value=avocado['region'].unique()[0],
                                            style={'textAlign': 'center', 'marginBottom': '10px', "width": "60%"},
                                            ),
                        html.Br(),
                        html.P("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.html. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",style={"width": "100%", "aligntext": "justify", 'color': colors['grey'],})
                            ], className="six columns"),
                        html.Div([
                                dcc.Graph(
                                    id='dem-graph-7',
                                    figure={
                                    }
                                )
                            ], className="six columns"),
                        ], className="row", style={"margin": "1% 3%"}),
#------------------------------------------------------ Second Row --------------------------------------------
                    html.Div([
                            html.Div([
                                html.H6('Total Sales Volume Analysis in a Specific Time period', style={'textAlign': 'center', 'color': colors['white']}),
                                dcc.DatePickerRange(
                                    id='input_date_2',
                                    month_format='YYYY/MM/DD',
                                    show_outside_days=True,
                                    minimum_nights=0,
                                    initial_visible_month=avocado['Date'].min(),
                                    min_date_allowed=avocado['Date'].min(),
                                    max_date_allowed=avocado['Date'].max(),
                                    start_date=datetime.strptime("2015-01-04", "%Y-%m-%d").date(),
                                    end_date=datetime.strptime("2016-03-25", "%Y-%m-%d").date(),
                                    style={'textAlign': 'center', "vertical": "center", 'marginBottom': '10px', 'width': '100%'}
                                ),
                                dcc.Graph(
                                    id='dem-graph-8',
                                )
                            ], className="four columns"),
                            html.Div([
                                html.H6('Top 20 States with greatest sales volume', style={'textAlign': 'center', 'color': colors['white']}),
                                dcc.RadioItems(
                                                id = 'input-radio-button-02',
                                                options = [dict(label = 'ORGANIC', value = 'organic'),
                                                            dict(label = 'CONVENTIONAL', value = 'conventional'),                                                               
                                                            ],
                                                value = 'organic', style={'textAlign': 'center', 'color': colors['grey']}, labelStyle={'display': 'inline-block'}
                                                ),
                                html.Br(),
                                dcc.Graph(
                                    id='dem-graph-9',
                                )
                            ], className="four columns"),
                            html.Div([
                                html.H6('Cumulative Sales Volume Analysis', style={'textAlign': 'center', 'color': colors['white']}),
                                html.Br(),
                                html.Br(),
                                dcc.Graph(
                                    id='dem-graph-10',
                                )
                            ], className="four columns")
                    ], className="row", style={"margin": "3% 3%"}),
                    html.Div([
                    ], className="row", style={"margin": "1% 3%"}),
                    ],style={"margin": "1% 1%"})
        return tab_2_layout

class Page_3():
    def Page_3_layout(self):
        tab_3_layout = html.Div([
                        html.Div([
                        html.Br(),
                        html.H3('Thank you for checking out my kernel!',style={'textAlign': 'left','color': colors['grey']}),
                        html.P("Please upvote if you like the dashboard and if you have any suggestions feel free to leave a comment!",style={"width": "100%", "aligntext": "justify", 'color': colors['grey'],}),
                        html.Br(),
                        html.Br(),
                        html.H4('Check my Github for source code:',style={'textAlign': 'left','color': colors['grey']}),
                        html.A("My Github Link", href='https://www.github.com/Ashovitz', target="_blank", style={'textAlign': 'left','color': colors['light_blue']}),
                        html.Br(),
                        html.Br(),                        
                        html.H4('Refrences:',style={'textAlign': 'left','color': colors['grey']}),
                        html.P("The data set used to create the dashboard can be found at:",style={"width": "100%", "aligntext": "justify", 'color': colors['grey'],}),
                        html.A("http://www.https://www.kaggle.com/datasets/neuromusic/avocado-prices", href='https://www.kaggle.com/datasets/neuromusic/avocado-prices', target="_blank", style={'textAlign': 'left','color': colors['light_blue']}),
                        ], className="row", style={"margin": "1% 3%"}),
                                ], className="row"),

        return tab_3_layout



tabs_container_styles = {"margin": "1% 50%", "verticalAlign":"middle", 'color':colors['black']}

app.layout = html.Div (
    children=[
        html.Div([
            html.Div([
                    html.Img(src=r'assets/plotly_logo.png', alt='image', width="400", height="80", ),
                    html.Br(),
                    html.H2('Avocado Sales Analysis',style={'textAlign': 'center','color': colors['white']}),
                    ], style={'textAlign': 'center'}, className="rows"),
        ], className="row", style={"margin": "1% 1%"}),

    dcc.Tabs(id="tabs", className="row",style={"margin": "2% 35%","verticalAlign":"middle"},
            value='Tab_01', 
            children=[dcc.Tab(label='Line Charts',
                                value='Tab_01', 
                                style=tab_unselected_style, 
                                selected_style = tab_selected_style
                            ),
                        dcc.Tab(label='Pie Charts', value='Tab_02',
                                style=tab_unselected_style , 
                                selected_style = tab_selected_style                                                                                                
                            ),
                        dcc.Tab(label='About', value='Tab_03',
                                style=tab_unselected_style , 
                                selected_style = tab_selected_style                                                                                                
                            ),   
                    ], 
            ),
    html.Div(id='tabs-content')
            ],
    style={'backgroundColor': colors['dark_blue']},
)



@app.callback(
    Output(component_id='tabs-content', component_property='children'),
    Input(component_id='tabs', component_property='value')
    )
def render_content(tab):
    if tab == 'Tab_01':
        return Page_1().Page_1_layout()
    elif tab == 'Tab_02':
        return Page_2().Page_2_layout()
    elif tab == 'Tab_03':
        return Page_3().Page_3_layout()

# Page 01 - Plot 01
@app.callback(
    Output(component_id='dem-graph-0', component_property='figure'),
    Input(component_id='opt', component_property='value')
)
def update_graph(selected_gepgraphy):
    line_fig = px.line(avocado[avocado['region']==selected_gepgraphy], x='Date' , y='AveragePrice',color='type')
    line_fig.update_layout(paper_bgcolor=colors['blue'], 
                            plot_bgcolor=colors['blue'],
                            font=dict(family="Courier New, Monospace",
                                        size=18,
                                        color=colors['grey']
                                    )
                        )
    line_fig.update_xaxes(color=colors['grey'])
    line_fig.update_yaxes(color=colors['grey'])
    return line_fig

# Page 01 - Plot 02
@app.callback(
    Output(component_id='dem-graph-1', component_property='figure'),
    [Input('input-radio-button', 'value'),Input('opt', 'value'), Input('input_date', 'start_date'), Input('input_date', 'end_date')]
)
def update_graph(selected_type, selected_region, selected_start_date, selected_end_date):
    line_fig = px.line(avocado[(avocado['region']==selected_region) & (avocado['type']==selected_type) & (avocado['Date'] < selected_end_date) & (avocado['Date'] > selected_start_date)], 
        x = 'Date', y ='AveragePrice',
        )
    line_fig.update_traces(line_color=colors['light_blue'])
    line_fig.update_xaxes(color=colors['grey'])
    line_fig.update_yaxes(color=colors['grey'])
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Average {} Avocado Price in {} between <br> {} to {}".format(selected_type, selected_region, selected_start_date, selected_end_date),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
            xaxis_title="<b>Date</b>",
            yaxis_title='<b>Average Price</b>',
        font=dict(
                family="Courier New, Monospace",
                size=14,
                color=colors['grey']
                )
    )
    return line_fig

# Page 01 - Plot 03
@app.callback(
    Output(component_id='dem-graph-2', component_property='figure'),
    [Input('input-radio-button', 'value'),Input('opt', 'value')]
)
def update_graph(selected_type, selected_region):
    line_fig = px.line(avocado[(avocado['region']==selected_region) & (avocado['type']==selected_type)], 
        x = 'Date', y ='AveragePrice',
    )
    line_fig.update_traces(line_color=colors['light_blue'])
    line_fig.update_xaxes(color=colors['grey'])
    line_fig.update_yaxes(color=colors['grey'])
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Average Price for {} Avocado <br> in {} State".format(selected_type, selected_region),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
            xaxis_title="<b>Date</b>",
            yaxis_title='<b>Average Price</b>',
        font=dict(
                family="Courier New, Monospace",
                size=14,
                color=colors['grey']
                )
    )
    return line_fig

# Page 01 - Plot 04
@app.callback(
    Output(component_id='dem-graph-3', component_property='figure'),
    [Input('opt', 'value'), Input('slider', 'value')]
)
def update_graph(selected_region, selected_range):
    avocado_group_1 = avocado[['region', 'type', 'year', 'Total Volume']].groupby(['region', 'type', 'year']).sum()
    avocado_group_2 = avocado_group_1[(avocado_group_1.index.get_level_values(0)==selected_region)]
    avocado_group_3 = avocado_group_2[(avocado_group_2.index.get_level_values(2) <= selected_range[1]) & (avocado_group_2.index.get_level_values(2) >= selected_range[0])]
    line_fig = px.bar(avocado_group_3, 
                        x = avocado_group_3.index.get_level_values(1), y =avocado_group_3['Total Volume'].values, 
                        color=avocado_group_3.index.get_level_values(1), 
                        barmode = 'group',
                        )
    line_fig.update_xaxes(color=colors['grey'])
    line_fig.update_yaxes(color=colors['grey'])
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Cumulative Sales Volume for {} <br> between {} and {}".format(selected_region, selected_range[0], selected_range[1]),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
            xaxis_title="<b>Avocado Type</b>",
            yaxis_title='<b>Cumulative Sales Volume</b>',
        font=dict(
                family="Courier New, Monospace",
                size=14,
                color=colors['grey']
                )
    )
    return line_fig

# Page 2 - Plot 01
@app.callback(
    Output(component_id='dem-graph-7', component_property='figure'),
    Input(component_id='opt2', component_property='value')
)
def update_graph(selected_gepgraphy):
    avocado_grouped_6 = avocado[avocado['region']==selected_gepgraphy][['region', 'type', 'Total Volume']].groupby(['region', 'type']).sum()
    line_fig = px.pie(avocado_grouped_6, values="Total Volume", names= avocado_grouped_6.index.get_level_values(1))
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Total Sales Volume for {} State".format(selected_gepgraphy),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
        font=dict(
                family="Courier New, Monospace",
                size=18,
                color=colors['grey']
                )
    )
    return line_fig

# Page 2 - Plot 02
@app.callback(
    Output(component_id='dem-graph-8', component_property='figure'),
    [Input(component_id='opt2', component_property='value'), Input('input_date_2', 'start_date'), Input('input_date_2', 'end_date')]
)
def update_graph(selected_gepgraphy, selected_start_date, selected_end_date):
    avocado_grouped_7 = avocado[(avocado['region']==selected_gepgraphy) & ((avocado['Date']>= selected_start_date) & (avocado['Date']< selected_end_date))][['region','Date', 'type', 'Total Volume']].groupby(['region','Date', 'type']).sum()
    line_fig = px.pie(avocado_grouped_7, values="Total Volume", names= avocado_grouped_7.index.get_level_values(2))
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Total Sales Volume for {} <br> in {} to {}".format(selected_gepgraphy, selected_start_date, selected_end_date),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
        font=dict(
                family="Courier New, Monospace",
                size=18,
                color=colors['grey']
                )
    )
    return line_fig

# Page 2 - Plot 03
@app.callback(
    Output(component_id='dem-graph-9', component_property='figure'),
    [Input(component_id='input-radio-button-02', component_property='value')]
)
def update_graph(selected_type):
    avocado_grouped_8 = avocado[avocado['type']==selected_type][['region', 'type', 'Total Volume']].groupby(['region', 'type']).sum()
    avocado_grouped_8 = avocado_grouped_8.sort_values('Total Volume').head(20)
    line_fig = px.pie(avocado_grouped_8, values="Total Volume", names= avocado_grouped_8.index.get_level_values(0))
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Top 20 States with greatest Total <br> {} avocado Sales Volume".format(selected_type),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
        font=dict(
                family="Courier New, Monospace",
                size=14,
                color=colors['grey']
                )
    )
    return line_fig

# Page 2 - Plot 04
@app.callback(
    Output(component_id='dem-graph-10', component_property='figure'),
    [Input(component_id='input-radio-button-02', component_property='value'), Input(component_id='opt2', component_property='value')]
)
def update_graph(selected_type, selected_gepgraphy):
    avocado_grouped_9 = avocado[(avocado['type']==selected_type) & (avocado['region']==selected_gepgraphy)][['region', 'type', 'Small Bags', 'Large Bags', 'XLarge Bags', 'Total Bags']].groupby(['region', 'type']).sum()
    line_fig = px.pie(values=[avocado_grouped_9.iloc[0,0], avocado_grouped_9.iloc[0,1], avocado_grouped_9.iloc[0,2]], 
                        names=[avocado_grouped_9.columns[0], avocado_grouped_9.columns[1], avocado_grouped_9.columns[2]],
                        )
    line_fig.update_layout(
        paper_bgcolor=colors['blue'], 
        plot_bgcolor=colors['blue'],
        title=dict(
                text="Cumulative Sales for Different Bag Size <br> in {} State.".format(selected_gepgraphy),
                x=0.5,
                y=0.95,
                font=dict(
                        family="Courier New, Monospace",
                        size=18,
                        color=colors['grey']
                        )
                ),
        font=dict(
                family="Courier New, Monospace",
                size=18,
                color=colors['grey']
                )
    )
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True) 
