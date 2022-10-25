package crypto;

public interface PublicKey {
    byte[] encrypt(byte[] plainText) throws Exception;

    boolean verify(String plainText, String signature) throws Exception;
}
