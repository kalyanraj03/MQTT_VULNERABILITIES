from scapy.all import *

def extract_mqtt_credentials(packet_data):

    username = None
    password = None

    # Find username
    try:
        username_start_idx = raw_data.index(b'\x07') + 1
        username_end_idx = raw_data.index(b'\x00', username_start_idx)

        username = raw_data[username_start_idx:username_end_idx]
    except ValueError:
        pass

    # Find password
    try:
        password_start_idx = raw_data.find(b'\x00\t') + 2
        password = raw_data[password_start_idx:]
    except ValueError:
        pass

    return username, password

# Read pcap file
pcap_file = 'test_case_1.pcapng'
packets = rdpcap(pcap_file)

# Iterate
for packet in packets:
    if packet.haslayer(TCP) and packet.haslayer(Raw):

        # Check if packet contains MQTT data
        raw_data = packet[Raw].load
        #print(raw_data)
        if b'MQTT' in raw_data:

            username, password = extract_mqtt_credentials(packet)
            if username and password:
                print("Credentials are found")
                print("Username:", username)
                print("Password:", password)
            else:
                print("Credentials are not found")
                break






