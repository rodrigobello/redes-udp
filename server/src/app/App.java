package app;

import app.services.UDPService;
import app.utils.SimpleDatagram;

public class App {
    public void run(int port, int datagramSize) throws Exception {
        UDPService service = new UDPService(port, datagramSize);
        try {
            while(true) {
                SimpleDatagram data = service.receive();
                service.send(data);
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        service.close();
    }
}
