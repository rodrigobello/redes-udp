public class StringStrategy implements Strategy {
  @Override
  public String execute(String buffer) {
    return new StringBuffer(buffer).reverse().toString();
  }
}
