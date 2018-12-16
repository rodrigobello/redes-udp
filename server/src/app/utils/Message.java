package app.utils;

public class Message {
    private String content;
    private String type;

    public Message(String value, String type) {
        this.content = value;
        this.type = type;
    }

    public byte[] encode() {
        return this.content.getBytes();
    }

    public String toString() {
        return String.format("%s '%s'", this.type, this.content);
    }
}
