class CreateSocketException(Exception):
    def __init__(self, msg):
        super().__init__('[Fail to create socket] {}'.format(msg))


class SendMessageException(Exception):
    def __init__(self, msg):
        super().__init__('[Fail to send message] {}'.format(msg))


class ReceiveResponseException(Exception):
    def __init__(self, msg):
        super().__init__('[Fail to receive response] {}'.format(msg))


class CloseSocketException(Exception):
    def __init__(self, msg):
        super().__init__('[Fail to close socket] {}'.format(msg))
