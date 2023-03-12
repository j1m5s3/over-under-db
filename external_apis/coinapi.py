import requests
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(dotenv_path=find_dotenv())


class CoinAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://rest.coinapi.io/v1/'
        self.headers = {
            'X-CoinAPI-Key': self.api_key
        }

    def get_live_price(self, symbol_id, vs_currency):
        """
        Get live price
        :param symbol_id: BTC, ETH, etc
        :param vs_currency: usd, eur, etc
        :return:
        """

        request_url = self.base_url + 'exchangerate' + '/' + symbol_id + '/' + vs_currency

        try:
            response = requests.get(request_url, headers=self.headers)
            data = response.json()
            return data
        except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
            print(e)