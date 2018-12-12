from app.service import UDPService
from app.exceptions import *

from datetime import datetime


class ClientController:
    def __init__(self, service=None):
        self.service = service or UDPService()

    def communicate(self, host, port, message=None):
        if not message:
            print('No message to communicate')
            return None
        try:
            self.service.create_socket()
            print('Created client socket')

            payload = message.payload()

            start = datetime.now()
            self.service.send_message(payload, host, port)
            print(f'Sent "{message}" to {host}:{port}')

            response, server = self.service.receive_response()
            rtt = datetime.now() - start

            host, port = server
            print(f'Received "{response.decode()}" from {host}:{port}')

            self.service.close_socket()
            print('Closed client socket')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        else:
            return rtt.total_seconds()
