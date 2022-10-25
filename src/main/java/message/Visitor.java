package message;

public class Visitor {
    public boolean visitSend(Send msg) {
        return false;
    }

    public boolean visitBalance(Balance msg) {
        return false;
    }
}
