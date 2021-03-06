import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from statsmodels.api import OLS
import pickle


moneyball = pd.read_csv('baseball.csv')

y = moneyball["RS"]
X = moneyball[["OBP","SLG"]]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0,random_state=101)


with open('X_col_names_LC_rs.pickle','wb') as f:
    pickle.dump(X,f)

X = open('X_col_names_LC_rs.pickle','rb')
X_names_LC_RS = pickle.load(X)



linear_cls_RS = LinearRegression()
linear_cls_RS.fit(X_train,y_train)

with open('linear_classification_rs.pickle','wb') as f:
    pickle.dump(linear_cls_RS,f)
    
with open('linear_classification_rs.pickle','rb') as f:
    linear_cls_RS = pickle.load(f)



print(linear_cls_RS.coef_)
print(linear_cls_RS.intercept_)

coeff_df = pd.DataFrame(linear_cls_RS.coef_,X_names_LC_RS.columns,columns=['Coefficient'])
print(coeff_df)

OLS(y_train,X_train).fit().summary()


linear_cls_RS.predict([[.33,.44]])

