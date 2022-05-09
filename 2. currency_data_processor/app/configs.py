from pydantic import BaseSettings
from functools import lru_cache


class Configs(BaseSettings):
    web_host: str
    web_port: int

    kafka_broker: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_configs() -> Configs:
    return Configs()
