package message;

public interface RegisterFactory {
    Register create(String rawMsg) throws Exception;
}
