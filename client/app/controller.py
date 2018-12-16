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
            print('Sent "{0}" to {1}:{2}'.format(message, host, port))

            response, server = self.service.receive_response()
            rtt = datetime.now() - start

            host, port = server
            print('Received "{0}" from {1}:{2}'.format(response.decode(), host, port))

            self.service.close_socket()
            print('Closed client socket')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        finally:
            return rtt.total_seconds() * 1000 if rtt else 0
