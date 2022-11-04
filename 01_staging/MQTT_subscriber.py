"""
 DHBW Stuttgart | Data Warehouse | Semester 5
 ********************************************
 Autor:            Jonathan Diebel
 Erstelldatum:     04.11.2022
"""
import paho.mqtt.client as mqtt
import json
from json import JSONDecodeError

def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")

    try:
        data = json.loads(data)
            if isinstance(data, dict):
                

    except JSONDecodeError:
        print("Error while decoding JSON")
        pass
    except Exception as err:
        print(f"Unhandled error {err}")

# Connect to MQTT client and subscribe to "DataMgmt/FIN"
broker_address="broker.hivemq.com"
client = mqtt.Client("inf20026", clean_session=False) #use your own unique ID
client.on_message = on_message
client.connect(broker_address)
client.subscribe("DataMgmt/FIN", qos=1)
client.loop_forever()

