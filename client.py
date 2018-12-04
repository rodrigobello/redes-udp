import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'50'

try:
    # Send data
    print(f'sending "{message}"')
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print(f'received "{data.decode()}"')

finally:
    print('closing socket')
    sock.close()
