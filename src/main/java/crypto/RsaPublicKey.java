package crypto;

import java.nio.charset.StandardCharsets;
import java.security.KeyFactory;
import java.security.Signature;
import java.security.interfaces.RSAPublicKey;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

import javax.crypto.Cipher;

public class RsaPublicKey implements PublicKey {
    public static PublicKey newPublicKey(String encodedPubKey) throws Exception {
        var decodedPubKey = Base64.getDecoder().decode(encodedPubKey);
        KeyFactory kf = KeyFactory.getInstance("RSA");
        var key = (RSAPublicKey) kf.generatePublic(new X509EncodedKeySpec(decodedPubKey));

        return new RsaPublicKey(key);
    }

    @Override
    public byte[] encrypt(byte[] plainText) throws Exception {
        var encryptCipher = Cipher.getInstance("RSA");
        encryptCipher.init(Cipher.ENCRYPT_MODE, this.key);
        byte[] encryptedBytes = encryptCipher.doFinal(plainText);
        return Base64.getEncoder().encode(encryptedBytes);
    }

    @Override
    public boolean verify(String plainText, String signature) throws Exception {
        Signature publicSignature = Signature.getInstance("SHA256withRSA");
        publicSignature.initVerify(this.key);
        publicSignature.update(plainText.getBytes(StandardCharsets.UTF_8));
        return publicSignature.verify(Base64.getDecoder().decode(signature));
    }

    private RsaPublicKey(RSAPublicKey key) {
        this.key = key;
    }

    private RSAPublicKey key;
}
