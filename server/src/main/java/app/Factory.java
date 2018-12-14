class Factory {
  public Message create_message_from_payload(bytes[] payload) {
    String payload = new String(payload);
    // Apply strategy depending on message type
    return Message(payload);
  }
}
