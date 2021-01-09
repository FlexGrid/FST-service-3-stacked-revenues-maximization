from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from stacked_revenues.maximize_stacked_revenues import battery_portfolio
from swagger_server.adapters.market_adapter import MarketAdapter
from datetime import datetime, timedelta


def stacked_revenue_adapter(scenario_params):
    assert isinstance(scenario_params, ScenarioParams)

    ns = len(scenario_params.storage_units)
    print(f"We got {ns} batteries")

    martketAdapter = MarketAdapter(
        datetime.combine(scenario_params.sdate, datetime.min.time()),
        datetime.combine(scenario_params.sdate, datetime.min.time()) +
                         timedelta(days=1) - timedelta(minutes=1))

    dam_participation = martketAdapter.day_ahead_market()
    print(f"dam_participation= {dam_participation}" )
    # Create a battery object
    # bsu = battery_portfolio(ns, dam_participation, rm_participation, fm_participation, bm_participation, dam_prices, rup_prices, rdn_prices, fmp_prices, fmq_prices, bm_up_prices, bm_dn_prices,
    #                     p_max, E_max, roundtrip_eff, E0)

    # # Maximize stacked revenues
    # [Profits, pup, pdn, dam_schedule, rup_commitment, rdn_commitment, pflexibility, qflexibility,
    #     soc, DAM_profits, RM_profits, FM_profits, BM_profits] = bsu.maximize_stacked_revenues()

    # return ScenarioResult.from_dict({
    #     "sdate": str(scenario_params.sdate),
    #     "flex_offer": {
    #         "day_ahead_market_offer": {
    #             "values": [
    #                 {
    #                     "price": 0,
    #                     "volume": 0
    #                 }
    #             ],
    #             "price_unit": "€/MWh",
    #             "volume_unit": "MWh"
    #         },
    #         "reserve_market_offer": {
    #             "values": [
    #                 {
    #                     "price": 0,
    #                     "volume": 0
    #                 }
    #             ],
    #             "price_unit": "(€/MWh)^2",
    #             "volume_unit": "MWh^2"
    #         },
    #         "d-LMPs": {
    #             "values": [
    #                 {
    #                     "price": 0,
    #                     "volume": 0
    #                 }
    #             ],
    #             "price_unit": "€/MWh",
    #             "volume_unit": "MWh"
    #         },
    #         "q-LMPs": {
    #             "values": [
    #                 {
    #                     "price": 0,
    #                     "volume": 0
    #                 }
    #             ],
    #             "price_unit": "€/MVar",
    #             "volume_unit": "MVar"
    #         },
    #         "balancing_market_offer": {
    #             "values": [
    #                 {
    #                     "price": 0,
    #                     "volume": 0
    #                 }
    #             ],
    #             "price_unit": "€/MWh",
    #             "volume_unit": "MWh"
    #         }
    #     },
    #     "revenues": {
    #         "day_ahead_market_revenues": {
    #             "values": [
    #                 {"volume": 113.3, "price": 23.13},
    #                 {"volume": 12.4, "price": 23.13},
    #                 {"volume": 5.5, "price": 23.13},
    #                 {"volume": 225.3, "price": 23.13},
    #                 {"volume": 2.6, "price": 23.13},
    #                 {"volume": 21.1, "price": 23.13},
    #                 {"volume": 21, "price": 23.13},
    #                 {"volume": 24.9, "price": 23.13},
    #                 {"volume": 24.2, "price": 23.13},
    #                 {"volume": 1.45, "price": 23.13},
    #                 {"volume": 15.4, "price": 23.13},
    #                 {"volume": 15.2, "price": 23.13},
    #                 {"volume": 15.1, "price": 23.13},
    #                 {"volume": 1.45, "price": 23.13},
    #                 {"volume": 5.54, "price": 23.13},
    #                 {"volume": 5.34, "price": 23.13},
    #                 {"volume": 6.45, "price": 23.13},
    #                 {"volume": 8.45, "price": 23.13},
    #                 {"volume": 8.45, "price": 23.13},
    #                 {"volume": 3.34, "price": 23.13},
    #                 {"volume": 1.34, "price": 23.13},
    #                 {"volume": 2.45, "price": 23.13},
    #                 {"volume": 7.14, "price": 23.13},
    #                 {"volume": 9.53, "price": 23.13},
    #             ],
    #             "currency": "€"
    #         }
    #     }
    # })
