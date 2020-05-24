from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from process_text import clean_text


app = Flask(__name__)
api = Api(app)

items = []

from flask import Flask, request
from flask_restful import Resource, Api
from process_text import *


app = Flask(__name__)
api = Api(app)


class CleanText(Resource):
    
    def post(self):
        data = request.get_json(silent=True)
        clean_data  = clean_text(data['text'])
        return {'text': clean_data}
    

api.add_resource(CleanText,'/cleandata')


if __name__ == '__main__':
    app.run(port=5000, debug=True) # it is although default