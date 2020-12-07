# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scenario_params_inner import ScenarioParamsInner  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScenarioController(BaseTestCase):
    """ScenarioController integration test stubs"""

    def test_scenarios_post(self):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        body = [ScenarioParamsInner()]
        response = self.client.open(
            '//scenarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
