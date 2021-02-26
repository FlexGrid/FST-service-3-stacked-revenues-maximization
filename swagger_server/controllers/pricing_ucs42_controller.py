import connexion
import six

from swagger_server.models.pricing_params import PricingParams  # noqa: E501
from swagger_server.models.pricing_result import PricingResult  # noqa: E501
from swagger_server import util


def pricing_post(body=None):  # noqa: E501
    """Creates an evaluation of various pricing mechanisms

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: PricingResult
    """
    if connexion.request.is_json:
        body = PricingParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
