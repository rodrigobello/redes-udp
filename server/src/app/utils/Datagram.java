package utils.udp;

class Datagram {
    private byte[] buffer;
    private String ipAddress;
    private int port;

    public Datagram(byte[] buffer, String ipAddress, int port) {
        this.buffer = buffer;
        this.ipAddress = ipAddress;
        this.port = port;
    }

    public getBuffer() {
        return this.buffer;
    }

    public getIpAddress() {
        return this.ipAddress;
    }

    public getPort() {
        return this.port;
    }
}
