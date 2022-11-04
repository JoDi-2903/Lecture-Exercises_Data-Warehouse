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


# Function to generate a random FIN
def random_fin_generator():
    fin_producer_list = ["DD",'WVW','WBA','WB1','1FM','ZFF','WMA','WAU','WPO','SCC','WOL','VF1',"SNT"]
    fin_start = random.choice(fin_producer_list)
    fin_end = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
    random_fin = fin_start + fin_end
    return random_fin

# Function to generate json
def generate_json():

    data = {
        "fin": FIN if use_random_FIN == False else random_fin_generator(),
        "zeit": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f"),
        "geschwindigkeit": random.randint(0, 200),
        "ort": random.randint(1, 10)
    }
    json_data = json.dumps(data)
    return json_data

# MAIN
if __name__ == "__main__":
    # Configure parameters
    broker_address="broker.hivemq.com"
    FIN = "WPOSJYDU7SDO692GB"
    use_random_FIN = False

    # Connect to MQTT client
    client = mqtt.Client("inf20026_publisher", clean_session=False) #use your own unique ID
    client.connect(broker_address)

    # Loop until Ctrl-C is pressed
    try:
        # Publish random JSON every 5 seconds
        while True:
            generated_json = generate_json()
            client.publish("DataMgmt/FIN", generated_json, qos=1)
            print(generated_json)
            time.sleep(5)
    except KeyboardInterrupt:
        pass

    # Close connection to MQTT client
    client.disconnect()
    print("Connection closed successfully.")
