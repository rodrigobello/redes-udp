package app;

class UDPService {
  private DatagramSocket serverSocket;
  private byte[] receiveData;

  public UDPService(int port, int datagramSize) {
    this.serverSocket = new DatagramSocket(port);
    this.data = new byte[datagramSize];
  }

  public DatagramPacket receivePacket() {
    DatagramPacket receivePacket = new DatagramPacket(this.receiveData, this.receiveData.length);
    this.serverSocket.receive(receivePacket);
    return receivePacket;
  }

  public DatagramPacket sendPacket(byte[] data, InetAddress ipAddress, int port) {
    DatagramPacket sendPacket = new DatagramPacket(data, data.length, IPAddress, port);
    this.serverSocket.send(sendPacket);
    return sendPacket;
  }

}
