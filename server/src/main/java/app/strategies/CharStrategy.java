package app.strategies;

import utils.Strategy;

public class CharStrategy implements Strategy {
  @Override
  public String execudte(String buffer) {
    if (Character.isUpperCase(buffer.charAt(0))) {
      return buffer.toLowerCase();
    }
    return buffer.toUpperCase();
  }
}
