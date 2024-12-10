from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"sqlite+aiosqlite:///{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
