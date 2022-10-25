package tests;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import crypto.RsaPrivateKey;
import crypto.RsaPublicKey;

public class RsaTest {
    @Test
    public void rsaPrivateKeyWithInvalidSize() {
        assertThrows(Exception.class, () -> {
            RsaPrivateKey.NewPrivateKey(1);
        });
    }

    @Test
    public void rsaPrivateKeySign() throws Exception {
        var priKey = RsaPrivateKey.NewPrivateKey(2048);
        String plainText = "test message";
        String signature = priKey.sign(plainText);

        String pubKeyStr = priKey.generatePublicKey();

        assertTrue(RsaPublicKey.newPublicKey(pubKeyStr).verify(plainText, signature));
    }

    @Test
    public void rsaPrivateKeyVerifyFalse() throws Exception {
        var priKey = RsaPrivateKey.NewPrivateKey(2048);
        String plainText = "test message";
        String signature = priKey.sign(plainText);
        String pubKeyStr = priKey.generatePublicKey();

        String invalidPlainText = "test message1";
        assertFalse(RsaPublicKey.newPublicKey(pubKeyStr).verify(invalidPlainText, signature));
    }

    @Test
    public void rsaNewPublicKeyFail() {
        assertThrows(Exception.class, () -> {
            RsaPublicKey.newPublicKey("invalid");
        });
    }
}
