import connexion
import six

from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server import util


def stacked_revenues_post(body=None):  # noqa: E501
    """Initiates a simulation scenario for Stacked Revenues maximization

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StackedRevenuesResult
    """
    if connexion.request.is_json:
        body = StackedRevenuesParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
