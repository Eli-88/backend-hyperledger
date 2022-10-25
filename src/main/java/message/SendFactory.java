package message;

public interface SendFactory {
    Send create(String rawMsg) throws Exception;
}
