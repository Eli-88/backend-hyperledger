package message;

public interface BalanceFactory {
    Balance create(String rawMsg) throws Exception;
}
