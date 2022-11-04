"""
 DHBW Stuttgart | Data Warehouse | Semester 5
 ********************************************
 Autor:            Jonathan Diebel
 Erstelldatum:     04.11.2022
"""

import paho.mqtt.client as mqtt
import psycopg2
import json
from json import JSONDecodeError


# Connect to postgres database
postgres = psycopg2.connect("dbname='staging' user='postgres' password='123456' host='localhost' port='5432'")
postgres.autocommit = True
cursor = postgres.cursor()

# Receive message and process it
def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")

    try:
        data = json.loads(data)
        if isinstance(data, dict):
                if data["fin"] == FIN or read_all_messages == True:
                    print(f"Received Message: {data}")
                    if write_message_to_postgres == True:
                        write_message_to_postgres(data)
    except JSONDecodeError:
        print("Error while decoding JSON")
        pass
    except Exception as err:
        print(f"Unhandled error {err}")

# Write message to postgres database
def write_message_to_postgres(data):
    cursor.execute(f"INSERT INTO staging.kfzzuordnung (payload, erstellt_am, quelle) VALUES ('{str(data)}', '{data['zeit']}', 'MQTT');")


# MAIN
if __name__ == '__main__':
    # Configure parameters
    broker_address="broker.hivemq.com"
    FIN = "WPOSJYDU7SDO692GB"
    read_all_messages = True
    write_messages_to_postgres = True

    # Connect to MQTT client and subscribe to "DataMgmt/FIN"
    client = mqtt.Client("inf20026_subscriber", clean_session=False) #use your own unique ID
    client.on_message = on_message
    client.connect(broker_address)
    client.subscribe("DataMgmt/FIN", qos=1)

    # Loop until Ctrl-C is pressed
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        pass

    # Close connections to MQTT client and postgres
    client.disconnect()
    #cursor.close()
    #postgres.close()
    print("All connections closed successfully.")
