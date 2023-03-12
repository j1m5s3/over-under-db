import logging
import logging.handlers
import multiprocessing


from external_apis.coingecko import CoinGecko
from external_apis.marketdata import MarketData

from db.mongo_interface import MongoInterface

from .jobs import live_data_job

from datetime import datetime, timedelta

from dotenv import dotenv_values, find_dotenv

config = dotenv_values(dotenv_path=find_dotenv())


def live_price_worker():
    # Initialize api handlers
    coingecko_api_handler = CoinGecko()
    marketdata_api_handler = MarketData(api_key=config['MARKETDATA_API_KEY'])

    mongo_handler = MongoInterface(db_name=config['MONGO_DB_NAME'],
                                   connection_url=config['MONGO_CONNECTION_URL'])

    live_data_job(coingecko_api_handler=coingecko_api_handler,
                  marketdata_api_handler=marketdata_api_handler,
                  mongo_handler=mongo_handler)

    return


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

    # create a shared log queue
    log_queue = multiprocessing.Queue()

    # create a listener to handle writing log messages to file
    handler = logging.FileHandler('log.txt')
    listener = logging.handlers.QueueListener(log_queue, handler)
    listener.start()

    pass
