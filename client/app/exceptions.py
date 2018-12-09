class CreateSocketException(Exception):
    def __init__(self, msg):
        super().__init__(f'[Fail to create socket] {msg}')


class SendMessageException(Exception):
    def __init__(self, msg):
        super().__init__(f'[Fail to send message] {msg}')


class ReceiveResponseException(Exception):
    def __init__(self, msg):
        super().__init__(f'[Fail to receive response] {msg}')


class CloseSocketException(Exception):
    def __init__(self, msg):
        super().__init__(f'[Fail to close socket] {msg}')
