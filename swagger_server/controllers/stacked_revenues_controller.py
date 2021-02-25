import connexion
import six

from swagger_server.models.stacked_revenues_params import StackedRevenuesParams  # noqa: E501
from swagger_server.models.stacked_revenues_result import StackedRevenuesResult  # noqa: E501
from swagger_server import util
from swagger_server.adapters.stacked_revenues_adapter import stacked_revenues_adapter

import logging
import traceback

def stacked_revenues_post(body):  # noqa: E501
    """Initiates a simulation scenario for Stacked Revenues maximization

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: StackedRevenuesResult
    """
    if connexion.request.is_json:
        try:
            body = StackedRevenuesParams.from_dict(connexion.request.get_json())  # noqa: E501
    
            result = stacked_revenues_adapter(body)

            return result
        except Exception as e:
            logging.error(traceback.format_exc())
            return {'error_message': traceback.format_exc()}, 400

    return "Expecting JSON content type", 400
