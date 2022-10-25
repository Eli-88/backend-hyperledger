package message;

public class Send extends Header {
    private String fromId;
    private String toId;
    private double amount;

    public Send(int id, long timestamp, String publicKey, String fromId, String toId, double amount) {
        super(id, timestamp, publicKey);

        this.fromId = fromId;
        this.toId = toId;
        this.amount = amount;
    }

    public String getFromId() {
        return this.fromId;
    }

    public String getToId() {
        return this.toId;
    }

    public double getAmount() {
        return this.amount;
    }

    public boolean accept(Visitor visitor) {
        return visitor.visitSend(this);
    }
}
