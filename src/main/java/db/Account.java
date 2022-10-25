package db;

public interface Account {
    public void initBalance(String accountId, Double amount, String publicKey) throws Exception;

    public void send(String fromAccountId, String toAccountId, Double amount) throws Exception;

    public byte[] getBalance(String accountId) throws Exception;
}
