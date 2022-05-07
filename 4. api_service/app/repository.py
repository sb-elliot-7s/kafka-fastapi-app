class CurrencyRepository:
    def __init__(self, currency_collection):
        self._currency_collection = currency_collection

    async def get_currency(self):
        return await self._currency_collection.find_one()

    async def get_currencies(self, limit: int, skip: int):
        return [currency async for currency in self._currency_collection
                .find()
                .sort('last_refreshed', -1)
                .skip(skip)
                .limit(limit)]
