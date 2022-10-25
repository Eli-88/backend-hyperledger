package message;

import com.google.gson.Gson;

import crypto.PublicKeyFactory;

public class JsonBalanceFactory implements BalanceFactory {
    private PublicKeyFactory publicKeyFactory;

    public JsonBalanceFactory(PublicKeyFactory publicKeyFactory) {
        this.publicKeyFactory = publicKeyFactory;
    }

    @Override
    public Balance create(String rawMsg) throws Exception {
        Gson gson = new Gson();
        Balance request = gson.fromJson(rawMsg, Balance.class);

        SignatureGeneratorVisitor signatureGenerator = new SignatureGeneratorVisitor();
        if (!request.accept(signatureGenerator)) {
            throw new Exception("signature generator invalid");
        }

        var publicKey = this.publicKeyFactory.generate(request.getPublicKey());

        if (!publicKey.verify(signatureGenerator.GetPlainResult(), request.getSignature())) {
            throw new Exception("balance request signature invalid");
        }
        return request;
    }
}
