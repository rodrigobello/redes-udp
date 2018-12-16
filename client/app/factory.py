class MessageFactory:
    class Message:
        def __init__(self, content=None, _type=None):
            self.content = content
            self.type = _type

        def payload(self):
            return '{0}{1}'.format(str(self.type[0]), str(self.content)).encode()

        def __str__(self):
            return str(self.content)

    def __init__(self):
        self.available_types = {
            '1': 'integer',
            '2': 'character',
            '3': 'string',
        }

    def create_message(self, message_content, message_type):
        try:
            if message_type == 'integer':
                message_content = self.__map_integer(message_content)

            elif message_type == 'string':
                message_content = self.__map_string(message_content)

            elif message_type == 'character':
                message_content = self.__map_character(message_content)
            else:
                raise NotImplementedError(message_type)

        except ValueError:
            raise MessageValidationException(
                '"{0}" is not of type {1}'.format(message_content, message_type))

        return self.Message(message_content, message_type)

    def __map_integer(self, content):
        return int(content)

    def __map_string(self, content):
        return str(content)

    def __map_character(self, content):
        char = str(content)
        if len(char) != 1:
            raise ValueError()
        return char

    def get_available_types(self):
        return self.available_types


class MessageValidationException(ValueError):
    pass
