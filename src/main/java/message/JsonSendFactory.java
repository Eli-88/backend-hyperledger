package message;

import com.google.gson.Gson;

import crypto.PublicKeyFactory;

public class JsonSendFactory implements SendFactory {
    private PublicKeyFactory publicKeyFactory;

    public JsonSendFactory(PublicKeyFactory publicKeyFactory) {
        this.publicKeyFactory = publicKeyFactory;
    }

    @Override
    public Send create(String rawMsg) throws Exception {
        var gson = new Gson();
        Send request = gson.fromJson(rawMsg, Send.class);

        var signatureGenerator = new SignatureGeneratorVisitor();
        if (!request.accept(signatureGenerator)) {
            throw new Exception("signature generator invalid");
        }

        var publicKey = this.publicKeyFactory.generate(request.getPublicKey());

        if (!publicKey.verify(signatureGenerator.GetPlainResult(), request.getSignature())) {
            throw new Exception("send request signature invalid");
        }

        return request;
    }
}
