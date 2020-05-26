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
    
"""

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name,items), None)
        return {'item': item}, 200 if item else 404
    
    def post(self,name):
        if next(filter(lambda x: x['name'] == name,items), None):
            return {'message':"An item with name'{}' already exist.".format(name)}, 400
            
        data = request.get_json(silent=True)
        item = {'name': name,'price': data['price']}
        items.append(item)
        return item, 201
    
    

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000, debug=True) # it is although default

"""
