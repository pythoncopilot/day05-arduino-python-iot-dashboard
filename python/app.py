import serial
import time

# CHANGE THIS depending on your system:
# Windows: COM3 / COM4
# Mac/Linux: /dev/ttyUSB0 or /dev/ttyACM0
arduino = serial.Serial('COM3', 9600, timeout=1)

time.sleep(2)  # wait for connection

print("Python IoT Bridge Started...\n")

while True:
    try:
        line = arduino.readline().decode().strip()

        if line:
            print("Raw Data:", line)

            # Expected format:
            # LIGHT:70,FAN:45,AC:30
            parts = line.split(",")

            light = parts[0].split(":")[1]
            fan   = parts[1].split(":")[1]
            ac    = parts[2].split(":")[1]

            print("LIGHT:", light)
            print("FAN:", fan)
            print("AC:", ac)
            print("----------------------")

    except Exception as e:
        print("Error:", e)
