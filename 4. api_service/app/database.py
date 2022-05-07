import motor.motor_asyncio
from configs import get_configs

client = motor.motor_asyncio.AsyncIOMotorClient(get_configs().mongodb_host, get_configs().mongodb_port)

database = client.database_name

currency_collection = database.currency


async def get_currency_collection():
    yield currency_collection
