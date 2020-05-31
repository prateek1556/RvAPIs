import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from statsmodels.api import OLS
import pickle


moneyball = pd.read_csv('baseball.csv')


print(len(moneyball) - moneyball.count())
print(len(moneyball))


del moneyball['RankSeason']
del moneyball['RankPlayoffs']

print(len(moneyball) - moneyball.count())
print(len(moneyball))

moneyball = moneyball.dropna()


print(len(moneyball) - moneyball.count())
print(len(moneyball))

y = moneyball["RA"]
X = moneyball[["OOBP","OSLG"]]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0,random_state=101)


with open('X_col_names_LC_ra.pickle','wb') as f:
    pickle.dump(X,f)

X = open('X_col_names_LC_ra.pickle','rb')
X_names_LC_RA = pickle.load(X)



linear_cls_RA = LinearRegression()
linear_cls_RA.fit(X_train,y_train)

with open('linear_classification_ra.pickle','wb') as f:
    pickle.dump(linear_cls_RA,f)
    
with open('linear_classification_ra.pickle','rb') as f:
    linear_cls_RA = pickle.load(f)



print(linear_cls_RA.coef_)
print(linear_cls_RA.intercept_)

coeff_df = pd.DataFrame(linear_cls_RA.coef_,X_names_LC_RA.columns,columns=['Coefficient'])
print(coeff_df)

OLS(y_train,X_train).fit().summary()


linear_cls_RA.predict([[.33,.44]])

