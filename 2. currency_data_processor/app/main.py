import faust
from schemas import CurrencySchema

app = faust.App('currency_data_processor', broker='kafka://localhost')

raw_currency_data_topic = app.topic('raw_currency_data_topic')
currency_data_topic = app.topic('currency_data_topic')


@app.agent(raw_currency_data_topic)
async def get_raw_currencies(currency_streams: faust.Stream):
    async for key, currency in currency_streams.items():
        currency_result = CurrencySchema.parse_obj(currency.get('Realtime Currency Exchange Rate'))
        await currency_data_topic.send(key=key, value=currency_result.json().encode())
        yield currency_result
