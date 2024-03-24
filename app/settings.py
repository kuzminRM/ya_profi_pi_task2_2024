from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    SERVICE_NAME: str = "ya_profi"
    ROOT_PATH: str = "/"

    API_host: str = "0.0.0.0"
    API_port: int = "9024"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
