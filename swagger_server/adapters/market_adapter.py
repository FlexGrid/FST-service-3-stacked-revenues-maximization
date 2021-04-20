import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
from . nordpool_auth_client import NordpoolAuthClient
import dateutil.parser


class MarketAdapter:
    def __init__(self, start_timestamp, end_timestamp):
        load_dotenv()

        self.start_timestamp = datetime.utcfromtimestamp(
            start_timestamp.timestamp()).replace(minute=0, second=0).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.end_timestamp = datetime.utcfromtimestamp(
            end_timestamp.timestamp()).replace(minute=0, second=0).strftime('%Y-%m-%dT%H:%M:%SZ')
        self.market_ids = {
            79: 'Frequency containment reserve for normal operation, hourly market prices',
            244: 'Up-regulating price in the balancing power market',
            106: 'Down-regulation price in the balancing market',
        }

    def fingrid(self, market_id):

        url = f"https://api.fingrid.fi/v1/variable/{market_id}/events/json"
        headers = {'x-api-key': os.environ.get("FINGRID_TOKEN")}
        return json.loads(requests.request("GET", url, params={
            'start_time': self.start_timestamp,
            'end_time': self.end_timestamp},
            headers=headers).content)

    def nordpool(self, deliveryarea):
        url = f"https://marketdata-api.nordpoolgroup.com/dayahead/prices/area"
        headers = NordpoolAuthClient().auth_headers()
        # print(f"The headers are {headers}")
        params = {
            'deliveryarea': deliveryarea,
            'status': 'O',
            'currency': 'EUR',
            'startTime': self.start_timestamp,
            'endTime':  (dateutil.parser.isoparse(self.end_timestamp) + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        }
        # print(f"The params are --> {params}")
        result = requests.request("GET", url, params=params,
                                  headers=headers)

        # print(f"The result is --> {json.loads(result.content)[0]['values']}")
        return [{'value': val['value'], 'start_time': val['startTime'], 'end_time': val['endTime']} for val in json.loads(result.content)[0]['values']]

    def day_ahead_market(self):
        #        return self.fingrid(79)
        return self.nordpool('FI')

    def balancing_market_up(self):
        return self.fingrid(244)

    def balancing_market_down(self):
        return self.fingrid(106)
