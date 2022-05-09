import json
import uuid
import faust
from currency_data_service import CurrencyDataProvider
from configs import get_configs

app = faust.App('currency_app',
                broker=f'kafka://{get_configs().kafka_broker}',
                web_host=get_configs().web_host,
                web_port=get_configs().web_port)

raw_currency_data_topic = app.topic('raw_currency_data_topic')


@app.timer(interval=60)
async def fetch_currencies():
    currency_provider = CurrencyDataProvider(base_url=get_configs().api_url)
    params = {'function': 'CURRENCY_EXCHANGE_RATE', 'apikey': get_configs().api_key, 'from_currency': 'USD', 'to_currency': 'JPY'}
    currency = await currency_provider.fetch_data(params=params)
    if currency:
        await raw_currency_data_topic.send(key=uuid.uuid4().bytes, value=json.dumps(currency).encode())


@app.task
async def start():
    print('start')
