# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server.test import BaseTestCase
import requests_mock


class TestScenarioController(BaseTestCase):
    """ScenarioController integration test stubs"""

    def __init__(self, args):
        super().__init__(args)
        self.request_obj = {
            "sdate": "2020-10-16",
            "country": "GR",
            "markets": ["day_ahead"],
            "storage_units": [
                {
                    "power_capacity_KW": 0,
                    "energy_capacity_KWh": 0,
                    "inefficiency_rate_per_cent": 0,
                    "initial_final_SoC_per_cent": 0,
                    "location": {
                        "id": "string",
                        "name": "string"
                    }
                }
            ]
        }

    @requests_mock.mock()
    def test_scenarios_post(self, m):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        m.register_uri(
            'GET', 'https://db.flexgrid-project.eu/authorization/', text='OK')

        body = ScenarioParams.from_dict(self.request_obj)
        response = self.client.open(
            '/scenarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers={'Authorization': 'Bearer 1234'})
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        res = json.loads(response.data.decode('utf-8'))

        assert len(ScenarioResult.from_dict(
            res).flex_offer.day_ahead_market_offer.values) > 0

    @requests_mock.mock()
    def test_scenarios_post_wrong_auth(self, m):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        m.register_uri(
            'GET', 'https://db.flexgrid-project.eu/authorization/', text='nOK')

        body = ScenarioParams.from_dict(self.request_obj)
        response = self.client.open(
            '/scenarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers={'Authorization': 'Bearer 1234'})
        self.assert401(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @requests_mock.mock()
    def test_scenarios_post_no_auth(self, m):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        m.register_uri(
            'GET', 'https://db.flexgrid-project.eu/authorization/', text='OK')

        body = ScenarioParams.from_dict(self.request_obj)
        response = self.client.open(
            '/scenarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert401(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    import unittest
    unittest.main()
