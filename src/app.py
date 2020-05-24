from flask import Flask, request
from flask_restful import Resource, Api
from process_text import clean_text
from text_classification import find_sentiment


app = Flask(__name__)
api = Api(app)

app = Flask(__name__)
api = Api(app)


class TextAnalysis(Resource):
    
    def post(self):
        data = request.get_json(silent=True)
        clean_data  = clean_text(data['text'])
        senti = find_sentiment(clean_data)
        getsentiment = 'Positive' if senti else 'Negative'
        return {'text': clean_data,'sentiment':getsentiment}
       

api.add_resource(TextAnalysis,'/cleandata')

if __name__ == '__main__':
    app.run(port=5000, debug=True) # it is although default