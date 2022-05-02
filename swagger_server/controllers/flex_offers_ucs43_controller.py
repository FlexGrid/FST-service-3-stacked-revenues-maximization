import connexion
import six

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server import util


def flex_offers_post(body=None):  # noqa: E501
    """Aggragates several Flex offers into a single offer

    This endpoint is for aggregating flex offers  The &#x60;flex_offers&#x60; field contains the &#x60;name&#x60; fields of the &#x60;flex_offers&#x60; that will be aggregated. To obtain the names use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getflex_offers](https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getflex_offers)  The &#x60;flex_request&#x60; field contains the &#x60;name&#x60; field of the &#x60;flex_request&#x60; that will be used for calculating the resulting revenues and quantities. To obtain the name use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests](hhttps://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests)  It returns the an aggregated offer, and the expected cleance quantities and prices   # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: FlexOfferResult
    """
    if connexion.request.is_json:
        body = FlexOfferParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
