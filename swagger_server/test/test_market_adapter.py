# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server.adapters.market_adapter import MarketAdapter
from swagger_server.test import BaseTestCase
from datetime import datetime
import os
import responses


class TestMarketAdapter(BaseTestCase):
    """MarketAdapter integration test stubs"""

    def __init__(self, args):
        super().__init__(args)
        self.marketAdapter = MarketAdapter(datetime.fromisoformat('2020-12-01T00:00:00+02:00'),
                                           datetime.fromisoformat('2020-12-01T23:00:00+02:00'))

    @responses.activate
    def test_run(self):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        res = self.marketAdapter.day_ahead_market()
        assert len(res) == 24

        res = self.marketAdapter.balancing_market_up()
        assert len(res) == 24

        res = self.marketAdapter.balancing_market_down()
        assert len(res) == 24


if __name__ == '__main__':
    import unittest
    unittest.main()
