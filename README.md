# Day 5 - Arduino to Python IoT Dashboard Integration

## Objective
Connect Arduino hardware to a Python backend that reads real-time sensor data and device states, and updates a smart home style dashboard.

---

## Description
This project implements a basic IoT pipeline where an Arduino board collects sensor data and control states such as light intensity and fan speed, and transmits this data through serial communication to a Python program. The Python script acts as a bridge between hardware and software by reading incoming serial data, processing it, and serving it to a web-based dashboard. This simulates a real-world IoT system architecture where embedded devices communicate with cloud or web applications for monitoring and control.

---
## Project Structure

arduino/ → Arduino firmware (sensor data generation)
python/  → Backend server (serial communication + API)
web/     → Frontend dashboard (UI visualization)

## Hardware Requirements
- Arduino Uno / Mega
- LDR (Light Sensor)
- Potentiometer (Fan speed control simulation)
- LEDs (Light control simulation)
- Breadboard + jumper wires
- USB cable

---

## Software Requirements
- Arduino IDE
- Python 3
- Libraries:
  - pyserial
  - flask

Install:
pip install pyserial flask


---

## System Architecture
1. Arduino reads analog sensor inputs
2. Values are converted into percentage format (0–100)
3. Data is sent in structured serial format
4. Python reads serial stream continuously
5. Python parses and stores latest values
6. Flask server exposes `/data` API endpoint
7. Web dashboard fetches and displays live data

---

## Data Format (Arduino → Python)
LIGHT:70,FAN:45,AC:30


---

## Working Principle
- Arduino continuously samples analog inputs
- Data is normalized to percentage scale
- Serial communication sends structured string output
- Python listens on COM port and extracts values
- Flask provides JSON endpoint for frontend
- Dashboard updates values in real time using API calls

---

## Expected Output
- Live sensor values in browser dashboard
- Real-time updates of:
  - Light intensity
  - Fan speed
  - AC level
- Smooth UI bar visualization
- Fully working IoT data pipeline simulation

---

## Learning Outcomes
- Understanding IoT layered architecture
- Serial communication between hardware and software
- Python-based middleware design
- API-based data exposure
- Real-time web dashboard integration

---

## Notes
This is the first complete IoT pipeline project in the learning journey. It connects embedded systems, backend processing, and frontend visualization into a single working architecture. Future upgrades will include bidirectional communication and cloud-based IoT integration.
