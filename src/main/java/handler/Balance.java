package handler;

import io.javalin.http.Context;
import io.javalin.http.Handler;
import message.BalanceFactory;

public class Balance implements Handler {
    private BalanceFactory balanceFactory;
    private db.Account account;

    public Balance(BalanceFactory balanceFactory, db.Account account) {
        this.balanceFactory = balanceFactory;
        this.account = account;
    }

    @Override
    public void handle(Context ctx) throws Exception {
        try {
            message.Balance msg = balanceFactory.create(ctx.body());
            byte[] amt = account.getBalance(msg.getAccountId());
            ctx.result(amt);
        } catch (Exception ex) {
            System.out.println("exception: " + ex.getMessage());
            ctx.result("error");
        }
    }
}
