from functools import lru_cache

from pydantic import BaseSettings


class Configs(BaseSettings):
    mongodb_host: str
    mongodb_port: int
    mongodb_username: str
    mongodb_password: str

    web_host: str
    web_port: int

    kafka_broker: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_configs() -> Configs:
    return Configs()
