# Import flask frame
# from flask import Flask

# Initialize Flask App
# app = Flask(__name__)


# Import flaskApi and flask libraries
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

# Import CORS for communication between decoupled server
from flask_cors import CORS

# import api_broker as brokerApi
import requests as req

# import threading as thread
# import time as t

import models as models

# Initialize FlaskApi App
app = FlaskAPI(__name__)
CORS(app)


@app.route('/')
def home():

    # call subscribe methods url
    deviceInfo = models.deviceInfo(0, "000.000.000.000", "http://127.0.0.1:2000/")
    topic = "data/user_preference"

    data = dict(deviceInfo=deviceInfo.asDict(), topic=topic)

    r = req.post(url="http://localhost:5000/subscription/request", data=None, json=data)

    return {"MQTT Client Applicaton (Publisher) ": "IoT project"}


@app.route('/subscription/acknowledge', methods=['POST'])
def subscriberRegistrationACK():
    if request.is_json:
        receivedData = request.get_json()
        print(receivedData)

        state = receivedData["state"]
        deviceInfoDict = receivedData["deviceInfo"]
        deviceInfo = models.asDeviceInfo(deviceInfoDict)

        print(state)
        print(deviceInfo.asDict())

        return {"Subscription acknowledgement": "IoT project"}


if __name__ == '__main__':
    # app.run()
    app.run(host="localhost", port=2500, debug=True)
