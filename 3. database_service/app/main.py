import faust
from repository import CurrencyRepository
from database import currency_collection

app = faust.App('currency_database', broker='kafka://localhost')

currency_data_topic = app.topic('currency_data_topic')


@app.agent(currency_data_topic)
async def save_data(currency_stream: faust.Stream):
    async for currency in currency_stream:
        _repository = CurrencyRepository(currency_collection=currency_collection)
        await _repository.save_to_database(currency_data=currency)
