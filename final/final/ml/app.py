from inference import *
from flask_cors import CORS
from flask import Flask, Response, request
from pymongo import MongoClient
import threading
import requests
import schedule
import time
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)


def risk():
    risk_level, HeartRateArr, BloodOxygenLevelArr, BodyTemperatureArr = risk_level_prediction()
    if risk_level == "Risky":
        requests.get('http://localhost/api/risk-alert')
    print(risk_level)


def diwo():
    exercise_plan, diet_plan, HeartRateArr, BloodOxygenLevelArr, BodyTemperatureArr = diet_workout_prediction()
    print(diet_plan)


def update_risk_level():
    while True:
        risk()
        time.sleep(120)


def update_diet_plan():
    # schedule.every().day.at("19:05:00").do(diwo)
    while True:
        diwo()
        # schedule.run_pending()
        time.sleep(60)


thread1 = threading.Thread(target=update_risk_level)
thread1.start()

thread2 = threading.Thread(target=update_diet_plan)
thread2.start()

print("test")


@app.route('/record', methods=['POST'])
def record():
    data = request.get_json()
    temperature = data['temperature']
    # Heart Rate
    bpm = data['bpm']
    spo2 = data['spo2']
    # temperature = random.uniform(29, 38)
    # temperature = round(temperature, 2)
    bpm = random.randint(60, 100)
    spo2 = random.randint(80, 110)
    print(temperature, bpm, spo2)
    health_collection = db['health']
    health_document = {
        "HeartRate": bpm,
        "BloodOxygenLevel": spo2,
        "BodyTemperature": temperature,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    health_collection.insert_one(health_document)
    return Response(
        response=json.dumps({
            "status": "success",
            "records": "Recieved"
        }),
        status=200,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=False,
        use_reloader=True
    )
