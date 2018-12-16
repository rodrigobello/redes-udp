package app.strategies;

import app.strategies.Strategy;

public class CharStrategy implements Strategy {
    @Override
    public String execute(String buffer) {
        System.out.println(String.format("Received char '%s'!", buffer));
        if (Character.isUpperCase(buffer.charAt(0))) {
            return buffer.toLowerCase();
        }
        return buffer.toUpperCase();
    }
}
