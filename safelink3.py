from flask import Flask, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)
db = {}

# ONLINE FEATURE
@app.route('/generate', methods=['POST'])
def online():
    data = request.json
    code = str(random.randint(100000, 999999))
    db[code] = {"lat": data.get('lat'), "lon": data.get('lon'), "expiry": datetime.now() + timedelta(minutes=30)}
    return jsonify({"online_link": f"safelink.in/{code}"})

# OFFLINE FEATURE
@app.route('/offline_sos', methods=['POST'])
def offline():
    data = request.json
    msg = f"HELP! https://maps.google.com/?q={data.get('lat')},{data.get('lon')}"
    with open("offline_sms_log.txt", "a") as f:
        f.write(str(datetime.now()) + " : " + msg + "\n")
    return jsonify({"status": "OFFLINE SMS SENT", "msg": msg})

@app.route('/')
def home():
    return "SAFELINK Online + Offline Running"

if __name__ == '__main__':
    app.run(port=5000)