package app;

import app.strategies.*;
import app.utils.message;

class MessageFactory {
    public Message createMessageFromPayload(bytes[] payload) {
        String buffer = new String(payload);
        String content, type;
        switch (payload.charAt(0)) {
        case 'i':
            type = "Integer";
            content = new IntegerStrategy().execute(buffer);
            break;
        case 'c':
            type = "Character";
            content = new CharStrategy().execute(buffer);
            break;
        case 's':
            type = "String";
            content = new StringStrategy().execute(buffer);
            break;
        default:
            throw new IllegalArgumentException("Invalid message type");
            break;
        }
        return Message(content, type);
    }
}
