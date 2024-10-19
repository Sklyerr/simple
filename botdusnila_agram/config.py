from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()

API = "9d9bdfa02b21d17b02cc511b105a809a" #API погода
API_S = "EaXtRiZKhNlUjPv6cB2GvEnNGb9vELuB" #API gid