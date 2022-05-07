from schemas import CurrencySchema


class CurrencyDataProcessing:

    @staticmethod
    async def processing(currency):
        return CurrencySchema.parse_obj(currency.get('Realtime Currency Exchange Rate'))
