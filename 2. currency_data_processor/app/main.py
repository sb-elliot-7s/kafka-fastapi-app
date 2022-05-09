import faust
from currency_data_processing import CurrencyDataProcessing
from configs import get_configs

app = faust.App('currency_data_processor',
                broker=f'kafka://{get_configs().kafka_broker}',
                web_host=get_configs().web_host,
                web_port=get_configs().web_port)

raw_currency_data_topic = app.topic('raw_currency_data_topic')
currency_data_topic = app.topic('currency_data_topic')


@app.agent(raw_currency_data_topic)
async def get_raw_currencies(currency_streams: faust.Stream):
    async for key, currency in currency_streams.items():
        currency_result = await CurrencyDataProcessing().processing(currency=currency)
        await currency_data_topic.send(key=key, value=currency_result.json().encode())
        yield currency_result
