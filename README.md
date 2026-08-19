# Smart Helmet: AIoT-Based Accident Detection and Emergency Alert System

## README

### Overview

The Smart Helmet is an Artificial Intelligence and Internet of Things (AIoT) project designed to improve road safety by automatically detecting accidents and sending emergency alerts to predefined contacts.

The system combines an ESP32 microcontroller, an MPU6050 motion sensor, a NEO-6M GPS module, a buzzer, a push button, and the Twilio API to create a real-time emergency response system.

When an accident is detected, the helmet immediately activates a buzzer to alert the rider. A 15-second delay allows the rider to cancel the alert by pressing a button. If the rider does not respond, the system automatically sends an emergency SMS containing the rider's location to multiple emergency contacts.

This project demonstrates the integration of Artificial Intelligence, IoT, wireless communication, sensor technology, GPS tracking, and cloud-based messaging.

---

## Features

* Real-time accident detection
* Automatic emergency SMS alerts
* GPS-based location sharing
* Buzzer-based local alert system
* Push-button cancellation
* Multiple emergency contacts
* Twilio cloud integration
* ESP32-based wireless communication
* Expandable AI-based architecture
* Bluetooth compatibility for future development

---

## Hardware Components

| Component     | Purpose                     |
| ------------- | --------------------------- |
| ESP32         | Main controller             |
| MPU6050       | Motion and impact detection |
| NEO-6M GPS    | Location tracking           |
| Active Buzzer | Audible emergency alert     |
| Push Button   | Alert cancellation          |
| Breadboard    | Circuit development         |
| Jumper Wires  | Hardware connections        |
| USB Cable     | Programming and power       |

---

## Software Requirements

### Arduino IDE

Required libraries:

* TinyGPSPlus
* Wire
* HardwareSerial

---

### Python

Required packages:

```bash
pip install twilio
pip install pyserial
```

---

## System Architecture

```text
MPU6050
     ↓
ESP32
     ↓
Accident Detection
     ↓
15-Second Waiting Period
     ↓
Button Pressed?
     ↓
   Yes → Cancel Alert
     ↓
   No
     ↓
Buzzer Activated
     ↓
GPS Location Retrieved
     ↓
Python Application
     ↓
Twilio API
     ↓
Emergency SMS Sent
```

---

## Circuit Connections

### MPU6050

| MPU6050 | ESP32  |
| ------- | ------ |
| VCC     | 3.3V   |
| GND     | GND    |
| SDA     | GPIO21 |
| SCL     | GPIO22 |

---

### NEO-6M GPS

| GPS | ESP32  |
| --- | ------ |
| VCC | VIN/5V |
| GND | GND    |
| TX  | GPIO16 |
| RX  | GPIO17 |

---

### Buzzer

| Buzzer   | ESP32  |
| -------- | ------ |
| Positive | GPIO25 |
| Negative | GND    |

---

### Push Button

| Push Button | ESP32  |
| ----------- | ------ |
| Terminal 1  | GPIO26 |
| Terminal 2  | GND    |

---

## Working Principle

### Step 1: Sensor Monitoring

The MPU6050 continuously measures acceleration values along the X, Y, and Z axes.

---

### Step 2: Accident Detection

The ESP32 calculates the total acceleration.

If the acceleration exceeds the predefined threshold, the system identifies it as a possible accident.

---

### Step 3: Local Alert

The buzzer immediately starts beeping to alert the rider.

---

### Step 4: Cancellation Period

The rider has 15 seconds to press the push button and cancel the alert.

---

### Step 5: Emergency Notification

If the rider does not cancel the alert, the ESP32 sends accident information to the Python application through serial communication.

---

### Step 6: SMS Transmission

The Python application uses the Twilio API to send an emergency message containing the rider's location.

---

## Future Enhancements

* Machine Learning-based accident prediction
* Bluetooth-based smartphone communication
* Mobile application development
* Cloud database integration
* Real-time dashboard
* Voice assistance
* Helmet battery monitoring
* Accident history analysis
* AI-powered false alarm reduction

---

## Applications

* Motorcycle safety
* Rider assistance systems
* Emergency response systems
* Smart transportation
* AIoT research
* Road safety monitoring

---

## Technologies Used

* C++
* Python
* Arduino IDE
* ESP32
* Twilio API
* GPS
* IoT
* AIoT
* Embedded Systems

---

## Conclusion

The Smart Helmet demonstrates how IoT, wireless communication, and cloud services can be integrated to improve road safety. The system automatically detects accidents, alerts emergency contacts, and shares location information in real time. Future integration of machine learning and Bluetooth communication can transform the prototype into a fully intelligent AIoT-based safety solution.

---

## Authors

**Amrita Rajesh**

B.Tech IoT

SRM Institute of Science and Technology

---

## License

This project is intended for educational and research purposes.
