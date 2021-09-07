from swagger_server.models.flex_offer_params import FlexOfferParams


def flex_offer_adapter(flex_offer_params):
    assert isinstance(flex_offer_params, FlexOfferParams)

    print(f"The object is {flex_offer_params}")
    return {"ok": 1}
