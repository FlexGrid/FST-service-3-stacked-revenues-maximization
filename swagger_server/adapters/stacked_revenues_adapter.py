from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_wh import DayOfferVectorEuroMWh  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_wh2 import DayOfferVectorEuroMWh2  # noqa: E501
from swagger_server.models.flex_offer_dlm_ps_item import FlexOfferDLMPsItem
from swagger_server.models.flex_offer_qlm_ps_item import FlexOfferQLMPsItem
from swagger_server.models.price_in_euro import PriceInEuro  # noqa: E501
from stacked_revenues.maximize_stacked_revenues import battery_portfolio
from swagger_server.adapters.market_adapter import MarketAdapter
from datetime import datetime, timedelta


def stacked_revenues_adapter(stacked_revenues_params):
    assert isinstance(stacked_revenues_params, StackedRevenuesParams)

    ns = len(stacked_revenues_params.storage_units)
    print(f"We got {ns} batteries")

    martketAdapter = MarketAdapter(
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()),
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()) +
        timedelta(days=1) - timedelta(minutes=1))

    dam_participation = 1
    rm_participation = 0
    fm_participation = 0
    bm_participation = 1

    dam_prices = [obj['value'] for obj in martketAdapter.day_ahead_market()]
    print(f"dam_prices= {len(dam_prices)}")
    rup_prices = [obj['value']
                    for obj in martketAdapter.reserve_market()]
    rdn_prices = [obj['value']
                    for obj in martketAdapter.reserve_market()]

    fmp_prices = [[0] * len(dam_prices)] * ns
    fmq_prices = [[0] * len(dam_prices)] * ns
    bm_up_prices = [obj['value']
                    for obj in martketAdapter.balancing_market_up()]
    print(f"bm_up_prices= {len(bm_up_prices)}")

    bm_dn_prices = [obj['value']
                    for obj in martketAdapter.balancing_market_down()]
    print(f"bm_dn_prices= {len(bm_dn_prices)}")

    p_max = [obj.power_capacity_kw for obj in stacked_revenues_params.storage_units]
    print(f"p_max= {p_max}")

    E_max = [obj.energy_capacity_k_wh for obj in stacked_revenues_params.storage_units]
    print(f"E_max= {E_max}")

    roundtrip_eff = [
        obj.inefficiency_rate_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"roundtrip_eff= {roundtrip_eff}")

    E0 = [obj.initial_final_so_c_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"E0= {E0}")

    # Create a battery object
    bsu = battery_portfolio(ns, dam_participation, rm_participation, fm_participation, bm_participation, dam_prices,
                            rup_prices, rdn_prices, fmp_prices, fmq_prices, bm_up_prices, bm_dn_prices,
                            p_max, E_max, roundtrip_eff, E0)

    # Maximize stacked revenues
    [Profits, pup, pdn, dam_schedule, rup_commitment, rdn_commitment, pflexibility, qflexibility,
        soc, DAM_profits, RM_profits, FM_profits, BM_profits] = bsu.maximize_stacked_revenues()

    print(f"\nProfits= {Profits},\n\n"
          f"pup = {pup},\n\n"
          f"pdn = {pdn},\n\n"
          f"dam_schedule = {dam_schedule},\n\n"
          f"rup_commitment = {rup_commitment},\n\n"
          f"rdn_commitment = {rdn_commitment},\n\n"
          f"pflexibility = {pflexibility},\n\n"
          f"qflexibility = {qflexibility},\n\n"
          f"soc = {soc},\n\n"
          f"DAM_profits = {DAM_profits},\n\n"
          f"RM_profits = {RM_profits},\n\n"
          f"FM_profits = {FM_profits},\n\n"
          f"BM_profits = {BM_profits}\n")

    return StackedRevenuesResult.from_dict({
        "sdate": str(stacked_revenues_params.sdate),
        "flex_offer": {
            "day_ahead_market_offer": build_market_offer(dam_prices, dam_schedule).to_dict(),
            "reserve_market_offer_up": build_reserve_market_offer(rup_prices, rup_commitment).to_dict(),
            "reserve_market_offer_down": build_reserve_market_offer(rdn_prices, rdn_commitment).to_dict(),
            "d-LMPs":  build_dflex_market_offer(fmp_prices, pflexibility, stacked_revenues_params.storage_units),
            "q-LMPs": build_qflex_market_offer(fmq_prices, qflexibility, stacked_revenues_params.storage_units),
            "balancing_market_offer_up": build_market_offer(bm_up_prices, pup).to_dict(),
            "balancing_market_offer_down": build_market_offer(bm_dn_prices, pdn).to_dict()
        },
        "revenues": {
            "day_ahead_market_revenues": build_profits(DAM_profits).to_dict(),
            "reserve_market_revenues": build_profits(RM_profits).to_dict(),
            "flexibility_market_revenues": build_profits(FM_profits).to_dict(),
            "balancing_market_revenues": build_profits(BM_profits).to_dict(),
        }
    })


def build_market_offer(prices, schedule):
    return DayOfferVectorEuroMWh.from_dict({
        "values": [{
            "price": prices[i],
            "volume": sum(schedule[j][i] for j in range(len(schedule)))
        } for i in range(len(prices))],
        "price_unit": "€/MWh",
        "volume_unit": "MWh"
    })


def build_reserve_market_offer(prices, schedule):
    return DayOfferVectorEuroMWh2.from_dict({
        "values": [{
            "price": prices[i],
            "volume": sum(schedule[j][i] for j in range(len(schedule)))
        } for i in range(len(prices))],
        "price_unit": "€/MWh^2",
        "volume_unit": "MWh^2"
    })


def build_dflex_market_offer(prices, schedule, storage_units):
    print(f"The price is {prices}, the scedule is {schedule}")
    return [
        FlexOfferDLMPsItem.from_dict({
            'price_unit': "€/MWh",
            'storage_unit': i,
            'values': [{
                "price": prices[i][j],
                "volume": schedule[i][j],
            } for j in range(len(schedule[i]))],
            'volume_unit': "MWh",
        }) for i in range(len(storage_units))]


def build_qflex_market_offer(prices, schedule, storage_units):
    print(f"The price is {prices}, the scedule is {schedule}")
    return [
        FlexOfferQLMPsItem.from_dict({
            'price_unit': "€/MVar",
            'storage_unit': i,
            'values': [{
                "price": prices[i][j],
                "volume": schedule[i][j],
            } for j in range(len(schedule[i]))],
            'volume_unit': "MVar",
        }) for i in range(len(storage_units))]


def build_profits(price):
    return PriceInEuro.from_dict({'value': price, 'currency': '€'})
