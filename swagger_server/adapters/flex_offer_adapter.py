from swagger_server.models.flex_offer_params import FlexOfferParams


def flex_offer_adapter(flex_offer_params):
    assert isinstance(flex_offer_params, FlexOfferParams)

    print(f"The object is {flex_offer_params}")

    return merge_flex_offers(flex_offer_params)


def merge_offer_matrices(aggregate, offer):

    for item in offer:
        if not (item['start_timestamp'], item['end_timestamp']) in aggregate:
            aggregate[(item['start_timestamp'], item['end_timestamp'])] = {
                v.price: v.volume for v in item['values']}
        else:
            for v in item['values']:
                if not v['price'] in aggregate[(item['start_timestamp'], item['end_timestamp'])]:
                    aggregate[(item['start_timestamp'], item['end_timestamp'])
                              ][v['price']] = v['volume']
                else:
                    aggregate[(item['start_timestamp'], item['end_timestamp'])
                              ][v['price']] += v['volume']


def merge_flex_offers(flex_offer_params):
    flex_dict = {}

    for asset in flex_offer_params.flex_assets:
        location_id = asset.location.id

        if not location_id in flex_dict:
            flex_dict[location_id] = {
                'consumer_id': 'aggregator',
                'location': asset.location
            }

        if asset.reserve_market_offer_up:
            if 'reserve_market_offer_up' in flex_dict[location_id]:
                if asset.reserve_market_offer_up.price_unit != flex_dict[location_id]['reserve_market_offer_up']['price_unit']:
                    raise ValueError(
                        f"Price unit up missmatch in asset at {location_id}")

                if asset.reserve_market_offer_up.volume_unit != flex_dict[location_id]['reserve_market_offer_up']['volume_unit']:
                    raise ValueError(
                        f"Volume unit up missmatch in asset at {location_id}")

                merge_offer_matrices(
                    flex_dict[location_id]['reserve_market_offer_up']['values'], asset.reserve_market_offer_up.values)
            else:
                flex_dict[location_id]['reserve_market_offer_up'] = {
                    'price_unit': asset.reserve_market_offer_up.price_unit,
                    'volume_unit': asset.reserve_market_offer_up.volume_unit,
                    'values': {(val['start_timestamp'], val['end_timestamp']): {item['price']: item['volume'] for item in val['values']} for val in asset.reserve_market_offer_up.values}
                }

        if asset.reserve_market_offer_down:
            if 'reserve_market_offer_down' in flex_dict[location_id]:
                if asset.reserve_market_offer_down.price_unit != flex_dict[location_id]['reserve_market_offer_down']['price_unit']:
                    raise ValueError(
                        f"Price unit down missmatch in asset at {location_id}")

                if asset.reserve_market_offer_down.volume_unit != flex_dict[location_id]['reserve_market_offer_down']['volume_unit']:
                    raise ValueError(
                        f"Volume unit down missmatch in asset at {location_id}")

                merge_offer_matrices(
                    flex_dict[location_id]['reserve_market_offer_down']['values'], asset.reserve_market_offer_down.values)

            else:
                flex_dict[location_id]['reserve_market_offer_down'] = {
                    'price_unit': asset.reserve_market_offer_down.price_unit,
                    'volume_unit': asset.reserve_market_offer_down.volume_unit,
                    'values': {(val['start_timestamp'], val['end_timestamp']): {item['price']: item['volume'] for item in val['values']} for val in asset.reserve_market_offer_down.values}
                }

    for location_id in flex_dict:
        if 'reserve_market_offer_up' in flex_dict[location_id]:
            up_vals = [{
                'start_timestamp': start_time,
                'end_timestamp': end_time,
                'values': [{'price': price, 'volume': flex_dict[location_id]['reserve_market_offer_up']['values'][(start_time, end_time)][price]} for price in flex_dict[location_id]['reserve_market_offer_up']['values'][(start_time, end_time)]]
            } for (start_time, end_time) in flex_dict[location_id]['reserve_market_offer_up']['values']]
            flex_dict[location_id]['reserve_market_offer_up']['values'] = up_vals

        if 'reserve_market_offer_down' in flex_dict[location_id]:
            down_vals = [{
                'start_timestamp': start_time,
                'end_timestamp': end_time,
                'values': [{'price': price, 'volume': flex_dict[location_id]['reserve_market_offer_down']['values'][(start_time, end_time)][price]} for price in flex_dict[location_id]['reserve_market_offer_down']['values'][(start_time, end_time)]]
            } for (start_time, end_time) in flex_dict[location_id]['reserve_market_offer_down']['values']]
            flex_dict[location_id]['reserve_market_offer_down']['values'] = down_vals

    return flex_dict
