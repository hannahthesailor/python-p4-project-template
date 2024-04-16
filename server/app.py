#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Salon

# Views go here!

class AllSalons(Resource):

    def get(self):
        response_body = [salon.to_dict(only=('id', 'appointment', 'stylist')) for salon in Salon.query.all()]
        return make_response(response_body, 200)

api.add_resource(AllSalons, '/salons')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'



if __name__ == '__main__':
    app.run(port=5555, debug=True)


