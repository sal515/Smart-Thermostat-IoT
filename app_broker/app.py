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

# import threading as thread
# import time as t

import models as models

# Initialize FlaskApi App
app = FlaskAPI(__name__)
CORS(app)


@app.route('/')
def home():
    return {"MQTT Broker": "IoT project"}


@app.route('/subscription/request', methods=['POST'])
def subscriberRegistrationRequest():
    if request.is_json:
        receivedData = request.get_json()
        print(receivedData)

        deviceInfoDict = receivedData["deviceInfo"]
        deviceInfo = models.asDeviceInfo(deviceInfoDict)
        topic = receivedData["topic"]

        state, deviceInfo = brokerApi.registerSubscriber(deviceInfo=deviceInfo, topic=topic)

        print(state)
        print(deviceInfo.asDict())

        data = dict(state=state, deviceInfo=deviceInfo.asDict())
        r = req.post(url="http://localhost:2500/subscription/acknowledge", data=None, json=data)

        return {"Subscription request processing": "IoT project"}


if __name__ == '__main__':
    # app.run()
    app.run(host="localhost", port=5000, debug=True)
