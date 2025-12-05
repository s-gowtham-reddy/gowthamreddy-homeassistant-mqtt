import paho.mqtt.client as mqtt
import time
import psutil


student_name = "Syamala Gowtham Reddy"  
unique_id = "42733117"  
topic = "home/gowthamreddy-2025/sensor" 


broker = "localhost"
port = 1883

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected to MQTT Broker! (Student: {student_name})")
    else:
        print(f" Failed to connect, return code {rc}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, f"python-mqtt-{unique_id}")
client.on_connect = on_connect
client.connect(broker, port)

print(f"\n🚀 Starting MQTT Publisher for {student_name}")
print(f"📡 Publishing to topic: {topic}")
print("-" * 50)


try:
    while True:
        
        temperature = 25
        humidity = 60
        
        
        cpu_usage = round(psutil.cpu_percent(interval=1), 1)
        
        
        client.publish(f"{topic}/temperature", temperature)
        client.publish(f"{topic}/humidity", humidity)
        client.publish(f"{topic}/cpu_usage", cpu_usage)
        
        
        print(f"📊 Published - Temp: {temperature}°C | Humidity: {humidity}% | CPU Usage: {cpu_usage}%")
        
        time.sleep(5)  
        
except KeyboardInterrupt:
    print("\n⚠️  Stopped by user")
    client.disconnect()
