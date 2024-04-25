import paho.mqtt.client as mqtt
import time

# MQTT Broker settings
broker_address = "test.mosquitto.org"
broker_port = 1883

# Credentials for Client 1
client1_username = "client2"

client1_password = "password1"

# Credentials for Client 2
client2_username = "client2"
client2_password = "password2"

# Topic for communication
communication_topic = "communication_topic"

# Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(communication_topic)

def on_message(client, userdata, message):
    print("Received message on topic: " + message.topic)
    print("Message payload: " + str(message.payload.decode()))

# Create MQTT client instances
client1 = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client2 = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Set callback functions
client1.on_connect = on_connect
client1.on_message = on_message
client2.on_connect = on_connect
client2.on_message = on_message

# Connect to broker
client1.username_pw_set(client1_username, client1_password)
client1.connect(broker_address, broker_port, 60)

client2.username_pw_set(client2_username, client2_password)
client2.connect(broker_address, broker_port, 60)

# Loop to maintain connection and process messages
client1.loop_start()
client2.loop_start()

# Wait for connections to establish
time.sleep(2)

# Publish message from client 1 to client 2
client1.publish(communication_topic, "Message from client 1 to client 2")

# Wait for the message to be received
time.sleep(2)

# Publish message from client 2 to client 1
client2.publish(communication_topic, "Message from client 2 to client 1")

# Wait for the message to be received
time.sleep(2)

# Disconnect clients
client1.loop_stop()
client2.loop_stop()
client1.disconnect()
client2.disconnect()
