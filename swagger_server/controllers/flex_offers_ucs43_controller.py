import connexion
import six

from swagger_server.models.flex_offer_params import FlexOfferParams  # noqa: E501
from swagger_server.models.flex_offer_result import FlexOfferResult  # noqa: E501
from swagger_server import util


def flex_offers_post(body=None):  # noqa: E501
    """Creates a Flexibility Offser (FlexOffer) based of FlexAssets

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: FlexOfferResult
    """
    if connexion.request.is_json:
        body = FlexOfferParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
