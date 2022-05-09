import aiohttp


class CurrencyDataProvider:
    def __init__(self, base_url: str):
        self._base_url = base_url

    async def fetch_data(self, params: dict) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self._base_url, params=params) as response:
                return await response.json() if response.status == 200 else {}
