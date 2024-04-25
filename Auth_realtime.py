import pyshark
from scapy.all import *

# Set up the packet capture
capture = pyshark.LiveCapture(interface='Wi-Fi')

# Start capturing packets
for packet in capture.sniff_continuously(packet_count=100):  # Adjust packet_count as needed
    # Analyze each packet
    if 'MQTT' in packet:
        raw_data = (packet['MQTT'])
        print(raw_data)

        if hasattr(packet, 'ip'):
            encrypted = int(packet.ip.ttl) < 32  # TTL < 32 typically indicates encrypted traffic
        else:
            encrypted = False
        try:
            username = raw_data.username
            password = raw_data.passwd
        except AttributeError:
            username = None
            password = None

        if username and password:
            print(username, password, encrypted)
            break
        else:
            print("There is No username or password for the user")
            print(encrypted)





