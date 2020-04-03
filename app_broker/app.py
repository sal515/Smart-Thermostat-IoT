# Import flask frame
# from flask import Flask

# Initialize Flask App
# app = Flask(__name__)


# Import flaskApi and flask libraries
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

# Import CORS for communication between decoupled server
from flask_cors import CORS

import api_broker as brokerApi


import requests as req
import threading as thread
import time as t





# Initialize FlaskApi App
app = FlaskAPI(__name__)
CORS(app)


@app.route('/')
def home():

    brokerApi.test()

    return {"Smart Thermostat": "IoT project"}


@app.route('/subscription/request', methods=['POST'])
def subscriberRegistration():
    return {"Smart Thermostat": "IoT project"}


if __name__ == '__main__':
    # app.run()
    app.run(host="localhost", port=5000, debug=True)
