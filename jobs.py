import time
from datetime import datetime, timedelta

from db.schemas.price_schemas import CoinGeckoPrice, MarketDataPrice


def live_data_job(coingecko_api_handler, marketdata_api_handler, mongo_handler, logging_handler=None):
    """
    Get live price data from CoinGecko and MarketData apis
    :param coingecko_api_handler:
    :param marketdata_api_handler:
    :param mongo_handler:
    :return:
    """

    while True:
        try:
            # Get BTC price from CoinGecko
            btc_response_cg = coingecko_api_handler.get_live_price(coin_id='bitcoin', vs_currency='usd')
            # Get ETH price from CoinGecko
            eth_response_cg = coingecko_api_handler.get_live_price(coin_id='ethereum', vs_currency='usd')

            if btc_response_cg is not None:
                # Create data objects for MONGO
                btc_live_price_data_cg = CoinGeckoPrice(**btc_response_cg)
                # Insert BTC data into MONGO
                btc_insert_result = mongo_handler.insert(collection='btc_live_price',
                                                         document=btc_live_price_data_cg.dict())
                if btc_insert_result.acknowledged:
                    print("BTC live price data inserted successfully")
                    print("btc_insert_result: ", btc_insert_result)
                else:
                    print("BTC live price data insert failed")

            if eth_response_cg is not None:
                # Create data objects for MONGO
                eth_live_price_data_cg = CoinGeckoPrice(**eth_response_cg)
                # Insert ETH data into MONGO
                eth_insert_result = mongo_handler.insert(collection='eth_live_price',
                                                         document=eth_live_price_data_cg.dict())
                if eth_insert_result.acknowledged:
                    print("ETH live price data inserted successfully")
                    print("eth_insert_result: ", eth_insert_result)
                else:
                    print("ETH live price data insert failed")

            # wait 20 seconds
            time.sleep(20)
            print("Sleeping for 20 seconds...")

            # Get BTC price from MarketData
            btc_response_md = marketdata_api_handler.get_live_price(exchange='kraken', pair='btcusd')
            # Get ETH price from MarketData
            eth_response_md = marketdata_api_handler.get_live_price(exchange='kraken', pair='ethusd')

            if btc_response_md is not None:
                # Create data objects for MONGO
                btc_live_price_data_md = MarketDataPrice(**btc_response_md)
                # Insert BTC data into MONGO
                btc_insert_result = mongo_handler.insert(collection='btc_live_price',
                                                         document=btc_live_price_data_md.dict())
                if btc_insert_result.acknowledged:
                    print("BTC live price data inserted successfully")
                    print("btc_insert_result: ", btc_insert_result)
                else:
                    print("BTC live price data insert failed")

            if eth_response_md is not None:
                # Create data objects for MONGO
                eth_live_price_data_md = MarketDataPrice(**eth_response_md)
                # Insert ETH data into MONGO
                eth_insert_result = mongo_handler.insert(collection='eth_live_price',
                                                         document=eth_live_price_data_md.dict())
                if eth_insert_result.acknowledged:
                    print("ETH live price data inserted successfully")
                    print("eth_insert_result: ", eth_insert_result)
                else:
                    print("ETH live price data insert failed")

        except Exception as e:
            print(f"An error occurred while processing live data: {str(e)}")
            # Wait for 10 seconds before trying again
            time.sleep(10)
    pass
