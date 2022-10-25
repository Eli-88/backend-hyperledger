package handler;

import io.javalin.http.Context;
import io.javalin.http.Handler;

public class Register implements Handler {
    private message.RegisterFactory messageFactory;
    private db.Account account;

    public Register(message.RegisterFactory messageFactory, db.Account account) {
        this.messageFactory = messageFactory;
        this.account = account;
    }

    @Override
    public void handle(Context ctx) throws Exception {
        try {
            var registerMsg = messageFactory.create(ctx.body());
            this.account.initBalance(registerMsg.getAccountId(), registerMsg.getInitialAmount(),
                    registerMsg.getPublicKey());
            ctx.result(Integer.toString(registerMsg.getId()));
        } catch (Exception ex) {
            ctx.result("error: " + ex.getMessage());
        }
    }
}
