import paho.mqtt.client as paho
from time import sleep
import threading
import datetime
import csv
import sys


def on_connect(client, userdata, flags, rc):
    reconnectFlag = 0

    dataList = []
    with open('C:\\Users\\Raunak\\Downloads\\dataset.csv', 'r') as file:
        reader = csv.reader(file)        
        for row in reader:
            if(rc == 0):
                print("Connected with result code "+str(rc))
                # sleep(1)
                client.publish("Zenatix/GetData", str(row))
                
                if((reconnectFlag == 1) & len(row)>0):
                    client.publish("Zenatix/GetData", str(row))



    if rc != 0:
        print ("Unexpected MQTT disconnection. Will auto-reconnect")
        dataList.append(row)
        sleep(5/12)
        reconnectFlag = 1

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqttdashboard.com")

client.loop_forever()
