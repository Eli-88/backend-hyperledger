package message;

public class Balance extends Header {
    private String accountId;

    public Balance(int id, long currTimeStamp, String publicKey, String accountId) {
        super(id, currTimeStamp, publicKey);
        this.accountId = accountId;
    }

    public String getAccountId() {
        return this.accountId;
    }

    public boolean accept(Visitor visitor) {
        return visitor.visitBalance(this);
    }
}
