package app.services;

import java.net.DatagramSocket;
import java.net.DatagramPacket;
import utils.Datagram;

class UDPService {
    private DatagramSocket serverSocket;
    private byte[] datagramSize;

    public UDPService(int port, int datagramSize) {
        this.serverSocket = new DatagramSocket(port);
        this.datagramSize = datagramSize;
    }

    public Datagram receiveMessage() {
        byte[] receiveData = new byte[this.datagramSize];
        DatagramPacket receivePacket = new DatagramPacket(this.receiveData, this.receiveData.length);
        this.serverSocket.receive(receivePacket);

        // Map DatagramPacket to Datagram
        return th();
    }

    public void sendMessage(Datagram data) {

        // Map Datagram to DatagramPacket
        DatagramPacket sendPacket = new DatagramPacket(
            data.getMessage(),
            data.getDataLength(),
            data.getIpAddress(),
            data.getPort()
        );
        this.serverSocket.send(sendPacket);
    }
}
