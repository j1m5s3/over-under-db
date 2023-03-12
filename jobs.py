import time
from datetime import datetime, timedelta

from db.schemas.price_schemas import CoinGeckoPrice, MarketDataPrice


def live_data_job(coingecko_api_handler, marketdata_api_handler, mongo_handler, logging_handler):
    """
    Get live price data from CoinGecko and MarketData apis
    :param coingecko_api_handler:
    :param marketdata_api_handler:
    :param mongo_handler:
    :return:
    """

    # Get start timestamp
    job_start_timestamp = datetime.now().timestamp()

    while True:
        try:
            # Get BTC price from CoinGecko
            btc_response_cg = coingecko_api_handler.get_live_price(coin_id='bitcoin', vs_currency='usd')
            # Get ETH price from CoinGecko
            eth_response_cg = coingecko_api_handler.get_live_price(coin_id='ethereum', vs_currency='usd')

            # Create data objects for MONGO
            btc_live_price_data_cg = CoinGeckoPrice(**btc_response_cg)
            eth_live_price_data_cg = CoinGeckoPrice(**eth_response_cg)

            # Insert data into MONGO
            mongo_handler.insert_one(collection_name='btc_live_price',
                                     data=btc_live_price_data_cg.dict())
            mongo_handler.insert_one(collection_name='eth_live_price',
                                     data=eth_live_price_data_cg.dict())

            # wait 10 seconds
            time.sleep(5)

            # Get BTC price from MarketData
            btc_response_md = marketdata_api_handler.get_live_price(exchange='kraken', pair='btcusd')
            eth_response_md = marketdata_api_handler.get_live_price(exchange='kraken', pair='ethusd')

            # Create data objects for MONGO
            btc_live_price_data_md = MarketDataPrice(**btc_response_md)
            eth_live_price_data_md = MarketDataPrice(**eth_response_md)

            # Insert data into MONGO
            btc_insert_result = mongo_handler.insert_one(collection_name='btc_live_price',
                                                         data=btc_live_price_data_md.dict())
            if btc_insert_result.acknowledged:
                print('btc_insert_result: ', btc_insert_result)
            eth_insert_result = mongo_handler.insert_one(collection_name='eth_live_price', data=eth_live_price_data_md.dict())

        except Exception as e:
            print(f"An error occurred while processing live data: {str(e)}")
            # Wait for 10 seconds before trying again
            time.sleep(10)
    pass



