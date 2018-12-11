class MessageFactory:
    def __init__(self):
        self.available_types = {
            '1': 'integer',
            '2': 'character',
            '3': 'string',
        }

    def create_message(self, message_value, message_type):
        try:
            if message_type == 'integer':
                message_value = self.__map_integer(message_value)

            elif message_type == 'string':
                message_value = self.__map_string(message_value)

            elif message_type == 'character':
                message_value = self.__map_character(message_value)
            else:
                raise NotImplementedError(message_type)

        except ValueError:
            raise MessageValidationException(
                f'"{message_value}" is not of type {message_type}')

        return self.Message(message_value, message_type)

    def __map_integer(self, value):
        return str(int(value))

    def __map_string(self, value):
        return str(value)

    def __map_character(self, value):
        char = str(value)
        if len(char) != 1:
            raise ValueError()
        return char

    def get_available_types(self):
        return self.available_types

    class Message:
        def __init__(self, value=None, _type=None):
            self.value = value
            self.type = _type

class MessageValidationException(ValueError):
    pass
