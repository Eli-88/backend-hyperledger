package handler;

import io.javalin.http.Context;
import io.javalin.http.Handler;

public class Send implements Handler {
    private message.SendFactory messageFactory;
    private db.Account account;

    public Send(message.SendFactory messageFactory, db.Account account) {
        this.messageFactory = messageFactory;
        this.account = account;
    }

    @Override
    public void handle(Context ctx) throws Exception {
        try {
            System.out.println("Body: " + ctx.body());
            message.Send msg = messageFactory.create(ctx.body());
            this.account.send(msg.getFromId(), msg.getToId(), msg.getAmount());
            ctx.result(Integer.toString(msg.getId()));
        } catch (Exception ex) {
            System.out.println("Exception: " + ex.getMessage());
            ctx.result("Error: " + ex.getMessage());
        }
    }
}
