from app.service import UDPService
from app.exceptions import *


class ClientController:
    def __init__(self, service=None):
        self.service = service or UDPService()

    def communicate(self, message='hello world', host='localhost', port=8000):
        try:
            self.service.create_socket()
            print('Created client socket')

            self.service.send_message(message.encode(), host, port)
            print(f'Sent "{message}" to {host}:{port}')

            response, server = self.service.receive_response()
            host, port = server
            print(f'Received "{response.decode()}" from {host}:{port}')

            self.service.close_socket()
            print('Closed client socket')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
