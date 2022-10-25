
import config.ConfigFactory;
import crypto.RsaPublicKeyFactory;
import io.javalin.Javalin;
import message.JsonBalanceFactory;
import message.JsonRegisterFactory;
import message.JsonSendFactory;

class Server {

    public static void main(String[] args) throws Exception {
        var config = (new ConfigFactory()).create();
        var app = Javalin.create();

        var account = new db.HyperLedgerAccount()
                .setPemFile(config.getPemFilePath())
                .setConnPath(config.getConnConfigPath())
                .setUserId(config.getUserId())
                .build();

        var sendHandler = new handler.Send(new JsonSendFactory(new RsaPublicKeyFactory()), account);
        app.post("/send", sendHandler);

        var balanceHandler = new handler.Balance(new JsonBalanceFactory(new RsaPublicKeyFactory()), account);
        app.post("/get-balance", balanceHandler);

        var registerHandler = new handler.Register(new JsonRegisterFactory(), account);
        app.post("/register", registerHandler);

        app.start(7070);
    }
}