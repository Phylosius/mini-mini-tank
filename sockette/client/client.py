import inspect
import json
import socket
import threading
import sys
import time


class TCPClient:
    def __init__(self, name="client", host="localhost", port=7721):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = (host, port)
        self.stop_flag = threading.Event()
        self.threads = []
        self.to_send = None  # Attribut pour stocker le message à envoyer

        self.name = name
        self.receiver_function = self.handle_data # function who handle received data : f(data): None | Boolean

    def demand_disconnect(self):
        to_send = {
            "type": "disconnect",
        }
        self.send_dict(to_send)

    def send_dict(self, data):
        self.send_data(json.dumps(data, separators=(',', ':')))

    def debug(self, message):
        method_name = inspect.currentframe().f_back.f_code.co_name
        self.display(message, f"DEBUG({method_name})")

    def display(self, message, comment=""):
        print(f"[{comment}]: {message}")

    def handle_data(self, data):

        if not data:
            self.display("Connection to server closed.")
            self.stop_flag.set()
            return None

        if data["type"] == "message":
            self.display(f"{data["content"]}", data["sender"])

        return True

    def receive_data(self):
        return json.loads(self.socket.recv(4096).decode())

    def send_data(self, data):
        self.to_send = data

    def connect(self):
        """Établit la connexion avec le serveur."""
        try:
            self.socket.connect(self.server_addr)
            self.send_message(f"Hello I'm {self.name}")
            self.display(f"Connected to server at {self.server_addr}")
        except ConnectionRefusedError:
            self.display("Failed to connect to the server. Make sure the server is running.")
            sys.exit(1)

    def handle_sending(self):
        """Vérifie et envoie les messages stockés dans l'attribut `to_send`."""
        try:
            while not self.stop_flag.is_set():
                if self.to_send:
                    self.socket.sendall(self.to_send.encode())
                    self.to_send = None  # Réinitialise après envoi
                time.sleep(0.1)  # Évite une boucle trop rapide
        except Exception as e:
            self.debug(f"Error while sending message: {e}")
            self.stop_flag.set()

    def handle_receiving(self):
        """Écoute et affiche les messages reçus du serveur."""
        try:
            while not self.stop_flag.is_set():
                server_data = self.receive_data()
                if not self.receiver_function(server_data):
                     break

        except Exception as e:
            self.debug(f"Error while receiving messages: {e}")
            self.stop_flag.set()

    def send_message(self, message):
        """Attribue un message à envoyer."""
        to_send = {
            "type": "message",
            "content": message,
            "sender": self.name,
        }
        self.send_data(json.dumps(to_send, separators=(",", ":")))

    def create_thread(self, target):
        recv_thread = threading.Thread(target=target)
        self.threads.append(recv_thread)
        recv_thread.daemon = True
        recv_thread.start()

    def start_threads(self):
        # Thread pour recevoir les messages
        self.create_thread(self.handle_receiving)

        # Thread pour gérer l'envoi des messages
        self.create_thread(self.handle_sending)

    def join_threads(self):
        [t.join() for t in self.threads]

    def handle_input(self):
        message = input("> ")

        if message.lower() in {"exit", "quit"}:
            self.demand_disconnect()
            return None

        self.send_message(message)
        return True

    def run(self):
        """Démarre le client avec les threads pour l'envoi et la réception."""
        self.connect()
        try:
            self.start_threads()

            # Boucle principale pour entrer les messages
            while not self.stop_flag.is_set():
                if not self.handle_input():
                    break

            # Attendre la fin des threads
            self.join_threads()
        except KeyboardInterrupt:
            self.display("\nClient shutting down.")
        finally:
            self.close()

    def close(self):
        """Ferme la connexion au serveur."""
        self.stop_flag.set()
        self.display("Closing connection to the server...")
        self.socket.close()
        self.display("Client closed.")
        sys.exit()


if __name__ == "__main__":
    client = TCPClient()
    client.run()
