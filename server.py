import paho.mqtt.client as paho
from csv import writer
import sys

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print("Connected to the broker")
    else:
        print("Connection failed")
        
def on_subscribe(client1, userdata, mid, qos):
    print("Subscribed: " +str(mid))

def on_message(client1, userdata, msg):
    print(msg.topic+" "+ str(msg.payload.decode("utf-8")))
    data = msg.payload.decode('utf-8')
    if(msg.topic=='Zenatix/GetData'):
        with open('Zenatix.csv', 'a') as f_object:   
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
        
client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqttdashboard.com")

client.loop_forever()