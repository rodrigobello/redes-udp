package app.message.strategies;

import app.strategies.Strategy;

public class CharStrategy implements Strategy {
    @Override
    public String execute(String buffer) {
        if (Character.isUpperCase(buffer.charAt(0))) {
            return buffer.toLowerCase();
        }
        return buffer.toUpperCase();
    }
}
