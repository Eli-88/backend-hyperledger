package crypto;

public class RsaPublicKeyFactory implements PublicKeyFactory {
    @Override
    public PublicKey generate(String publicKeyStr) throws Exception {
        return RsaPublicKey.newPublicKey(publicKeyStr);
    }
}
