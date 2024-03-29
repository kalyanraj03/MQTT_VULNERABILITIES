import paho.mqtt.client as mqtt
import time

# Broker settings
broker_address = "test.mosquitto.org"
port = 1883  # default MQTT port
username = "kalyan"
password = "kalyan"

# Callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Failed to connect, return code: {rc}")

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")

# Publisher
def publish_message():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.username_pw_set(username, password)  # Set username and password
    client.connect(broker_address, port)
    client.loop_start()

    while True:
        message = "Hello, this is a test message from the Publisher!"
        client.publish("test_topic", message)
        print(f"Published message: {message}")
        time.sleep(5)

# Subscriber
def subscribe_to_topic():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    client.username_pw_set(username, password)  # Set username and password
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port)
    client.subscribe("test_topic")
    client.loop_forever()

if __name__ == "__main__":
    # Run publisher and subscriber concurrently
    import threading
    threading.Thread(target=publish_message).start()
    threading.Thread(target=subscribe_to_topic).start()
