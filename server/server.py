import re
import socket

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000

class SocketServer:
    """SocketServer class to initiate the creation of a socket server and the related options."""

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        try:
            # TODO : Make this method better
            if self.__update_connection_ports(host, port):
                self.host = host
                self.port = port
            else :
                self.host = DEFAULT_HOST
                self.port = DEFAULT_PORT

            print(f"Using HOST:PORT {host}:{port}")
            self.start_server()

        except Exception as e:
            print("Initialization failed due to exception : " ,e)

    def start_server(self):
        """Entry point of the socket server"""
        try:
            self.start_socket_server()

        except Exception as e:
            print(f"Exception occured : {e}")

    def start_socket_server(self):
        """Starting a socket server with the defined configuration"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

    def __update_connection_ports(self, host, port):
        if self.__using_default_connection_ports(host, port):
            return False
        if (self.__validateHost(host) and self.__validatePort(port)):
            return True
        return False

    def __using_default_connection_ports(self, host, port):
        if host == DEFAULT_HOST or port == DEFAULT_PORT:
            print("Using default ports")
            return True
        return False

# Not required but keeping to learn as when connecting to socket it will throw exception if there is issue   
    def __validateHost(self, ip_address):
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
    
    def __validatePort(self, port):
        """Method to validate if the port is a valid port that can be used."""
        
        if port <= 1024 and port > 65535:
            return False
        return True