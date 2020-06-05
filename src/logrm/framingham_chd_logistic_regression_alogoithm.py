import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report , accuracy_score,confusion_matrix
import pickle

framingham = pd.read_csv('framingham.csv')

len(framingham)
len(framingham) - framingham.count()


framingham = framingham.dropna()


len(framingham)
len(framingham) - framingham.count()

print(framingham.columns)

X = framingham[['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
       'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
       'diaBP', 'BMI', 'heartRate', 'glucose']]
y = framingham['TenYearCHD']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)


with open('framinghum_log_X_test.pickle','wb') as f:
    pickle.dump(X_test,f)

X_test = open('framinghum_log_X_test.pickle','rb')
fram_X_test = pickle.load(X_test)



with open('framinghum_log_y_test.pickle','wb') as f:
    pickle.dump(y_test,f)

y_test = open('framinghum_log_y_test.pickle','rb')
fram_y_test = pickle.load(y_test)



logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)



with open('framinghum_logistic_model.pickle','wb') as f:
    pickle.dump(logmodel,f)
    
with open('framinghum_logistic_model.pickle','rb') as f:
    logmodel = pickle.load(f)

predictions = logmodel.predict(fram_X_test)

print(predictions)
print(logmodel.predict([[1,39,4,0,0,0,0,0,0,195,106,70,26.97,80,77]]))


print('Accuract Score :', accuracy_score(fram_y_test,predictions))

print(classification_report(fram_y_test,predictions))

print(confusion_matrix(fram_y_test,predictions))

con = confusion_matrix(fram_y_test,predictions)

print(con)
con[0][0]
con[0][1]
