import plotly.express as px 
import json, plotly 
import pandas as pd

def get_fruit_plot():
    df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    # fig = px.bar(df, x='Fruit', y='Amount', barmode='group')
    fig = px.bar(df, x='Fruit', y='Amount', color='City',    barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON