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
        print(f"The params are --> {params}")
        result = requests.request("GET", url, params=params,
                                  headers=headers)

        # print(f"The result is --> {json.loads(result.content)[0]['values']}")
        return [{'value': val['value'], 'start_time': val['startTime'], 'end_time': val['endTime']} for val in json.loads(result.content)[0]['values']]

    def fmp(self, location_ids):
        dataset = {'DSO_AREA_1': [0] * 24,
                   'DSO_AREA_2': [-100.27, -100.27, -10.27, -10.27, -10.27, -10.27, 0, 0, -9.59, -9.59,
                                  -9.54, -15, -15, -15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'DSO_AREA_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15,
                                  3.55, 3.01, 3.01, 3.44, 3.41, 13.74, 12.02, 15, 12.55, 12.53, 12.04, 8.55, 2.98],
                   'DSO_AREA_4': [-10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.27, -10.01, -9.92, -9.54, -9.17,
                                  -15, -15, -15, -9.26, -9.54, -9.54, -9.17, 1.83, 1.55, -9.65, 1.02, 0.61, 0.61],
                   'DSO_AREA_5': [2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 2.98, 3.36, 3.25, 15, 15, 3.54, 3.54, 3.54, 15,
                                  15, 15, 15, 15, 12.57, 12, 12.07, 15, 15], }

        return [dataset[lid] for lid in location_ids]

    def fmq(self, location_ids):
        dataset = {'DSO_AREA_1': [0] * 24,
                   'DSO_AREA_2': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -0.05, -0.25, -6.88, -6.88, -6.87, -10.61,
                                  -10.4, -10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   'DSO_AREA_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11.24, 3, 3, 3, 3, 3, 10.34, 9.12,
                                  10.54, 8.83, 8.82, 8.69, 6.41, 3],
                   'DSO_AREA_4': [-6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.97, -6.94, -6.93, -6.87, -6.82, -10.62,
                                  -10.62, -10.62, -6.83, -6.87, -6.87, -6.82, 0.93, 0.79, -6.89, 0.52, 0.31, 0.31],
                   'DSO_AREA_5': [3, 3, 3, 3, 3, 3, 3, 3, 3, 11.24, 10.85, 3, 3, 3, 10.94, 11.24, 11.24, 10.85, 10.54,
                                  8.83, 9.11, 8.67, 11, 11], }

        return [dataset[lid] for lid in location_ids]

    def day_ahead_market(self):
        if os.environ.get("SAMPLE_DATA"):
            result = json.loads("""[
                {
                    "category": "dayAhead",
                    "createdTime": 1601462571635,
                    "type": "price",
                    "SubType": "area",
                    "resolution": "PT1H",
                    "unit": "EUR/MWh",
                    "scale": 2,
                    "startTime": "2020-10-15T21:00:00Z",
                    "endTime": "2020-10-16T21:00:00Z",
                    "values": [
                        {
                            "startTime": "2020-10-15T21:00:00Z",
                            "endTime": "2020-10-15T22:00:00Z",
                            "value": 20.01
                        },
                        {
                            "startTime": "2020-10-15T22:00:00Z",
                            "endTime": "2020-10-15T23:00:00Z",
                            "value": 20.13
                        },
                        {
                            "startTime": "2020-10-15T23:00:00Z",
                            "endTime": "2020-10-16T00:00:00Z",
                            "value": 19.7
                        },
                        {
                            "startTime": "2020-10-16T00:00:00Z",
                            "endTime": "2020-10-16T01:00:00Z",
                            "value": 19.56
                        },
                        {
                            "startTime": "2020-10-16T01:00:00Z",
                            "endTime": "2020-10-16T02:00:00Z",
                            "value": 19.57
                        },
                        {
                            "startTime": "2020-10-16T02:00:00Z",
                            "endTime": "2020-10-16T03:00:00Z",
                            "value": 19.96
                        },
                        {
                            "startTime": "2020-10-16T03:00:00Z",
                            "endTime": "2020-10-16T04:00:00Z",
                            "value": 35.23
                        },
                        {
                            "startTime": "2020-10-16T04:00:00Z",
                            "endTime": "2020-10-16T05:00:00Z",
                            "value": 50.03
                        },
                        {
                            "startTime": "2020-10-16T05:00:00Z",
                            "endTime": "2020-10-16T06:00:00Z",
                            "value": 54.29
                        },
                        {
                            "startTime": "2020-10-16T06:00:00Z",
                            "endTime": "2020-10-16T07:00:00Z",
                            "value": 66.22
                        },
                        {
                            "startTime": "2020-10-16T07:00:00Z",
                            "endTime": "2020-10-16T08:00:00Z",
                            "value": 62.34
                        },
                        {
                            "startTime": "2020-10-16T08:00:00Z",
                            "endTime": "2020-10-16T09:00:00Z",
                            "value": 56.59
                        },
                        {
                            "startTime": "2020-10-16T09:00:00Z",
                            "endTime": "2020-10-16T10:00:00Z",
                            "value": 52.9
                        },
                        {
                            "startTime": "2020-10-16T10:00:00Z",
                            "endTime": "2020-10-16T11:00:00Z",
                            "value": 52.84
                        },
                        {
                            "startTime": "2020-10-16T11:00:00Z",
                            "endTime": "2020-10-16T12:00:00Z",
                            "value": 52.79
                        },
                        {
                            "startTime": "2020-10-16T12:00:00Z",
                            "endTime": "2020-10-16T13:00:00Z",
                            "value": 45.23
                        },
                        {
                            "startTime": "2020-10-16T13:00:00Z",
                            "endTime": "2020-10-16T14:00:00Z",
                            "value": 44.57
                        },
                        {
                            "startTime": "2020-10-16T14:00:00Z",
                            "endTime": "2020-10-16T15:00:00Z",
                            "value": 46.42
                        },
                        {
                            "startTime": "2020-10-16T15:00:00Z",
                            "endTime": "2020-10-16T16:00:00Z",
                            "value": 58.44
                        },
                        {
                            "startTime": "2020-10-16T16:00:00Z",
                            "endTime": "2020-10-16T17:00:00Z",
                            "value": 59.68
                        },
                        {
                            "startTime": "2020-10-16T17:00:00Z",
                            "endTime": "2020-10-16T18:00:00Z",
                            "value": 58.56
                        },
                        {
                            "startTime": "2020-10-16T18:00:00Z",
                            "endTime": "2020-10-16T19:00:00Z",
                            "value": 39.59
                        },
                        {
                            "startTime": "2020-10-16T19:00:00Z",
                            "endTime": "2020-10-16T20:00:00Z",
                            "value": 35.96
                        },
                        {
                            "startTime": "2020-10-16T20:00:00Z",
                            "endTime": "2020-10-16T21:00:00Z",
                            "value": 26.48
                        }
                    ],
                    "attributes": [
                        {
                            "role": null,
                            "name": "deliveryArea",
                            "value": "FI"
                        },
                        {
                            "role": null,
                            "name": "status",
                            "value": "O"
                        },
                        {
                            "role": null,
                            "name": "currency",
                            "value": "EUR"
                        },
                        {
                            "role": null,
                            "name": "confirmationStatus",
                            "value": "confirmed"
                        }
                    ]
                }
            ] """)
            return [{'value': val['value'], 'start_time': val['startTime'], 'end_time': val['endTime']} for val in result[0]['values']]
        return self.nordpool('FI')

    def balancing_market_up(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 20.010000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 20.130000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 19.700000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 19.560000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 19.570000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 19.960000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 35.230000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 50.030000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 54.290000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 66.220000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 62.340000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 100.590000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 52.900000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 52.840000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 52.790000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 45.230000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 44.570000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 46.420000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 58.440000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 80.000000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 58.560000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 39.590000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 35.960000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 52.500000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")
        return self.fingrid(244)

    def balancing_market_down(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 20.010000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 20.130000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 19.700000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 19.560000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 19.570000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 19.960000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 35.230000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 54.290000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 28.000000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 28.000000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 56.590000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 52.900000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 52.840000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 52.790000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 24.500000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 18.500000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 26.000000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 59.680000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 58.560000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 39.590000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 16.000000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 26.480000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")

        return self.fingrid(106)

    def reserve_market(self):
        if os.environ.get("SAMPLE_DATA"):
            return json.loads("""[
                {
                    "value": 5.240000,
                    "start_time": "2020-10-15T21:00:00+0000",
                    "end_time": "2020-10-15T22:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-15T22:00:00+0000",
                    "end_time": "2020-10-15T23:00:00+0000"
                },
                {
                    "value": 9.940000,
                    "start_time": "2020-10-15T23:00:00+0000",
                    "end_time": "2020-10-16T00:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-16T00:00:00+0000",
                    "end_time": "2020-10-16T01:00:00+0000"
                },
                {
                    "value": 9.850000,
                    "start_time": "2020-10-16T01:00:00+0000",
                    "end_time": "2020-10-16T02:00:00+0000"
                },
                {
                    "value": 9.150000,
                    "start_time": "2020-10-16T02:00:00+0000",
                    "end_time": "2020-10-16T03:00:00+0000"
                },
                {
                    "value": 9.310000,
                    "start_time": "2020-10-16T03:00:00+0000",
                    "end_time": "2020-10-16T04:00:00+0000"
                },
                {
                    "value": 12.770000,
                    "start_time": "2020-10-16T04:00:00+0000",
                    "end_time": "2020-10-16T05:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T05:00:00+0000",
                    "end_time": "2020-10-16T06:00:00+0000"
                },
                {
                    "value": 12.120000,
                    "start_time": "2020-10-16T06:00:00+0000",
                    "end_time": "2020-10-16T07:00:00+0000"
                },
                {
                    "value": 12.500000,
                    "start_time": "2020-10-16T07:00:00+0000",
                    "end_time": "2020-10-16T08:00:00+0000"
                },
                {
                    "value": 12.000000,
                    "start_time": "2020-10-16T08:00:00+0000",
                    "end_time": "2020-10-16T09:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T09:00:00+0000",
                    "end_time": "2020-10-16T10:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T10:00:00+0000",
                    "end_time": "2020-10-16T11:00:00+0000"
                },
                {
                    "value": 12.690000,
                    "start_time": "2020-10-16T11:00:00+0000",
                    "end_time": "2020-10-16T12:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T12:00:00+0000",
                    "end_time": "2020-10-16T13:00:00+0000"
                },
                {
                    "value": 12.120000,
                    "start_time": "2020-10-16T13:00:00+0000",
                    "end_time": "2020-10-16T14:00:00+0000"
                },
                {
                    "value": 12.310000,
                    "start_time": "2020-10-16T14:00:00+0000",
                    "end_time": "2020-10-16T15:00:00+0000"
                },
                {
                    "value": 12.880000,
                    "start_time": "2020-10-16T15:00:00+0000",
                    "end_time": "2020-10-16T16:00:00+0000"
                },
                {
                    "value": 13.080000,
                    "start_time": "2020-10-16T16:00:00+0000",
                    "end_time": "2020-10-16T17:00:00+0000"
                },
                {
                    "value": 14.000000,
                    "start_time": "2020-10-16T17:00:00+0000",
                    "end_time": "2020-10-16T18:00:00+0000"
                },
                {
                    "value": 9.000000,
                    "start_time": "2020-10-16T18:00:00+0000",
                    "end_time": "2020-10-16T19:00:00+0000"
                },
                {
                    "value": 8.850000,
                    "start_time": "2020-10-16T19:00:00+0000",
                    "end_time": "2020-10-16T20:00:00+0000"
                },
                {
                    "value": 7.920000,
                    "start_time": "2020-10-16T20:00:00+0000",
                    "end_time": "2020-10-16T21:00:00+0000"
                }
            ]""")

        return self.fingrid(79)
