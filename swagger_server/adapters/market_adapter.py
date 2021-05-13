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

    def fmp(self, location_ids):
        dataset = {'BSU1': [-10.27, -10.27, -10.27, -10.27, -10.27, -10.27, 0, 0, -9.59, -9.59,
                            -9.54, -15, -15, -15, -9.94, -9.97, -9.59, -9.64, 1.83, 1.52, 1.51, 0.26, 0, -10.27],
                   'BSU2': [2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 11.43, 12.46, 13.74, 13.74, 15,
                            3.55, 3.01, 3.01, 3.44, 3.41, 13.74, 12.02, 15, 12.55, 12.53, 12.04, 8.55, 2.98],
                   'BSU3': [-10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.01, -9.92, -9.54, -9.17,
                            -15, -15, -15, -9.26, -9.54, -9.54, -9.17, 1.83, 1.55, -9.65, 1.02, 0.61, 0.61],
                   'BSU4': [2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 3.36, 3.25, 15, 15, 3.54, 3.54, 3.54, 15,
                            15, 15, 15, 15, 12.57, 12, 12.07, 15, 15], }

        return [dataset[lid] for lid in location_ids]

    def fmq(self, location_ids):
        dataset = {'BSU1': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -0.05, -0.25, -6.88, -6.88, -6.87, -10.61,
                            -10.4, -10.4, -6.93, -6.93, -6.88, -6.89, 0.93, 0.78, 0.77, 0, 0, -6.97],
                   'BSU2': [3, 3, 3, 3, 3, 3, 8.47, 8.87, 10.34, 10.34, 11.24, 3, 3, 3, 3, 3, 10.34, 9.12,
                            10.54, 8.83, 8.82, 8.69, 6.41, 3],
                   'BSU3': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.94, -6.93, -6.87, -6.82, -10.62,
                            -10.62, -10.62, -6.83, -6.87, -6.87, -6.82, 0.93, 0.79, -6.89, 0.52, 0.31, 0.31],
                   'BSU4': [3, 3, 3, 3, 3, 3, 3, 3, 3, 11.24, 10.85, 3, 3, 3, 10.94, 11.24, 11.24, 10.85, 10.54,
                            8.83, 9.11, 8.67, 11, 11], }

        return [dataset[lid] for lid in location_ids]

    def day_ahead_market(self):
        #        return self.fingrid(79)
        return self.nordpool('FI')

    def balancing_market_up(self):
        return self.fingrid(244)

    def balancing_market_down(self):
        return self.fingrid(106)

    def reserve_market(self):
        return self.fingrid(79)
