class CurrencyRepository:
    def __init__(self, currency_collection):
        self._currency_collection = currency_collection

    async def save_to_database(self, currency_data: dict):
        result = await self._currency_collection.insert_one(currency_data)
        if not result.inserted_id:
            print('handle error')
