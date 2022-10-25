package message;

public class SignatureGeneratorVisitor extends Visitor {
    private String result = null;

    @Override
    public boolean visitSend(Send msg) {
        result = String.format("%d%dfromId%stoId%samount%f%s", msg.getId(), msg.getTimestamp(), msg.getFromId(),
                msg.getToId(), msg.getAmount(), msg.getPublicKey());
        return true;
    }

    @Override
    public boolean visitBalance(Balance msg) {
        result = String.format("%d%daccountId%s%s", msg.getId(), msg.getTimestamp(), msg.getAccountId(),
                msg.getPublicKey());
        return true;
    }

    public String GetPlainResult() {
        return result;
    }

    public String GetSignedResult(crypto.PrivateKey privateKey) throws Exception {
        return privateKey.sign(result);
    }
}
