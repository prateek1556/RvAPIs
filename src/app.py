#Flask Packages
from flask import Flask, request
from flask_restful import Resource, Api

#Developer defined
from nlp.process_text import clean_text
from nlp.text_classification import find_sentiment
from lrm.linear_regression_housingprice import predict_housing_price, housing_price_model_details


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
         a=data['a']
         b=data['b']
         c=data['c']
         d=data['d']
         e=data['e']
         house_price_pred = predict_housing_price(a,b,c,d,e).tolist()
         return {'price': house_price_pred}, 200 if house_price_pred else 404
         
    def get(self):
        MEA, MSE, RMSE, MAPE, coeff_df = housing_price_model_details() #, MSE, RMSE, MAPE = housing_price_model_details()
        return {'MEA': MEA, 'MSE':MSE, 'RMSE':RMSE, 'MAPE':MAPE,'coeff_df':coeff_df.to_json()}
        

api.add_resource(TextAnalysis,'/cleandata')
api.add_resource(LR_HousingPrice,'/lrmodel')

if __name__ == '__main__':
    app.run(port=5000, debug=True) # it is although default