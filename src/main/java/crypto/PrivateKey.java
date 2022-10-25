package crypto;

public interface PrivateKey {
    byte[] decrypt(byte[] cipherText) throws Exception;

    String generatePublicKey() throws Exception;

    String sign(String plainText) throws Exception;
}
