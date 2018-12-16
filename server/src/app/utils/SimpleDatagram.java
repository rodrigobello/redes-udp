package app.utils;

import app.utils.Message;

public class SimpleDatagram {
    private Message message;
    private String ipAddress;
    private int port;

    public SimpleDatagram(Message message, String ipAddress, int port) {
        this.message = message;
        this.ipAddress = ipAddress;
        this.port = port;
    }

    public Message getMessage() {
        return this.message;
    }

    public String getIpAddress() {
        return this.ipAddress;
    }

    public int getPort() {
        return this.port;
    }
}
