import paho.mqtt.client as mqtt
import random
import json
import threading
import time

import paho.mqtt.enums as enums


# clases de modulos
class Module:
    def __init__(
        self, id: int, temperature: float, humidity: float, valve: bool, client: int
    ):
        self.id = id
        self.temperature = temperature
        self.humidity = humidity
        self.valve = valve
        self.client = client


class Pump:
    def __init__(self, value: bool):
        self.PumpState = value


PumpModule = Pump(False)
modulo1 = Module(1, 0, 0, False, 1122)
modulo11 = Module(11, 0, 0, False, 1122)
modulo111 = Module(111, 0, 0, False, 1122)
modulo1111 = Module(1111, 0, 0, False, 1122)


modulo2 = Module(2, 0, 0, False, 3344)
modulo22 = Module(22, 0, 0, False, 3344)
modulo222 = Module(222, 0, 0, False, 3344)
modulo2222 = Module(2222, 0, 0, False, 3344)


modulo3 = Module(3, 0, 0, False, 5566)
modulo33 = Module(33, 0, 0, False, 5566)
modulo333 = Module(333, 0, 0, False, 5566)
modulo3333 = Module(3333, 0, 0, False, 5566)


modulo4 = Module(4, 0, 0, False, 6677)
modulo44 = Module(44, 0, 0, False, 6677)
modulo444 = Module(444, 0, 0, False, 6677)
modulo4444 = Module(4444, 0, 0, False, 6677)


# Definir las funciones de callbacks de conexión y publicación
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: " + str(rc))


def on_publish(client, userdata, mid):
    print("Mensaje publicado")


# Crear una instancia de cliente MQTT
client = mqtt.Client(callback_api_version=enums.CallbackAPIVersion.VERSION1)


# Asignar las funciones de callback de conexión y publicación
client.on_connect = on_connect
client.on_publish = on_publish

# Conectarse al broker de Mosquitto en localhost
client.connect("localhost", 1883, 60)


# Define the callback function for the subscription
def on_message(client, userdata, message):
    # Parse the received JSON message
    try:
        if message.topic == "modulo/valve":
            json_data = json.loads(message.payload.decode())
            data = json_data["data"]
            module_id = data["moduleId"]
            valve_value = data["value"]
            print(
                f"Received message: Module ID : {module_id}, Valve Value - {valve_value}"
            )

            match module_id:
                case 1:
                    modulo1.valve = valve_value
                case 2:
                    modulo2.valve = valve_value
                case 3:
                    modulo3.valve = valve_value
                case 4:
                    modulo4.valve = valve_value

            print(f"Module {module_id} valve value updated to {valve_value}")

            print(f"Module 1 valve value: {modulo1.valve}")
            print(f"Module 2 valve value: {modulo2.valve}")
            print(f"Module 3 valve value: {modulo3.valve}")
            print(f"Module 4 valve value: {modulo4.valve}")
        elif message.topic == "pump/request":
            json_data = json.loads(message.payload.decode())
            data = json_data["data"]
            value = data["value"]
            PumpModule.PumpState = value
            print(f"Received message: Pump Value - {PumpModule.PumpState}")
            dataM = {
                "pump": PumpModule.PumpState,
            }
            mess = json.dumps(dataM)
            time.sleep(5)
            print("Sending message")
            client.publish("pump/status", mess)

    except KeyError:
        print("Received message does not contain the 'moduleId' key.")
        print(
            f"Received message on topic {message.topic} does not contain the expected keys."
        )
        print(f"Message payload: {message.payload.decode()}")


def receive_messages():
    client.subscribe("modulo/valve")
    client.subscribe("pump/request")
    client.on_message = on_message
    client.loop_forever()


def send_messages():
    while True:
        modulo1.temperature = random.randint(1, 100)
        modulo1.humidity = random.randint(1, 100)
        dataM1 = {
            "moduleId": modulo1.id,
            "temperature": modulo1.temperature,
            "humidity": modulo1.humidity,
            "valve": modulo1.valve,
            "client": modulo1.client,
        }
        message = json.dumps(dataM1)
        client.publish("modulo/status", message)

        modulo11.temperature = random.randint(1, 100)
        modulo11.humidity = random.randint(1, 100)
        dataM11 = {
            "moduleId": modulo11.id,
            "temperature": modulo11.temperature,
            "humidity": modulo11.humidity,
            "valve": modulo11.valve,
            "client": modulo11.client,
        }
        message = json.dumps(dataM11)
        client.publish("modulo/status", message)

        modulo111.temperature = random.randint(1, 100)
        modulo111.humidity = random.randint(1, 100)
        dataM111 = {
            "moduleId": modulo111.id,
            "temperature": modulo111.temperature,
            "humidity": modulo111.humidity,
            "valve": modulo111.valve,
            "client": modulo111.client,
        }
        message = json.dumps(dataM111)
        client.publish("modulo/status", message)

        modulo1111.temperature = random.randint(1, 100)
        modulo1111.humidity = random.randint(1, 100)
        dataM1111 = {
            "moduleId": modulo1111.id,
            "temperature": modulo1111.temperature,
            "humidity": modulo1111.humidity,
            "valve": modulo1111.valve,
            "client": modulo1111.client,
        }
        message = json.dumps(dataM1111)
        client.publish("modulo/status", message)

        modulo2.temperature = random.randint(1, 100)
        modulo2.humidity = random.randint(1, 100)
        dataM2 = {
            "moduleId": modulo2.id,
            "temperature": modulo2.temperature,
            "humidity": modulo2.humidity,
            "valve": modulo2.valve,
            "client": modulo2.client,
        }
        message = json.dumps(dataM2)
        client.publish("modulo/status", message)

        modulo22.temperature = random.randint(1, 100)
        modulo22.humidity = random.randint(1, 100)
        dataM22 = {
            "moduleId": modulo22.id,
            "temperature": modulo22.temperature,
            "humidity": modulo22.humidity,
            "valve": modulo22.valve,
            "client": modulo22.client,
        }
        message = json.dumps(dataM22)
        client.publish("modulo/status", message)

        modulo222.temperature = random.randint(1, 100)
        modulo222.humidity = random.randint(1, 100)
        dataM222 = {
            "moduleId": modulo222.id,
            "temperature": modulo222.temperature,
            "humidity": modulo222.humidity,
            "valve": modulo222.valve,
            "client": modulo222.client,
        }
        message = json.dumps(dataM222)
        client.publish("modulo/status", message)

        modulo2222.temperature = random.randint(1, 100)
        modulo2222.humidity = random.randint(1, 100)
        dataM2222 = {
            "moduleId": modulo2222.id,
            "temperature": modulo2222.temperature,
            "humidity": modulo2222.humidity,
            "valve": modulo2222.valve,
            "client": modulo2222.client,
        }
        message = json.dumps(dataM2222)
        client.publish("modulo/status", message)

        modulo3.temperature = random.randint(1, 100)
        modulo3.humidity = random.randint(1, 100)
        dataM3 = {
            "moduleId": modulo3.id,
            "temperature": modulo3.temperature,
            "humidity": modulo3.humidity,
            "valve": modulo3.valve,
            "client": modulo3.client,
        }
        message = json.dumps(dataM3)
        client.publish("modulo/status", message)

        modulo33.temperature = random.randint(1, 100)
        modulo33.humidity = random.randint(1, 100)
        dataM33 = {
            "moduleId": modulo33.id,
            "temperature": modulo33.temperature,
            "humidity": modulo33.humidity,
            "valve": modulo33.valve,
            "client": modulo33.client,
        }
        message = json.dumps(dataM33)
        client.publish("modulo/status", message)

        modulo333.temperature = random.randint(1, 100)
        modulo333.humidity = random.randint(1, 100)
        dataM333 = {
            "moduleId": modulo333.id,
            "temperature": modulo333.temperature,
            "humidity": modulo333.humidity,
            "valve": modulo333.valve,
            "client": modulo333.client,
        }
        message = json.dumps(dataM333)
        client.publish("modulo/status", message)

        modulo3333.temperature = random.randint(1, 100)
        modulo3333.humidity = random.randint(1, 100)
        dataM3333 = {
            "moduleId": modulo3333.id,
            "temperature": modulo3333.temperature,
            "humidity": modulo3333.humidity,
            "valve": modulo3333.valve,
            "client": modulo3333.client,
        }
        message = json.dumps(dataM3333)
        client.publish("modulo/status", message)

        modulo4.temperature = random.randint(1, 100)
        modulo4.humidity = random.randint(1, 100)
        dataM4 = {
            "moduleId": modulo4.id,
            "temperature": modulo4.temperature,
            "humidity": modulo4.humidity,
            "valve": modulo4.valve,
            "client": modulo4.client,
        }
        message = json.dumps(dataM4)
        client.publish("modulo/status", message)

        modulo44.temperature = random.randint(1, 100)
        modulo44.humidity = random.randint(1, 100)
        dataM44 = {
            "moduleId": modulo44.id,
            "temperature": modulo44.temperature,
            "humidity": modulo44.humidity,
            "valve": modulo44.valve,
            "client": modulo44.client,
        }
        message = json.dumps(dataM44)
        client.publish("modulo/status", message)

        modulo444.temperature = random.randint(1, 100)
        modulo444.humidity = random.randint(1, 100)
        dataM444 = {
            "moduleId": modulo444.id,
            "temperature": modulo444.temperature,
            "humidity": modulo444.humidity,
            "valve": modulo444.valve,
            "client": modulo444.client,
        }
        message = json.dumps(dataM444)
        client.publish("modulo/status", message)

        modulo4444.temperature = random.randint(1, 100)
        modulo4444.humidity = random.randint(1, 100)
        dataM4444 = {
            "moduleId": modulo4444.id,
            "temperature": modulo4444.temperature,
            "humidity": modulo4444.humidity,
            "valve": modulo4444.valve,
            "client": modulo4444.client,
        }
        message = json.dumps(dataM4444)
        client.publish("modulo/status", message)

        time.sleep(4)


send_thread = threading.Thread(target=send_messages)

receive_thread = threading.Thread(target=receive_messages)


send_thread.start()
receive_thread.start()
