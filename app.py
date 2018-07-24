# import necessary libraries
import numpy as np
from numpy.polynomial.polynomial import polyfit
from scipy import stats
import pandas as pd
from urllib.request import urlopen
import time

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import requests

from flask_sqlalchemy import SQLAlchemy
# PyMySQL 
import pymysql

from config import db_pwd
from config import AV_apikey

#################################################
# common variables needed across functions
#################################################
app = Flask(__name__)
#################################################
# Database Setup 
#################################################

pymysql.install_as_MySQLdb()
# Create Engine and Pass in MySQL Connection
engine = create_engine("mysql://root:"+db_pwd+"@localhost:3306/stockuser")
conn = engine.connect()

 # def __repr__(self):
#        return '<Pet %r>' % (self.name)

#############################
# Initial setup if any
#############################

#@app.before_first_request
#def setup():

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/analyzeStock")
def analyzeStock():
    return render_template("stock_dashboard.html")


#######################################
# Data API routes
#########################################
#### commneted out for now. Update later based on what we want to provide APIs to

@app.route("/api/fundamentals")
def fundamentals():
    ticker = request.args['ticker']
    #pull results from db for the ticker and return as json object

   #query DB
    query_string = "SELECT stock_return,pe,pb,fcf FROM stocks WHERE ticker = '"+ticker+"' and stock_return != 0;"
    data = pd.read_sql(query_string, conn)

    stockreturn = []
    pe = []
    pb = []
    fcf = []
    for row in data.iterrows():
        stockreturn.append(row[1].stock_return)
        pe.append(row[1].pe)
        pb.append(row[1].pb)
        fcf.append(row[1].fcf)
    
    stockreturnint = [float(i) for i in stockreturn]
    peint = [float(i) for i in pe]
    pbint = [float(i) for i in pb]
    fcfint = [float(i) for i in fcf]

    pe_slope, pe_int, pe_r_value, pe_p_value, pe_std_err = stats.linregress(peint, stockreturnint)
    pb_slope, pb_int, pb_r_value, pb_p_value, pb_std_err = stats.linregress(pbint, stockreturnint)
    fcf_slope, fcf_int, fcf_r_value, fcf_p_value, fcf_std_err = stats.linregress(fcfint, stockreturnint)

    regPE = [pe_slope, pe_int, pe_r_value, pe_p_value, pe_std_err]
    regPB = [pb_slope, pb_int, pb_r_value, pb_p_value, pb_std_err]
    regFCF = [fcf_slope, fcf_int, fcf_r_value, fcf_p_value, fcf_std_err]
    

    fundamentals_data ={
        "ticker": ticker,
        "returns": stockreturnint,
        "pe": peint,
        "fcf": fcfint,
        "pb": pbint,
        "regPE": regPE,
        "regFCF": regFCF,
        "regPB": regPB
        }

    return jsonify(fundamentals_data)


#get trading data for selected ticker, ticker needs to be sent in as URL argument
@app.route("/api/tradingData")
def tradingData():
    ticker = request.args['ticker']
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&apikey='+AV_apikey
    response = requests.get(url).json()
    data = response['Time Series (Daily)']
    dates = list(data.keys())
    
    price_changes = []
    start_date = dates[-1]
    ref_price = float(data[start_date]['4. close'])

    for i in range(0, len(dates)):
        date = dates[i]
        price = float(data[date]['4. close'])
        price_changes.append(((price-ref_price)/ref_price)*100) 

    plot_data = {
                "ticker":ticker,
                "dates": dates,
                "price_changes": price_changes
                }
    
    return jsonify(plot_data)


if __name__ == "__main__":
    app.run()
