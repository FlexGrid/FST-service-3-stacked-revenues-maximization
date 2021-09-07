# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server.test import BaseTestCase
import responses

from dateutil import parser
import datetime


class TestFlexOffersUCS43Controller(BaseTestCase):
    """FlexOffersUCS43Controller integration test stubs"""

    def __init__(self, args):
        super().__init__(args)
        base_date = parser.parse("2021/9/7T00:00:00Z")
        self.request_obj = {
            "country": "Greece",
            "flex_assets": [
                {
                    "consumer_id": "asdf",
                    "location": {"id": "DSO_AREA_1", "name": "string"},
                    "reserve_market_offer_up": {
                        "price_unit": "€/MWh",
                        "volume_unit": "MWh",
                        "values": [{
                            "start_timestamp": (base_date + datetime.timedelta(
                                hours=offset
                            )).isoformat(),
                            "end_timestamp": (base_date + datetime.timedelta(
                                hours=(offset+1)
                            )).isoformat(),
                            "values": [{
                                "price": 123,
                                "volume": 39
                            }]
                        } for offset in range(24)]
                    }
                }
            ]
        }

    @responses.activate
    def test_flex_offers_post(self):
        """Test case for flex_offers_post

        Creates a Flexibility Offser (FlexOffer) based of FlexAssets
        """
        body = FlexOfferParams.from_dict(self.request_obj)
        response = self.client.open(
            '/flex_offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers={'Authorization': 'Bearer 1234'})
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        res = json.loads(response.data.decode('utf-8'))

        res_obj = FlexOfferResult.from_dict(res)

        print(f"The result object is {res_obj}")

if __name__ == '__main__':
    import unittest
    unittest.main()
