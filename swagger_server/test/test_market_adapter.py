# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server.adapters.market_adapter import MarketAdapter
from swagger_server.test import BaseTestCase
from datetime import datetime
import os

class TestMarketAdapter(BaseTestCase):
    """MarketAdapter integration test stubs"""

    def __init__(self, args):
        super().__init__(args)
        self.marketAdapter = MarketAdapter(datetime.fromisoformat('2020-12-01T00:00:00+02:00'), datetime.fromisoformat('2020-12-02T00:00:00+02:00'))

    def test_run(self):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        print(f"The token is {os.environ.get('FINGRID_TOKEN')}")
        print(f"DaY ahead: {self.marketAdapter.day_ahead_market()}")
        
        # assert len(res.flex_offer.day_ahead_market_offer.values) > 0


if __name__ == '__main__':
    import unittest
    unittest.main()
