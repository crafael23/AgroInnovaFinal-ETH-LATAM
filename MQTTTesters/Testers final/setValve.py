import datetime
import paho.mqtt.client as mqtt
import random
import time
import json

# Definir las funciones de callbacks de conexión y publicación
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: "+str(rc))

def on_publish(client, userdata, mid):
    print("Mensaje publicado")

# Crear una instancia de cliente MQTT
client = mqtt.Client()

# Asignar las funciones de callback de conexión y publicación
client.on_connect = on_connect
client.on_publish = on_publish

# Conectarse al broker de Mosquitto en localhost
client.connect("localhost", 1883, 60)




temperatura1 = random.randint(1,100)
humedad1 = random.randint(1,100)
date1 = datetime.datetime.now()
dataM1 = {
    "moduleId":2,
    "temperature": temperatura1,
    "humidity": humedad1,
    "valve": False 
}
message = json.dumps(dataM1)

client.publish("modulo/response", message, qos=1)




    
# Mantener la conexión MQTT activa
client.loop_forever()
