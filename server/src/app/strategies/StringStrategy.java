package app.strategies;

import app.strategies.Strategy;

public class StringStrategy implements Strategy {
    @Override
    public String execute(String buffer) {
        System.out.println(String.format("Received string '%s'!", buffer));
        return new StringBuffer(buffer).reverse().toString();
    }
}
