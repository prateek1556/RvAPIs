import pandas as pd
import numpy as np
from sklearn import metrics
import pickle

def predict_housing_price(a,b,c,d,e):
    with open('linear_regression.pickle','rb') as f:
        linear_reg = pickle.load(f)
        
    return linear_reg.predict([[a,b,c,d,e]])


def housing_price_model_details():
    
    X = open('X_col_names_LR.pickle','rb')
    X_names_LR = pickle.load(X)
    
    y_test = open('y_test_LR.pickle','rb')
    y_test_LR = pickle.load(y_test)
    
    X_test = open('X_test_LR.pickle','rb')
    X_test_LR = pickle.load(X_test)
    
    with open('linear_regression.pickle','rb') as f:
        linear_reg = pickle.load(f)
    
    predictions = linear_reg.predict(X_test_LR)
    coeff_df = pd.DataFrame(linear_reg.coef_,X_names_LR.columns,columns=['Coefficient'])
    
    MEA =  metrics.mean_absolute_error(y_test_LR, predictions)
    MSE = metrics.mean_squared_error(y_test_LR, predictions)
    RMSE = np.sqrt(metrics.mean_squared_error(y_test_LR, predictions))
    MAPE = np.mean(np.abs((y_test_LR - predictions) / y_test_LR)) * 100
    
    return MEA,MSE,RMSE,MAPE,coeff_df