# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.job_submitted import JobSubmitted  # noqa: E501
from swagger_server.models.pricing_job_result import PricingJobResult  # noqa: E501
from swagger_server.models.pricing_params import PricingParams  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPricingUCS42Controller(BaseTestCase):
    """PricingUCS42Controller integration test stubs"""

    def test_pricing_get(self):
        """Test case for pricing_get

        Retrieves information about a pricing job
        """
        response = self.client.open(
            '//pricing/{job_id}'.format(job_id='job_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pricing_post(self):
        """Test case for pricing_post

        Creates an evaluation of various pricing mechanisms
        """
        body = PricingParams()
        response = self.client.open(
            '//pricing',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
