"""
 DHBW Stuttgart | Data Warehouse | Semester 5
 ********************************************
 Autor:            Jonathan Diebel
 Erstelldatum:     04.11.2022
"""

import paho.mqtt.client as mqtt
import datetime
import time
import random
import string
import json

# Connect to MQTT client
broker_address="broker.hivemq.com"
client = mqtt.Client("inf20026", clean_session=False) #use your own unique ID
client.connect(broker_address)

# Function to generate a random FIN
def random_fin_generator():
    fin_anfang_liste = ["DD",'WVW','WBA','WB1','1FM','ZFF','WMA','WAU','WPO','SCC','WOL','VF1',"SNT"]
    fin_anfang = random.choice(fin_anfang_liste)
    fin_ende = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
    random_fin = fin_anfang+fin_ende
    return random_fin

# Function to generate json
def generate_json():

    data = {
        "fin": "WPOSJYDU7SDO692GB",
        "zeit": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f"),
        "geschwindigkeit": random.randint(0, 200),
        "ort": random.randint(1, 10)
    }
    json_data = json.dumps(data)
    return json_data

# MAIN
if __name__ == "__main__":
    # Publish random JSON every 5 seconds
    while True:
        generated_json = generate_json()
        client.publish("DataMgmt/FIN", generated_json, qos=1)
        print(generated_json)
        time.sleep(5)


