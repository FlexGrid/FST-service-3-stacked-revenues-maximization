import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from swagger_server.models.day_price_vector_euro import DayPriceVectorEuro  # noqa: E501
import json

class MarketAdapter:
    def __init__(self, start_timestamp, end_timestamp):
        load_dotenv()

        self.start_timestamp = datetime.utcfromtimestamp(
            start_timestamp.timestamp()).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.end_timestamp = datetime.utcfromtimestamp(
            end_timestamp.timestamp()).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.market_ids = {
            79: 'Frequency containment reserve for normal operation, hourly market prices',
            244: 'Up-regulating price in the balancing power market',
            106: 'Down-regulation price in the balancing market',
        }

    def fingrid(self, market_id):

        url = f"https://api.fingrid.fi/v1/variable/{market_id}/events/json"
        headers = {'x-api-key': os.environ.get("FINGRID_TOKEN")}
        return requests.request("GET", url, params={'start_time': self.start_timestamp, 'end_time': self.end_timestamp},  headers=headers).content


    def day_ahead_market(self):
        return DayPriceVectorEuro.from_dict({'currency': '€', 'values': json.loads(self.fingrid(79))})

    def balancing_market_up(self):
        return self.fingrid(244)

    def balancing_market_down(self):
        return self.fingrid(106)
