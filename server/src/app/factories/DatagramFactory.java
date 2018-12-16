package app.factories;

import java.net.DatagramPacket;
import java.net.InetAddress;
import app.utils.SimpleDatagram;
import app.factories.MessageFactory;

public class DatagramFactory {
    private MessageFactory factory;

    public DatagramFactory() {
        this.factory = new MessageFactory();
    }

    public SimpleDatagram buildSimpleDatagramFromDatagramPacket(DatagramPacket payload) throws IllegalArgumentException {
        return new SimpleDatagram(
            this.factory.buildMessageFromPayload(payload.getData()),
            payload.getAddress().getHostAddress(),
            payload.getPort()
        );
    }

    public DatagramPacket buildDatagramPacketFromSimpleDatagram(SimpleDatagram payload) throws Exception {
        byte[] data = payload.getMessage().encode();
        InetAddress ip = InetAddress.getByName(payload.getIpAddress());
        int port = payload.getPort();
        return new DatagramPacket(
            data,
            data.length,
            ip,
            port
        );
    }
}
