import inspect
import json
import socket
import threading
import sys

from .models.client import Client


class TCPServer:
    def __init__(self, name = "server", host="localhost", port=7721, max_clients=5):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (host, port)
        self.max_clients = max_clients
        self.threads = []  # Liste pour stocker les threads clients
        self.stop_flag = threading.Event()  # Drapeau pour arrêter les threads

        self.clients = []
        self.name = name

        self.debug_sign = "DEBUG"
        self.input_sign = "> "

        self.client_handler = self.handle_client
        self.client_data_handler = self.handle_client_data

    def debug(self, message):
        method_name = inspect.currentframe().f_back.f_code.co_name
        self.display(message, f"{self.debug_sign}({method_name})")

    def display(self, message, comment=""):
        print(f"[{comment}]: {message}")

    def init_client(self, client_socket, client_addr):
        """init client"""
        try:
            client_data = json.loads(client_socket.recv(1024).decode())
            client_name = client_data["sender"]

            client = Client(self, client_name, client_socket, client_addr)

            self.clients.append(client)

            self.display(f"New connection from {client_name} {client_addr}")

            return client

        except Exception as e:

            self.debug(f"Exception caught\n {e}")

    def handle_client_data(self, client):
        data = client.receive_data()

        if not data:
            self.display(f"Client {client.name} {client.addr} disconnected.")
            return None

        if data["type"] == "message":
            self.display(f"{data["sender"]}: {data["content"]}")

        if data["type"] == "disconnect":
            self.display(f"Client {client.name} {client.addr} demand disconnection.")
            self.clients.remove(client)

            return None

        return True

    def handle_client(self, client):

        try:
                client.send_message("You are connected to the server!\n")

                while not self.stop_flag.is_set():  # Arrête la boucle si le serveur est fermé
                    if not self.client_data_handler(client):
                        break

        except Exception as e:
            self.debug(f"Error handling client {client.name} {client.addr}: {e}")
        finally:
            client.close()

    def bind(self):
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.addr)
        self.sock.listen(self.max_clients)
        self.display(f"Server is running on {self.addr}")

    def run(self):
        self.bind()

        try:
            while not self.stop_flag.is_set():
                client_socket, client_address = self.sock.accept()

                thread = threading.Thread(target=self.client_handler, args=(self.init_client(client_socket, client_address),))
                thread.daemon = True  # Permet d'arrêter les threads lorsqu'ils ne sont plus nécessaires
                thread.start()

                self.threads.append(thread)
        except KeyboardInterrupt:
            self.display("\nServer shutting down.")
        finally:
            self.close()

    def close(self):
        self.display("Closing server...")
        self.stop_flag.set()  # Signale aux threads de s'arrêter
        self.sock.close()
        for thread in self.threads:
            thread.join()  # Attend la fin de tous les threads
        self.display("Server closed.")
        sys.exit()


if __name__ == "__main__":
    server = TCPServer()
    server.run()
