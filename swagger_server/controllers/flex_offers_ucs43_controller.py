import connexion
import six

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server.adapters.flex_offer_adapter import post_flex_offers_adapter
from swagger_server import util

import traceback
from werkzeug.exceptions import HTTPException
from flask import abort


def flex_offers_post(body=None):  # noqa: E501
    """Aggragates several Flex offers into a single offer

    This endpoint is for aggregating flex offers  The &#x60;flex_offers&#x60; field contains the &#x60;name&#x60; fields of the &#x60;flex_offers&#x60; that will be aggregated. To obtain the names use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getflex_offers](https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getflex_offers)  The &#x60;flex_request&#x60; field contains the &#x60;name&#x60; field of the &#x60;flex_request&#x60; that will be used for calculating the resulting revenues and quantities. To obtain the name use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests](hhttps://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests)  It returns the an aggregated offer, and the expected cleance quantities and prices   # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: FlexOfferResult
    """
    if connexion.request.is_json:
        try:
            body = FlexOfferParams.from_dict(connexion.request.get_json())  # noqa: E501
            result = post_flex_offers_adapter(body)
            return result
        except HTTPException as e:
            raise(e)
        except Exception as e:
            abort(500, description=traceback.format_exc())

    return "Expecting JSON content type", 400
