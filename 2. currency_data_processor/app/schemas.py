from datetime import datetime

from pydantic import BaseModel, Field


# {
#     "Realtime Currency Exchange Rate": {
#         "1. From_Currency Code": "USD",
#         "2. From_Currency Name": "United States Dollar",
#         "3. To_Currency Code": "JPY",
#         "4. To_Currency Name": "Japanese Yen",
#         "5. Exchange Rate": "130.55000000",
#         "6. Last Refreshed": "2022-05-07 14:50:21",
#         "7. Time Zone": "UTC",
#         "8. Bid Price": "130.55000000",
#         "9. Ask Price": "130.55000000"
#     }
# }

class CurrencySchema(BaseModel):
    from_currency_code: str = Field(alias='1. From_Currency Code')
    from_currency_name: str = Field(alias='2. From_Currency Name')
    to_currency_code: str = Field(alias='3. To_Currency Code')
    to_currency_name: str = Field(alias='4. To_Currency Name')
    exchange_rate: float = Field(alias='5. Exchange Rate')
    last_refreshed: datetime = Field(alias='6. Last Refreshed')
    time_zone: str = Field(alias='7. Time Zone')
    bid_price: float = Field(alias='8. Bid Price')
    ask_price: float = Field(alias='9. Ask Price')
