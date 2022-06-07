from dashboardapp import app
from flask import render_template
import pandas as pd
import json, plotly
# from script_finance.wrangling import data_wrangle
import plotly.express as px
from script_finance.get_fruit_plot import get_fruit_plot
from script_finance.nasdaq_pe_ratio import get_nasdaq_pe_ratio
from script_finance.sp500_returns import get_sp500_returns

# app = Flask(__name__)

# home page
@app.route('/')
def index():  
  return render_template('index.html')

# finance project
@app.route('/project01')
def project01():
  graph1json = get_fruit_plot()
  return render_template('project01.html',graph1json= graph1json)

@app.route('/nasdaq_pe_ratio')
def nasdaq_pe_ratio():
  npr_json = get_nasdaq_pe_ratio()
  sp500_json = get_sp500_returns()
  return render_template('nasdaq_pe_ratio.html', graph1json = npr_json, graph2json = sp500_json)

# netflix project

# bilibili project
@app.route('/project-bilibili')
def get_bilibili():
  graph1json = get_fruit_plot()
  return render_template('project-bilibili.html',graph1json= graph1json)

# sidebar project
@app.route('/sidebar')
def sidebar():  
  return render_template('sidebar.html')

@app.route('/sidebar2')
def sidebar2():  
  return render_template('sidebar2.html')