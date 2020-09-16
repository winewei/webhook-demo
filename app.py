#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, reqparse,request
import logging

app = Flask(__name__)
api = Api(app)

parse = reqparse.RequestParser()
class Webhook(Resource):
    def get(self):
        return {"msg": "hi"}, 200
    def post(self):
        args = request.get_json(force=True)
        logging.info(args)

        return {"msg": "success"}, 200

api.add_resource(Webhook, '/api/v1/webhook')

if __name__ == '__main__':
    app.run(debug=False, port=5000)
