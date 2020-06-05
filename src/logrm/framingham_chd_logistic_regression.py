from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


def find_framingham_chd_prediction(male, age, education, currentSmoker, cigsPerDay, BPMeds,
                                   prevalentStroke, prevalentHyp, diabetes, totChol, sysBP,
                                   diaBP, BMI, heartRate, glucose):
    
    
    with open('logrm/models/framinghum_logistic_model.pickle','rb') as f:
        logmodel = pickle.load(f)
    
    
    #1,39,4,0,0,0,0,0,0,195,106,70,26.97,80,77
    pred = logmodel.predict([[male, age, education, currentSmoker, cigsPerDay, BPMeds,prevalentStroke, prevalentHyp, diabetes, totChol, sysBP,diaBP, BMI, heartRate, glucose]]) 
    return pred
    
def framingham_model_details():
    X_test = open('logrm/models/framinghum_log_X_test.pickle','rb')
    fram_X_test = pickle.load(X_test)
    
    y_test = open('logrm/models/framinghum_log_y_test.pickle','rb')
    fram_y_test = pickle.load(y_test)
    
    with open('logrm/models/framinghum_logistic_model.pickle','rb') as f:
        logmodel = pickle.load(f)
    
    
    predictions = logmodel.predict(fram_X_test)
    
    Accuracy = accuracy_score(fram_y_test,predictions)
    
    #print(classification_report(fram_y_test,predictions))
    
    con_matrix = confusion_matrix(fram_y_test,predictions)
    TN = con_matrix[0][0]
    FP = con_matrix[0][1]
    FN = con_matrix[1][0]
    TP = con_matrix[1][1]
    
    return Accuracy, TN, FP, FN, TP
    
