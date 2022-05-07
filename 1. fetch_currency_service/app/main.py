import json
import uuid

import faust
from currency_data_service import CurrencyDataProvider
from configs import get_configs

app = faust.App('currency_app', broker='kafka://localhost')

raw_currency_data_topic = app.topic('raw_currency_data_topic')


@app.timer(interval=60)
async def fetch_currencies():
    currency_provider = CurrencyDataProvider(base_url=get_configs().api_url)
    params = {'apikey': get_configs().api_key, 'from_currency': 'USD', 'to_currency': 'BTC'}
    currency = await currency_provider.fetch_data(params=params)

    if currency:
        await raw_currency_data_topic.send(key=uuid.uuid4().bytes, value=json.dumps(currency).encode())


@app.task
async def start():
    print('start')