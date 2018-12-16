package app.factories;

import app.strategies.*;
import app.utils.Message;

public class MessageFactory {
    public Message buildMessageFromPayload(byte[] payload) throws IllegalArgumentException {
        String buffer = new String(payload).trim();
        String content, type;
        switch (buffer.charAt(0)) {
        case 'i':
            type = "integer";
            content = new IntegerStrategy().execute(buffer.substring(1));
            break;
        case 'c':
            type = "char";
            content = new CharStrategy().execute(buffer.substring(1));
            break;
        case 's':
            type = "string";
            content = new StringStrategy().execute(buffer.substring(1));
            break;
        default:
            throw new IllegalArgumentException("Invalid message type");
        }
        return new Message(content, type);
    }
}
