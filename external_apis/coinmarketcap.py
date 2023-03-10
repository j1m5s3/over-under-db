import requests
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(dotenv_path=find_dotenv())

class CoinMarketCap:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    def get_latest(self, limit=10):
        params = {
            'start': '1',
            'limit': limit,
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        session = Session()
        session.headers.update(headers)
        try:
            requests.get(self.base_url, params=params)
            response = session.get(self.base_url, params=params)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)