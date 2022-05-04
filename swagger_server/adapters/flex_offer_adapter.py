import json
from sqlite3 import Timestamp
from flask import abort, url_for
from swagger_server.models.flex_offer_params import FlexOfferParams
from swagger_server.models.flex_offer_result import FlexOfferResult
from swagger_server.adapters.central_db_adapter import CentralDBAdapter
import math


def post_flex_offers_adapter(flex_offer_params):
    assert isinstance(flex_offer_params, FlexOfferParams)

    print(f"The object is {flex_offer_params}")

    result = run_algorithm(flex_offer_params)

    return FlexOfferResult.from_dict(result)


def run_algorithm(flex_offer_params):

    # prosumers = []
    # for i in range(10):
    #     prosumers += [ f'user_{i+1}_Low', f'user_{i+1}_Medium', f'user_{i+1}_High']

    db_adapter = CentralDBAdapter()
    flex_offer_data = [db_adapter.get_flex_offer(fo,
                                                 flex_offer_params.start_datetime, flex_offer_params.end_datetime)
                       for fo in flex_offer_params.flex_offers]

    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA", len(flex_offer_data))
    # print(json.dumps(flex_offer_data, indent=4, sort_keys=True))

    if len(flex_offer_data) != len(flex_offer_params.flex_offers):
        # raise  ValueError("Missing prosumer")
        abort(500, description="Missing data for at least one flex_offer in centrail db")

    flex_request_data = db_adapter.get_flex_request(flex_offer_params.flex_request,
                                                    flex_offer_params.start_datetime, flex_offer_params.end_datetime)

    print(json.dumps(flex_request_data, indent=4, sort_keys=True))

    aggregate = merge_flex_offers(
        flex_offer_data, flex_request_data['location']['name'], flex_request_data['time_granurality_sec'])

    return {'aggr_flex_offer': aggregate, 'expected_result': clear_market(aggregate, flex_request_data)}


def merge_flex_offers(flex_offers, location_name, time_granurality_sec):

    flex_offers = [fo for fo in flex_offers if (fo['country'] ==
                   location_name or fo['location']['name'] == location_name) and
                   fo['time_granurality_sec'] == time_granurality_sec]

    if len(flex_offers) == 0:
        abort(
            500, description=f"No flex_offers match location {location_name} at granularity {time_granurality_sec} sec")

    aggregate = {
        'name': 'aggregate_fo',
        'country': flex_offers[0]['country'],
        'location': {'name': location_name},
        'data_points': [],
    }

    merge_hash = {}
    for fo in flex_offers:
        for dp in fo['data_points']:
            if dp['timestamp'] not in merge_hash:
                merge_hash[dp['timestamp']] = {}

            for f in dp['flexibility']:
                if (f['price_euro_per_kw'], f['direction'], f['minquantity']) not in merge_hash[dp['timestamp']]:
                    merge_hash[dp['timestamp']][(
                        f['price_euro_per_kw'], f['direction'], f['minquantity'])] = 0
                merge_hash[dp['timestamp']][(
                    f['price_euro_per_kw'], f['direction'], f['minquantity'])] += f['quantity_kw']

    for timestamp, data_point in merge_hash.items():
        aggregate['data_points'] += sorted([{
            'timestamp': timestamp,
            'flexibility': sorted([{
                "direction": d,
                "minquantity": m,
                "price_euro_per_kw": p,
                "quantity_kw": q

            } for (p, d, m), q in data_point.items()], key=lambda x: x['price_euro_per_kw'])
        }], key=lambda x: x['timestamp'])

    print(json.dumps(aggregate, indent=4, sort_keys=True))

    return aggregate


def clear_market(flex_offer, flex_request):

    result = []
    for fr_dp in flex_request['data_points']:
        for fo_dp in flex_offer['data_points']:
            if fr_dp['timestamp'] != fo_dp['timestamp']:
                continue

            aggr_r = {}
            sum_r = {}
            aggr_o = {}
            sum_o = {}
            for dir in ['Up', 'Down']:
                print("timestamp  = ", fr_dp['timestamp'], " direction ", dir)
                aggr_r[dir] = {}
                sum_r[dir] = 0
                for fr_fl in sorted(fr_dp['flexibility'], key=lambda x: x['price_euro_per_kw'], reverse=True):
                    if fr_fl['direction'] == dir:
                        sum_r[dir] += fr_fl['quantity_kw']
                        price = fr_fl['price_euro_per_kw']
                        if price not in aggr_r[dir]:
                            aggr_r[dir][price] = 0
                        aggr_r[dir][price] = sum_r[dir]

                aggr_o[dir] = {}
                sum_o[dir] = 0
                for fo_fl in sorted(fo_dp['flexibility'], key=lambda x: x['price_euro_per_kw'], reverse=False):
                    if fo_fl['direction'] == dir:
                        sum_o[dir] += fo_fl['quantity_kw']
                        price = fo_fl['price_euro_per_kw']
                        if price not in aggr_o[dir]:
                            aggr_o[dir][price] = 0
                        aggr_o[dir][price] = sum_o[dir]

                graph = sorted([
                    {
                        'volume': volume,
                        'type': 'R',
                        'price': price,
                    } for price, volume in aggr_r[dir].items()
                ] + [
                    {
                        'volume': volume,
                        'type': 'O',
                        'price': price,
                    } for price, volume in aggr_o[dir].items()
                ], key=lambda x: x['volume'])

                print(json.dumps(graph, indent=4, sort_keys=True))
                best = {
                    'R': {
                        'volume': 0,
                        'price': 0,
                    },
                    'O': {
                        'volume': 0,
                        'price': math.inf,
                    },
                }
                for row in graph:
                    if row['type'] == 'R':
                        if row['price'] > best['O']['price']:
                            break
                    if row['type'] == 'O':
                        if row['price'] < best['R']['price']:
                            break
                    best[row['type']] = {
                        'volume': row['volume'],
                        'price': row['price'],
                    }
                    print("row, ", row)
                    print("best,", best)
                result += [{
                    'timestamp': fr_dp['timestamp'],
                    'quantity_kw': min(best['O']['volume'], best['R']['volume']),
                    'direction': dir,
                    'price_euro_per_kw':  max(best['O']['price'], best['R']['price'])
                }]
    return [r for r in result if r["quantity_kw"] > 0]
