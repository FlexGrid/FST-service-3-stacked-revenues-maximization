from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server.models.day_offer_vector_euro_m_wh import DayOfferVectorEuroMWh  # noqa: E501
from swagger_server.models.price_in_euro import PriceInEuro  # noqa: E501
from stacked_revenues.maximize_stacked_revenues import battery_portfolio
from swagger_server.adapters.market_adapter import MarketAdapter
from datetime import datetime, timedelta
import dateutil.parser


def stacked_revenues_adapter(stacked_revenues_params):
    assert isinstance(stacked_revenues_params, StackedRevenuesParams)

    ns = len(stacked_revenues_params.storage_units)
    print(f"We got {ns} batteries")

    martketAdapter = MarketAdapter(
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()),
        datetime.combine(stacked_revenues_params.sdate, datetime.min.time()) +
        timedelta(days=1) - timedelta(minutes=1))

    timestamps = [(
        (dateutil.parser.isoparse(martketAdapter.start_timestamp) +
         timedelta(hours=t)).strftime('%Y-%m-%dT%H:%M:%SZ'),
        (dateutil.parser.isoparse(martketAdapter.start_timestamp) +
         timedelta(hours=t+1)).strftime('%Y-%m-%dT%H:%M:%SZ'),
    ) for t in range(24)]

    print(f"min time {datetime.min.time()} timestamps= {timestamps}")

    dam_participation = "DAM" in stacked_revenues_params.markets
    rm_participation = "RM" in stacked_revenues_params.markets
    fm_participation = "FM" in stacked_revenues_params.markets
    bm_participation = "BM" in stacked_revenues_params.markets

    dam_prices = [obj['value'] for obj in martketAdapter.day_ahead_market()]
    print(f"dam_prices= {len(dam_prices)}")
    rup_prices = [obj['value']
                  for obj in martketAdapter.reserve_market()]
    print(f"rup_prices= {len(rup_prices)}")
    rdn_prices = [obj['value']
                  for obj in martketAdapter.reserve_market()]
    print(f"rdn_prices= {len(rdn_prices)}")

    fmp_prices = martketAdapter.fmp(
        [su.location.id for su in stacked_revenues_params.storage_units])
    fmq_prices = martketAdapter.fmq(
        [su.location.id for su in stacked_revenues_params.storage_units])
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

    E0 = [obj.initial_so_c_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"E0= {E0}")

    ET = [obj.final_so_c_per_cent for obj in stacked_revenues_params.storage_units]
    print(f"ET= {ET}")

    # Create a battery object
    bsu = battery_portfolio(ns, dam_participation, rm_participation, fm_participation, bm_participation, dam_prices,
                            rup_prices, rdn_prices, fmp_prices, fmq_prices, bm_up_prices, bm_dn_prices,
                            p_max, E_max, roundtrip_eff, E0, ET)

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
        "flex_offer": [{
            "location": stacked_revenues_params.storage_units[su_ind].location.id,
            "day_ahead_market_offer": build_market_offer_mwh(timestamps, dam_schedule[su_ind]),
            "reserve_market_offer_up": build_market_offer_mwh(timestamps, rup_commitment[su_ind]),
            "reserve_market_offer_down": build_market_offer_mwh(timestamps, rdn_commitment[su_ind]),
            "d-LMPs":  build_market_offer_mwh(timestamps, pflexibility[su_ind]),
            "q-LMPs": build_market_offer_mvar(timestamps, qflexibility[su_ind]),
            "balancing_market_offer_up": build_market_offer_mwh(timestamps, pup[su_ind]),
            "balancing_market_offer_down": build_market_offer_mwh(timestamps, pdn[su_ind])
        } for su_ind in range(len(stacked_revenues_params.storage_units))],
        "revenues": {
            "day_ahead_market_revenues": build_profits(DAM_profits).to_dict(),
            "reserve_market_revenues": build_profits(RM_profits).to_dict(),
            "flexibility_market_revenues": build_profits(FM_profits).to_dict(),
            "balancing_market_revenues": build_profits(BM_profits).to_dict(),
        }
    })


def build_market_offer_mwh(timestamps, schedule):
    return {
        "values": [{
            "start_timestamp": timestamps[i][0],
            "end_timestamp": timestamps[i][1],
            "volume": round(schedule[i], 2),
        } for i in range(len(timestamps))],
        "price_unit": "€/MWh",
        "volume_unit": "kWh"
    }


def build_market_offer_mvar(timestamps, schedule):
    return {
        "values": [{
            "start_timestamp": timestamps[i][0],
            "end_timestamp": timestamps[i][1],
            "volume": round(schedule[i], 2),
        } for i in range(len(timestamps))],
        "price_unit": "€/MVar",
        "volume_unit": "kVar"
    }


def build_profits(price):
    return PriceInEuro.from_dict({'value': price, 'currency': '€'})
