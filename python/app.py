from flask import Flask, jsonify
import serial
import threading
import time

app = Flask(__name__)

# CHANGE PORT IF NEEDED
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

# shared data storage
data = {
    "light": 0,
    "fan": 0,
    "ac": 0
}

def read_serial():
    global data

    while True:
        try:
            line = arduino.readline().decode().strip()

            if line and "LIGHT" in line:
                parts = line.split(",")

                data["light"] = int(parts[0].split(":")[1])
                data["fan"]   = int(parts[1].split(":")[1])
                data["ac"]    = int(parts[2].split(":")[1])

        except:
            pass

threading.Thread(target=read_serial, daemon=True).start()

@app.route("/data")
def get_data():
    return jsonify(data)

@app.route("/")
def home():
    return "IoT Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
