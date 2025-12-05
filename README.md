WELCOME TO gowthamreddy-homeassistant-mqtt
# Home Assistant MQTT Sensor Integration

Student: Syamala Gowtham Reddy  
Register Number: 42733117
Assignment: Nakshatra Automation - Home Assistant Technical Screening

Project Overview

This project demonstrates the integration of MQTT-based IoT sensors with Home Assistant. A Python script publishes real-time sensor data (Temperature, Humidity, and CPU Usage) to an MQTT broker, which is then displayed on a Home Assistant dashboard.

## Sensors Implemented

1. Temperature Sensor - Static value: 25°C
2. Humidity Sensor - Static value: 60%
3. CPU Usage Sensor - Real-time system CPU usage percentage (Unique sensor)

MQTT Topic:home/gowthamreddy-2025/sensor

## Technology Stack

- **Home Assistant** - Running in Docker container
- **Mosquitto MQTT Broker** - Message broker for IoT communication
- **Python 3.x** - For sensor data publishing
- **Libraries:** 
  - `paho-mqtt` - MQTT client library
  - `psutil` - System monitoring library

## Setup Instructions

#Prerequisites
- Windows 10/11 with WSL2
- Docker Desktop
- Python 3.x installed
- Mosquitto MQTT Broker

### Installation Steps
1. Install Home Assistant (Docker)
2. Install Mosquitto MQTT Broker
3. Install Python Dependencies
4. Configure Home Assistant MQTT
5. Enable MQTT Integration in Home Assistant

Run the project
1.ensure mosquitto is running
2.run the python script
3.access home assistant
4.view the overview sensores dashboard

yeah you wil notice the sensors on dashboard and outcome which refreshes for every 5 seconds 

contact:
Name: Syamala Gowtham reddy
Registor Number :42733117
topic :home/gowthamreddy-2025/sensor

#### 1. Install Home Assistant (Docker)
