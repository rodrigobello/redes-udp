package app.strategies;

import app.strategies.Strategy;

public class IntegerStrategy implements Strategy {
    @Override
    public String execute(String buffer) {
        System.out.println(String.format("Received integer '%s'!", buffer));
        int result = Integer.parseInt(buffer);
        return Integer.toString(result + 1);
    }
}
