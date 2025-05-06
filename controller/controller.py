"""Module providing lib from pandas to logic and plotly to draw graphs """
import pandas as pd
import plotly.express as px

def draw_graph(df, graph_type:str, x_line: str, y_line: str = ""):
    '''
        df : type dataframe Not Null
        graph_type: type String Not Null
        x_line: type String Not Null
        y_line: type String Default ""

        Getting the dataframe and type of graph, the function builds a graph using plotly.express.
        returning fig. It has to be interpreted by st.plotly_chart.
        if graph_type is equal to 'hist' 
        plotly.express.histogram Receive the df and define x. 
        to return a histogram figure
        if graph_type is equal to 'hist' 
        plotly.express.scatter receives the df, defines vector x, and defines vector y.
        to return a scatter figure  
    '''
    if graph_type == 'hist':
        fig = px.histogram(df, x=x_line)
    else:
        fig = px.scatter(df, x=x_line, y=y_line)
    return fig

def charge_file(url):
    '''
        url: type String Not null
        Getting url and return a dataframe from csv file 
        using pandas.read_csv
    '''
    return pd.read_csv(url)
