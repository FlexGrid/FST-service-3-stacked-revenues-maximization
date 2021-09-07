import connexion
import six

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server import util
from swagger_server.adapters.flex_offer_adapter import flex_offer_adapter

import logging
import traceback


def flex_offers_post(body):  # noqa: E501
    """Creates a Flexibility Offser (FlexOffer) based of FlexAssets

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: FlexOfferResult
    """
    if connexion.request.is_json:
        try:
            body = FlexOfferParams.from_dict(connexion.request.get_json())  # noqa: E501

            result = flex_offer_adapter(body)

            return result
        except Exception as e:
            logging.error(traceback.format_exc())
            return {'error_message': traceback.format_exc()}, 400

    return "Expecting JSON content type", 400
