import motor.motor_asyncio
from configs import get_configs

client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://{get_configs().mongodb_username}:'
                                                f'{get_configs().mongodb_password}@'
                                                f'{get_configs().mongodb_host}:'
                                                f'{get_configs().mongodb_port}')
database = client.database_name

currency_collection = database.currency
