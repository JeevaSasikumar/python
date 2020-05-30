import paho.mqtt.client as mqtt

#Callbacks
def on_connect(client,userdata,flags,rc):
    print("connected with code - "+str(rc))
    #subscribe
    client.subscribe("dotworld/beacons")

def on_message(client,userdata,msg):
    print(str(msg.payload))
    f=open("suscribed","a+")
    f.write(str(msg.payload)+"\n")
    f.close()

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.username_pw_set("jeeva","jeevasasi")
client.connect("broker.hivemq.com",1883,60)

client.loop_forever()
