# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server.adapters.stacked_revenues_adapter import stacked_revenues_adapter
from swagger_server.test import BaseTestCase
import responses

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

    @responses.activate
    def test_run(self):
        """Test case for stacked_revenues_post

        Initiates a simulation scenario
        """
        res = stacked_revenues_adapter(
            StackedRevenuesParams.from_dict(self.request_obj))

        print(f"The flexoffer is {res}")
        assert len(res.flex_offer.day_ahead_market_offer.values) > 0


if __name__ == '__main__':
    import unittest
    unittest.main()
