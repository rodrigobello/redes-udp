import app.App;

public class Server {
    public static void main(String[] args) throws Exception {

        int port = args.length > 0 ? Integer.parseInt(args[0]) : 8000;

        int datagramSize = args.length > 1 ? Integer.parseInt(args[1]) : 1024;

        App app = new App();
        app.run(port, datagramSize);
    }
}
