from app.service import UDPService
from app.exceptions import *


class ClientController:
    def __init__(self, service=None):
        self.service = service or UDPService()

    def communicate(self, host, port, message='hello world'):
        try:
            self.service.create_socket()
            print('Created client socket')

            self.service.send_message(message.encode(), host, port)
            print(f'Sent "{message}" to {host}:{port}')

            response, server = self.service.receive_response()
            host, port = server
            response = response.decode()
            print(f'Received "{response}" from {host}:{port}')

            self.service.close_socket()
            print('Closed client socket')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
