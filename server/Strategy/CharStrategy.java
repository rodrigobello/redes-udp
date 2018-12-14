public class CharStrategy implements Strategy {
  @Override
  public String execute(String buffer) {
    if (Character.isUpperCase(buffer.charAt(0))) {
      return buffer.toLowerCase();
    }
    return buffer.toUpperCase();
  }
}
