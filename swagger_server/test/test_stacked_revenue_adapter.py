# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server.adapters.stacked_revenue_adapter import stacked_revenue_adapter
from swagger_server.test import BaseTestCase


class TestStackedRevenueAdapter(BaseTestCase):
    """StackedRevenueAdapter integration test stubs"""

    def __init__(self, args):
        super().__init__(args)
        self.request_obj = {
            "sdate": "2020-10-16",
            "country": "GR",
            "markets": ["day_ahead"],
            "storage_units": [
                {
                    "power_capacity_KW": 5,
                    "energy_capacity_KWh": 10,
                    "inefficiency_rate_per_cent": 0.5,
                    "initial_final_SoC_per_cent": 0.5,
                    "location": {
                        "id": "string",
                        "name": "string"
                    }
                },
                {
                    "power_capacity_KW": 5,
                    "energy_capacity_KWh": 10,
                    "inefficiency_rate_per_cent": 0.5,
                    "initial_final_SoC_per_cent": 0.5,
                    "location": {
                        "id": "string",
                        "name": "string"
                    }
                }
            ]
        }

    def test_run(self):
        """Test case for scenarios_post

        Initiates a simulation scenario
        """
        res = stacked_revenue_adapter(
            ScenarioParams.from_dict(self.request_obj))

        print(f"the resutls if {res}")
        assert len(res.flex_offer.day_ahead_market_offer.values) > 0


if __name__ == '__main__':
    import unittest
    unittest.main()
