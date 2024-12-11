from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_FILE: str

    @property
    def DATABASE_URL(self) -> str:
        return f"sqlite+aiosqlite:///{self.DB_FILE}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
