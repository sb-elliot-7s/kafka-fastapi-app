import faust
from repository import CurrencyRepository
from database import currency_collection
from configs import get_configs

app = faust.App('currency_database',
                broker=f'kafka://{get_configs().kafka_broker}',
                web_host=get_configs().web_host,
                web_port=get_configs().web_port)

currency_data_topic = app.topic('currency_data_topic')


@app.agent(currency_data_topic)
async def save_data(currency_stream: faust.Stream):
    async for currency in currency_stream:
        _repository = CurrencyRepository(currency_collection=currency_collection)
        await _repository.save_to_database(currency_data=currency)
