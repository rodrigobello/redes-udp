from app.service import UDPService
from app.exceptions import *


class Client:
    def __init__(self, service=None):
        self.service = service or UDPService()

    def communicate(self, message='hello world', host='localhost', port=8000):
        try:
            self.service.create_socket()
            print('Created client socket')

            self.service.send_message(message.encode(), host, port)
            print(f'Sent "{message}" to {host}:{port}')

            response, server = self.service.receive_response()
            print(f'Received "{response.decode()}" from {server[0]}:{server[1]}')

            self.service.close_socket()
            print('Closed client socket')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
