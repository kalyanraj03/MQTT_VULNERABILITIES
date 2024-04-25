import socket

def check_port(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout to 1 second
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

def main():
    hostname = 'localhost'  # Change this to your server's hostname or IP address
    ports = [1883, 8883]    # Ports commonly used for MQTT

    for port in ports:
        if check_port(hostname, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()
