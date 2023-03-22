import numpy as np
from scipy import stats
import pandas as pd
import time
import time
#import math
#importing packages
import seaborn as sns
import matplotlib.pyplot as plt
#import math

def performance_model(returns_BH_test,y_test_real,y_test_predicted,returns_open_close_daily): 
    '''
    Arguments
    ==========
    X_test
    
    Y_test_real
    
    Y_test_predicted
    
    returns_open_close_daily
    ''' 
        
    #Testing decisions
    validation = pd.DataFrame()

    validation["returns_real_buy_hold_daily_test"]=returns_BH_test
    validation["returns_open_close_daily"]=returns_open_close_daily
    validation["y_test_real"]=y_test_real
    validation["y_test_predicted"]=y_test_predicted
    validation["action"]=validation["y_test_real"]==validation["y_test_predicted"]
    validation["position"] = np.where(validation["y_test_predicted"]<1, -1, 1 )

    #Performance strategy
    validation["strategy_performance_day"] = 1 + validation.position * validation["returns_open_close_daily"]
    validation["strategy_creturns"]=validation.strategy_performance_day.cumprod()

    #Performance buy and hold
    validation["hold_performance_day"] = 1 + validation["returns_real_buy_hold_daily_test"]
    validation["hold_creturns"]=validation.hold_performance_day.cumprod()

    #Calculating drawdown
    validation["cummax_BH"] = validation.hold_creturns.cummax()
    validation["cummax_strategy"] = validation.strategy_creturns.cummax()

    validation["drawndown_BH"] = (validation["cummax_BH"] - validation["hold_creturns"])/validation["cummax_BH"]
    validation["drawndown_strategy"] = (validation["cummax_strategy"] - validation["strategy_creturns"])/validation["cummax_strategy"]

    perf = validation["strategy_creturns"].iloc[-1] # absolute performance of the strategy
    perf = round(perf, 3)

    benchmark = validation["hold_creturns"].iloc[-1] #Benchmark - buy & hold strategy
    benchmark = round(benchmark, 3)

    outperf = perf - benchmark # out-/underperformance of strategy

    drawdown_BH = round(validation["drawndown_BH"].max(),3)
    drawdown_strategy = round(validation["drawndown_strategy"].max(),3)

    print("Strategy Performance: " + str(perf))
    print("Hold and Buy Performance: " + str(benchmark))
    print("Strategy Maximun Drawdown: " + str(drawdown_strategy))
    print("Hold and Buy Drawdown: " + str(drawdown_BH))
    
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    # First subplot: hold_creturns vs. strategy_creturns
    validation[["hold_creturns","strategy_creturns"]].dropna().plot(ax=axs[0], title="Profit Factor. ML MODEL vs BH", fontsize=12)
    axs[0].set_xlabel("Date", fontsize=12)
    axs[0].set_ylabel("PF", fontsize=12)
    axs[0].tick_params(axis='x', labelrotation=45, labelsize=16)

    # Second subplot: drawndown_BH vs. drawndown_strategy
    validation[["drawndown_BH","drawndown_strategy"]].dropna().plot(ax=axs[1], title="Drawdown. ML MODEL vs BH", fontsize=12)
    axs[1].set_xlabel("Date", fontsize=12)
    axs[1].set_ylabel("Drawdown", fontsize=12)
    axs[1].tick_params(axis='x', labelrotation=45, labelsize=16)

    # Set common legend for the two subplots
    plt.rc('legend',fontsize=20) # using a size in points
    handles, labels = axs[0].get_legend_handles_labels()
    #fig.legend(handles, labels, loc="upper center", ncol=2)

    # Show the plot
    plt.tight_layout()
    plt.show()

        
    return validation


