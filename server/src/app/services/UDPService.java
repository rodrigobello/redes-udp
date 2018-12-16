package app.services;

import java.net.DatagramSocket;
import java.net.DatagramPacket;
import app.utils.SimpleDatagram;
import app.factories.DatagramFactory;

public class UDPService {
    private DatagramSocket serverSocket;
    private int datagramSize;
    private DatagramFactory factory;

    public UDPService(int port, int datagramSize) throws Exception {
        System.out.println(String.format("Creating socket at %d...",port));
        this.serverSocket = new DatagramSocket(port);
        this.datagramSize = datagramSize;
        this.factory = new DatagramFactory();
    }

    public SimpleDatagram receive() throws Exception {
        System.out.println("Waiting message...");
        byte[] receiveData = new byte[this.datagramSize];
        DatagramPacket packet = new DatagramPacket(receiveData, receiveData.length);
        this.serverSocket.receive(packet);
        System.out.println(String.format("[New message from %s]",packet.getAddress().toString()));
        SimpleDatagram data = this.factory.buildSimpleDatagramFromDatagramPacket(packet);
        return data;
    }

    public void send(SimpleDatagram data) throws Exception {
        System.out.println(String.format("Sending %s...", data.getMessage().toString()));
        DatagramPacket packet = this.factory.buildDatagramPacketFromSimpleDatagram(data);
        this.serverSocket.send(packet);
    }

    public void close() throws Exception {
        System.out.println("Closing socket...");
        this.serverSocket.close();
    }
}
