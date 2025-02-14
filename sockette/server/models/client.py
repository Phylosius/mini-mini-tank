import json


class Client:
    def __init__(self, server, name, client_socket, client_addr):

        self.socket = client_socket
        self.addr = client_addr

        self.name = name
        self.server = server

    def close(self):
        self.socket.close()

    def send_data(self, data):
        self.socket.send(data.encode())

    def send_dict(self, data):
        self.send_data(json.dumps(data, separators=(',', ':')))

    def send_message(self, message):
        to_send = {
                "type": "message",
                "content": message,
                "sender": self.server.name,
            }
        self.send_dict(to_send)

    def receive_data(self):
        return json.loads(self.socket.recv(4096).decode())
