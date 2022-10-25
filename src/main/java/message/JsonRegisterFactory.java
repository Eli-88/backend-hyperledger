package message;

import com.google.gson.Gson;

public class JsonRegisterFactory implements RegisterFactory {
    @Override
    public Register create(String rawMsg) throws Exception {
        var gson = new Gson();
        return gson.fromJson(rawMsg, Register.class);
    }
}
