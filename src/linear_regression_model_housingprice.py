#Liner Regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

USAhousing = pd.read_csv('USA_Housing.csv')

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)




# Pickling the dataset
with open('X_col_names_LR.pickle','wb') as f:
    pickle.dump(X,f)

# Unpickling dataset
X = open('X_col_names_LR.pickle','rb')
X_names_LR = pickle.load(X)




with open('y_test_LR.pickle','wb') as f:
    pickle.dump(y_test,f)

# Unpickling dataset
y_test = open('y_test_LR.pickle','rb')
y_test_LR = pickle.load(y_test)


with open('X_test_LR.pickle','wb') as f:
    pickle.dump(X_test,f)

# Unpickling dataset
X_test = open('X_test_LR.pickle','rb')
X_test_LR = pickle.load(X_test)



linear_reg = LinearRegression()
linear_reg.fit(X_train,y_train)


# Saving our classifier
with open('linear_regression.pickle','wb') as f:
    pickle.dump(linear_reg,f)
    
with open('linear_regression.pickle','rb') as f:
    linear_reg = pickle.load(f)



print(linear_reg.intercept_)

coeff_df = pd.DataFrame(linear_reg.coef_,X_test_LR.columns,columns=['Coefficient'])
print(coeff_df)
coeff_df.to_json (r'coeff_df_DataFrame.json')
print(type(coeff_df))


predictions = linear_reg.predict(X_test_LR)

a=1
b=1
c=1
d=1
e=1
x = metrics.mean_absolute_error(y_test_LR, predictions)
print(type(x))
                                
linear_reg.predict([[a,b,c,d,e]])
print('MAE:', metrics.mean_absolute_error(y_test_LR, predictions))
print('MSE:', metrics.mean_squared_error(y_test_LR, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test_LR, predictions)))
print('MAPE:', np.mean(np.abs((y_test_LR - predictions) / y_test_LR)) * 100)