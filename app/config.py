from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    database_url: str
    test_database_url: str
    secret_key: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()
