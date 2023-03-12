from external_apis.coinapi import CoinAPI
from external_apis.coingecko import CoinGecko
from external_apis.coinmarketcap import CoinMarketCap
from external_apis.marketdata import MarketData

from db.mongo_interface import MongoInterface

from datetime import datetime, timedelta

from dotenv import dotenv_values, find_dotenv

config = dotenv_values(dotenv_path=find_dotenv())


def live_data_job(start_timestamp, coingecko_api_handler, marketdata_api_handler, mongo_handler):
    """
    Get live price data from CoinGecko and MarketData apis
    :param start_timestamp:
    :param coingecko_api_handler:
    :param marketdata_api_handler:
    :param mongo_handler:
    :return:
    """
    pass


def historical_data_job(start_timestamp, coinapi_api_handler, coingecko_api_handler, mongo_handler):
    """
    Get historical price data from CoinGecko and CoinAPI apis
    :param start_timestamp:
    :param coinapi_api_handler:
    :param coingecko_api_handler:
    :param mongo_handler:
    :return:
    """
    pass


if __name__ == '__main__':
    pass
