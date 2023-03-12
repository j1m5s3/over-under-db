import requests


class MarketData:
    def __init__(self,):
        self.base_url = 'https://api.cryptowat.ch/'

    def get_live_price(self, exchange, pair):
        """
        Get live price
        :param exchange: kraken, coinbase, etc
        :param pair: btcusd, ethusd, etc
        :return:
        """

        request_url = self.base_url + 'markets' + '/' + exchange + '/' + pair + '/price'

        try:
            response = requests.get(request_url)
            data = response.json()
            return data
        except (ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
            print(e)