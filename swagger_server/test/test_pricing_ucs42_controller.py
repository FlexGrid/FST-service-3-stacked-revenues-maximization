# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pricing_params import PricingParams  # noqa: E501
from swagger_server.models.pricing_result import PricingResult  # noqa: E501
from swagger_server.test import BaseTestCase
import responses


class TestPricingUCS42Controller(BaseTestCase):
    """PricingUCS42Controller integration test stubs"""

    @responses.activate
    def test_pricing_post(self):
        """Test case for pricing_post

        Creates an evaluation of various pricing mechanisms
        """
        body = PricingParams()
        response = self.client.open(
            '/pricing',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers={'Authorization': 'Bearer 1234'})
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
