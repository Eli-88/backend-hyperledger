package crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyPairGenerator;
import java.security.Signature;
import java.util.Base64;

import javax.crypto.Cipher;

public class RsaPrivateKey implements PrivateKey {

    public static RsaPrivateKey NewPrivateKey(int keySize) throws Exception {
        var generator = KeyPairGenerator.getInstance("RSA");
        generator.initialize(keySize);
        var pair = generator.genKeyPair();
        return new RsaPrivateKey(pair.getPrivate(), pair.getPublic());
    }

    private RsaPrivateKey(java.security.PrivateKey privateKey, java.security.PublicKey publicKey) {
        this.privateKey = privateKey;
        this.publicKey = publicKey;
    }

    @Override
    public byte[] decrypt(byte[] cipherText) throws Exception {
        var decodedCipherText = Base64.getDecoder().decode(cipherText);
        var cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, this.privateKey);
        return cipher.doFinal(decodedCipherText);
    }

    @Override
    public String generatePublicKey() throws Exception {
        return Base64.getEncoder().encodeToString(this.publicKey.getEncoded());
    }

    @Override
    public String sign(String plainText) throws Exception {
        Signature privateSignature = Signature.getInstance("SHA256withRSA");
        privateSignature.initSign(this.privateKey);
        privateSignature.update(plainText.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(privateSignature.sign());
    }

    private java.security.PrivateKey privateKey;
    private java.security.PublicKey publicKey;
}
