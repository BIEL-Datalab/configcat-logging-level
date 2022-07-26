from pydantic import BaseSettings


class Settings(BaseSettings):
    CANFIGCAT_POLL_INTERVAL_SECONDS: int = 60
    EXECUTION_ENV: str = "default"
    CONFIGCAT_SDK: str = None
    FEATURE_FLAG_NAME: str = "LOGGER_LEVEL"
    MOCK_LOGGING_LEVEL: str = "DEFAULT"

    class Config:
        env_file = ".env"


settings = Settings()
