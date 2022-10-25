package config;

import java.io.InputStream;

import com.google.gson.Gson;

public class ConfigFactory {
    public Config create() throws Exception {
        InputStream is = getClass().getClassLoader().getResourceAsStream("config.txt");
        Gson gson = new Gson();
        return gson.fromJson(new String(is.readAllBytes()), Config.class);
    }
}
