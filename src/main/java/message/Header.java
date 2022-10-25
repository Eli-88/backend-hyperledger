package message;

public class Header {
    private int id;
    private long currTimeStamp;
    private String publicKey;
    private String signature;

    public Header(int id, long currTimeStamp, String publicKey) {
        this.id = id;
        this.currTimeStamp = currTimeStamp;
        this.publicKey = publicKey;
    }

    public int getId() {
        return this.id;
    }

    public long getTimestamp() {
        return this.currTimeStamp;
    }

    public String getPublicKey() {
        return this.publicKey;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public String getSignature() {
        return this.signature;
    }
}
