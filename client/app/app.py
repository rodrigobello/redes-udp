from app.controller import ClientController
from app.factory import MessageFactory


class App:
    def __init__(self, controller=None, factory=None):
        self.controller = controller or ClientController()
        self.factory = factory or MessageFactory()

    def __get_user_input(self):
        while True:
            print('What type of message will be sent?')

            available_types = self.factory.get_available_types()

            for key, value in sorted(available_types.items(), key=lambda x: x[0]):
                print('{0}: {1}'.format(key, value))

            input_type = input('Please choose one of the types above: ')
            message_type = available_types.get(input_type)

            if message_type:
                message_value = input('Insert the {}: '.format(message_type))
                try:
                    return self.factory.create_message(message_value, message_type)
                except ValueError as e:
                    print(e)
            else:
                print('Type unavailable please try again.')

    def run(self, **kwargs):
        host = kwargs.get('host') or '127.0.0.1'
        port = kwargs.get('port') or 8000

        print('Running client on {0}:{1}'.format(host, port))

        message = self.__get_user_input()
        rtt = self.controller.communicate(
            message=message,
            host=host,
            port=port
        )
        print('RTT: {} ms'.format(rtt*1000))
