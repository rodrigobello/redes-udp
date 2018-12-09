import socket as SocketService
from app.exceptions import *


class UDPService:
    def __init__(self, socket_service=None):
        self.socket_service = socket_service or SocketService

    def create_socket(self):
        try:
            self.socket = self.socket_service.socket(
                self.socket_service.AF_INET,
                self.socket_service.SOCK_DGRAM
            )
        except Exception as e:
            raise CreateSocketException(e)

    def send_message(self, message, host, port):
        try:
            self.socket.sendto(message, (host, port))
        except Exception as e:
            raise SendMessageException(e)

    def receive_response(self):
        try:
            return self.socket.recvfrom(4096)
        except Exception as e:
            raise ReceiveResponseException(e)

    def close_socket(self):
        try:
            self.socket.close()
        except Exception as e:
            raise CloseSocketException(e)
