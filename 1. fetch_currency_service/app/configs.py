from functools import lru_cache

from pydantic import BaseSettings


class Configs(BaseSettings):
    api_url: str
    api_key: str

    web_host: str
    web_port: int

    kafka_broker: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_configs() -> Configs:
    return Configs()
