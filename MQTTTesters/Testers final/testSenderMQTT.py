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



while True:
    
    # #Agua
    # ph= random.randint(1,100)
    # nivel= random.choice([True, False])
    # tiempoA = datetime.datetime.now()
    # dataA = {
    #     "ph": ph,
    #     "nivel": nivel,
    # }
    # messageA = json.dumps(dataA)
    # client.publish("Reserva_Agua", messageA)
    
    #Agua
            
    
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    date1 = datetime.datetime.now()
    dataM1 = {
        "moduleId":1,
        "temperature": temperatura1,
        "humidity": humedad1,
        "valve": random.choice([True, False])
    }
    message = json.dumps(dataM1)
    client.publish("modulo/status", message)
    
    
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    date1 = datetime.datetime.now()
    dataM1 = {
        "moduleId":2,
        "temperature": temperatura1,
        "humidity": humedad1,
        "valve": random.choice([True, False])
    }
    message = json.dumps(dataM1)
    client.publish("modulo/status", message)
    
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    date1 = datetime.datetime.now()
    dataM1 = {
        "moduleId":3,
        "temperature": temperatura1,
        "humidity": humedad1,
        "valve": random.choice([True, False])
    }
    message = json.dumps(dataM1)
    client.publish("modulo/status", message)
    
    
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    date1 = datetime.datetime.now()
    dataM1 = {
        "moduleId":4,
        "temperature": temperatura1,
        "humidity": humedad1,
        "valve": random.choice([True, False])
    }
    message = json.dumps(dataM1)
    client.publish("modulo/status", message)

    time.sleep(5)