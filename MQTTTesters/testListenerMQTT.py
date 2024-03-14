import time
import paho.mqtt.client as mqtt

# MQTT broker details
broker = "localhost"
port = 1883
topic = "TestTopic2"

# Callback triggered when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    # Subscribe to the topic
    client.subscribe(topic)

# Callback triggered when a message is received
def on_message(client, userdata, msg):
    # Print the received message
    print("Received message: " + str(msg.payload.decode()))
    
    # Send a response message
    time.sleep(4)
    response = "This is a response"
    client.publish(topic + "/response", response)

# Create an MQTT client
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the MQTT client loop (blocking call)
client.loop_forever()
