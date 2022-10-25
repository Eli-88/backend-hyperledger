package config;

public class Config {
    private String pemFilePath;
    private String userId;
    private String connConfigPath;

    public Config(String pemFilePath, String userId, String connConfigPath) {
        this.pemFilePath = pemFilePath;
        this.userId = userId;
        this.connConfigPath = connConfigPath;
    }

    public String getPemFilePath() {
        return this.pemFilePath;
    }

    public String getUserId() {
        return this.userId;
    }

    public String getConnConfigPath() {
        return this.connConfigPath;
    }
}
