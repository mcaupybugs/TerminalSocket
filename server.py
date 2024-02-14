import re
import socket

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000

def start_application():
    try:
        host = input("Enter the host address to be exposed for connection: ")
        port = input("Enter the port to be used for the connection to be established: ")
        if not (validateHost(host) and validatePort(port)):
            host = DEFAULT_HOST
            port = DEFAULT_PORT
    
    except ValueError:
        print(f"Exception occured : {ValueError}")

# Not required but keeping to learn as when connecting to socket it will throw exception if there is issue   
def validateHost(ip_address):
    """Method to validate the ip address is a valid host or not."""

    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address)

    if not bool(match):
        print(f"IP address {ip_address} is not valid")
        return False
    
    individual_bytes = ip_address.split(".")
    
    for ip_bytes in bytes:
        if int(ip_bytes) < 0 or int(ip_bytes) > 255:
            print(f"IP address {ip_address} is not valid")
            return False

    print(f"IP address {ip_address} is valid")
    return True

def validatePort(port):
    """Method to validate if the port is a valid port that can be used."""
    if port <= 1024 and port > 65535:
        return False
    return True


# SOCK_STREAM is a type of socket.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)