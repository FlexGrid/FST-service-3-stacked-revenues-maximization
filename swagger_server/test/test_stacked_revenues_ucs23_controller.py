# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStackedRevenuesUCS23Controller(BaseTestCase):
    """StackedRevenuesUCS23Controller integration test stubs"""

    def test_stacked_revenues_post(self):
        """Test case for stacked_revenues_post

        Initiates a simulation scenario for Stacked Revenues maximization
        """
        body = StackedRevenuesParams()
        response = self.client.open(
            '//stacked_revenues',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
