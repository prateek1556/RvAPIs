#Liner Regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from statsmodels.api import OLS
import pickle

moneyball = pd.read_csv('baseball.csv')

moneyball['RD'] = moneyball['RS']-moneyball['RA']

y = moneyball["W"]
X = moneyball[["RD"]]


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0,random_state=101)

with open('X_col_names_LC_diff.pickle','wb') as f:
    pickle.dump(X,f)

X = open('X_col_names_LC_diff.pickle','rb')
X_names_LC_diff = pickle.load(X)



linear_cls_diff = LinearRegression()
linear_cls_diff.fit(X_train,y_train)


with open('linear_classification_diff.pickle','wb') as f:
    pickle.dump(linear_cls_diff,f)
    
with open('linear_classification_diff.pickle','rb') as f:
    linear_cls_diff = pickle.load(f)

print(linear_cls_diff.coef_)
print(linear_cls_diff.intercept_)

OLS(y_train,X_train).fit().summary()


coeff_df = pd.DataFrame(linear_cls_diff.coef_,X_names_LC_diff.columns,columns=['Coefficient'])
print(coeff_df)

linear_cls_diff.predict([[134]])


#2ND REGRESSION


