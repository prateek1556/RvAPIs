#Flask Packages
from flask import Flask, request
from flask_restful import Resource, Api

#Developer defined
from nlp.process_text import clean_text
from nlp.text_classification import find_sentiment
from lrm.linear_regression_housingprice import predict_housing_price, housing_price_model_details
from lcm.moneyball_linear_classification import predict_runs_scored, predict_runs_allowed, predict_matches_win


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
        #print(OBP)
        runs_scored = predict_runs_scored(OBP,SLG)
        runs_allowed = predict_runs_allowed(OOBP,OSLG)
        #print(runs_scored)
        print("______________________________")
        print(runs_scored[0])
        print(runs_allowed[0])
        total_wins_season, percentage_qualification = predict_matches_win(runs_scored[0],runs_allowed[0])
        
        return { 'QualifyingPercentage':percentage_qualification,'wins':total_wins_season[0]}
        
        

api.add_resource(TextAnalysis,'/cleandata')
api.add_resource(LR_HousingPrice,'/lrmodel')
api.add_resource(LC_Moneyball,'/lcmodel')

if __name__ == '__main__':
    app.run(port=5000, debug=True) # it is although default