package message;

public class Register extends Header {
    private String accountId;
    private double initialAmount;

    public Register(int id, long currTimeStamp, String publicKey, String accountId, double initialAmount) {
        super(id, currTimeStamp, publicKey);
        this.accountId = accountId;
        this.initialAmount = initialAmount;
    }

    public String getAccountId() {
        return this.accountId;
    }

    public double getInitialAmount() {
        return this.initialAmount;
    }
}
