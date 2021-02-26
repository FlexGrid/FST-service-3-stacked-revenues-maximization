# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFlexOffersUCS43Controller(BaseTestCase):
    """FlexOffersUCS43Controller integration test stubs"""

    def test_flex_offers_post(self):
        """Test case for flex_offers_post

        Creates a Flexibility Offser (FlexOffer) based of FlexAssets
        """
        body = FlexOfferParams()
        response = self.client.open(
            '/flex_offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
