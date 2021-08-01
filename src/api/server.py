from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://mongo_db:27017')
db = client.projectDB
meetups = db['Meetups']


"""
RESOURCES
"""

class Hello(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)