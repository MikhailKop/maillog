from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    db_name: str = Field(default="maillog_database", env="DB_NAME")
    db_user: str = Field(default="app", env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")
    db_host: str = Field(default="127.0.0.1", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")
    file_path: str = Field(default="maillog", env="FILE_PATH")
    lock_file: str = Field(default="etl.lock")

    class Config:
        env_file = ".env"


settings = Settings()
