import requests


class MarketData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.cryptowat.ch/'

        self.headers = {
            'X-CW-API-Key': self.api_key,
        }

    def get_live_price(self, exchange, pair):
        """
        Get live price
        :param exchange: kraken, coinbase, etc
        :param pair: btcusd, ethusd, etc
        :return:
        """

        request_url = self.base_url + 'markets' + '/' + exchange + '/' + pair + '/price'

        try:
            response = requests.get(request_url, headers=self.headers)
            data = response.json()
            price = data['result']
            return price
        except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
            print(e)