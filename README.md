# SP500_ML_Daily
Machine Learning models to predict next day trend in the SP500

The main notebook is **ML_SP500_Binary_Classification.ipynb**

# 1.Data aggregation: 
In this step, data is retrieved from multiple sources, including S&P500, macro-factors such as gold price, oil price, yield price, Nasdaq, Dow Jones, VIX, and FRED data such as GDP, consumer price index, personal consumption expenditures, and industrial production. Additionally, quantitative methods such as MACD and RSI are used to analyze the data. Quality checks are performed to ensure data consistency, and the data is saved for future use.

# 2.Transforming to a 2_Class-Binary Problem: 
In this step, the problem is transformed into a binary classification problem where the next day movement is predicted as either up or down.

# 3.Machine Learning Models: 
In this step, various machine learning models are implemented to predict the next day movement. The models include Naive Bayes, Logistic Regression, K-nearest Neighbours, Support Vector Machine, Decision Tree Classifier, Bagging Decision Tree, Boosting Decision Tree, Random Forest, and Voting Classifier. The performance of each model is compared against the buy and hold (BH) strategy, where the stock is held for a long time and the performance is measured against this baseline.

# 4.ML Models vs. Buy and Hold (BH) strategy: 
In this step, the performance of each model is compared against the BH strategy. The performance of each model is evaluated using various performance metrics such as accuracy, precision, recall, and F1-score.

Annexes: Two annexes are included where the performance of the Ensemble Voting Classifier (EVC) is saved and the notebook simulation is saved for future use.

Overall, this project involves data aggregation, transformation, and machine learning to predict the next day movement in the stock market. The performance of the models is compared against the buy and hold strategy, which serves as a baseline for comparison.
