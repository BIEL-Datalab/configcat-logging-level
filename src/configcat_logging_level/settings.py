from pydantic import BaseSettings


class Settings(BaseSettings):
    EXECUTION_ENV: str = "default"
    CONFIGCAT_SDK: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
