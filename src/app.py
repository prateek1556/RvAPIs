#Flask Packages
from flask import Flask, request
from flask_restful import Resource, Api

#Developer defined
from nlp.process_text import clean_text
from nlp.text_classification import find_sentiment
from lrm.linear_regression_housingprice import predict_housing_price, housing_price_model_details
from lcm.moneyball_linear_classification import predict_runs_scored, predict_runs_allowed, predict_matches_win, moneyball_model_details
from logrm.framingham_chd_logistic_regression import find_framingham_chd_prediction, framingham_model_details


app = Flask(__name__)
api = Api(app)

class TextAnalysis(Resource):
    
    def post(self):
        data = request.get_json(silent=True)
        clean_data  = clean_text(data['text'])
        senti = find_sentiment(clean_data)
        getsentiment = 'Positive' if senti else 'Negative'
        return {'text': clean_data,'sentiment':getsentiment}, 200 if clean_data else 404


class LR_HousingPrice(Resource):
    def post(self):
         data = request.get_json() #x = np.array(data).tolist() # a = np.array([1,2,3,4,5]).tolist()
         
         a=float(data['a'])
         b=float(data['b'])
         c=float(data['c'])
         d=float(data['d'])
         e=float(data['e'])
         
         house_price_pred = predict_housing_price(a,b,c,d,e).tolist()
         return {'price': house_price_pred}, 200 if house_price_pred else 404
         
    def get(self):
        MEA, MSE, RMSE, MAPE, coeff_df = housing_price_model_details() #, MSE, RMSE, MAPE = housing_price_model_details()
        return {'MEA': MEA, 'MSE':MSE, 'RMSE':RMSE, 'MAPE':MAPE,'coeff_df':coeff_df.to_json()}
        

class LC_Moneyball(Resource):
    def post(self):
        data = request.get_json()
        
        OBP = float(data['OBP'])
        SLG = float(data['SLG'])
        OOBP = float(data['OOBP'])
        OSLG = float(data['OSLG'])

        runs_scored = predict_runs_scored(OBP,SLG)
        runs_allowed = predict_runs_allowed(OOBP,OSLG)
        total_wins_season, percentage_qualification = predict_matches_win(runs_scored[0],runs_allowed[0])
        
        return { 'QualifyingPercentage':percentage_qualification,'wins':total_wins_season[0]}
    
    def get(self):
        intercept,coff = moneyball_model_details()
        return{'intercept':intercept,'cofficient':{'RunDifference':coff[0]}}
        

class LOG_framingham(Resource):
    def post(self):
        data = request.get_json()
        
        male = float(data['Gender'])
        age = float(data['Age'])
        education = float(data['Education'])
        currentSmoker = float(data['Smoking'])
        cigsPerDay = float(data['BigarettesPerDay'])
        BPMeds = float(data['BloodPressureMedication'])
        prevalentStroke = float(data['PrevelentStroke'])
        prevalentHyp = float(data['PrevalentHypertension'])
        diabetes = float(data['Diabetes'])
        totChol = float(data['TotalCholesterol'])
        sysBP = float(data['SystolicBloodPressure'])
        diaBP = float(data['DiabeticBloodPressure'])
        BMI = float(data['BodyMassIndex'])
        heartRate = float(data['HeartRate'])
        glucose = float(data['Glucose'])
        
        pred_chd_tenyears = find_framingham_chd_prediction(male, age, education, currentSmoker,cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose).tolist()
        
        return {"CoronaryHeartDisease":pred_chd_tenyears[0]}
        
        
    def get(self):
        Accuracy, TN, FP, FN, TP = framingham_model_details()
        return {"Accuracy":float(Accuracy), "TN":float(TN), "FP":float(FP), "FN":float(FN), "TP":float(TP)}
        

api.add_resource(TextAnalysis,'/cleandata')
api.add_resource(LR_HousingPrice,'/lrmodel')
api.add_resource(LC_Moneyball,'/lcmodel')
api.add_resource(LOG_framingham,'/logmodel')

if __name__ == '__main__':
    app.run(port=5000, debug=True) # it is although default