package crypto;

public interface PublicKeyFactory {
    PublicKey generate(String publicKeyStr) throws Exception;
}
