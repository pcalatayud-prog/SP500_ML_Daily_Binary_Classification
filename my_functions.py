# +
#Importing Required Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import cufflinks as cf
from pandas_datareader import data
from pandas.tseries.frequencies import to_offset
import csv
from datetime import datetime
import time

import matplotlib.pyplot as plt
from scipy.optimize import brute
plt.style.use("seaborn")


# -

def data_agreggation_yahoo(start,end,a):
    df = pd.DataFrame()
    data=[]
    for ticker in a:
        
        data = yf.download(ticker, start = start, end = end)
        a=ticker+"_returns"
        df[a] = np.log(data.Open / data.Close)*100
                        
    return df


def data_agreggation_csv(start,end,name_csv,dates):
    
    
    week_13_treasury = pd.read_csv(name_csv)
    mask = (week_13_treasury["Date"]>=start) & (week_13_treasury["Date"]<=end)
    week_13_treasury = week_13_treasury.loc[mask]
    
    week_13_treasury["yield_returns"] = np.log(week_13_treasury.Open / week_13_treasury.Close)*100
    
    dates_treasury = list(week_13_treasury["Date"])
    dates_treasury_return = list(week_13_treasury["yield_returns"])
    
    
    
    data=pd.DataFrame(columns = ['Date','Yield_returns'])
    
    
    for i in dates:
        for j in range(len(dates_treasury_return)):

            if dates_treasury[j] in str(i):
                
                a=[i,dates_treasury_return[j]]
                data.loc[len(data.index)] = a
    
    data.index = data["Date"]
    
    return data
