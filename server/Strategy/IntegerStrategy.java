public class IntegerStrategy implements Strategy {
  @Override
  public String execute(String buffer) {
    int result = Integer.parseInt(buffer);
    return Integer.toString(result + 1);
  }
}
