import connexion
import six

from swagger_server.models.job_submitted import JobSubmitted  # noqa: E501
from swagger_server.models.pricing_job_result import PricingJobResult  # noqa: E501
from swagger_server.models.pricing_params import PricingParams  # noqa: E501
from swagger_server.adapters.pricing_adapter import get_pricing_adapter, post_pricing_adapter
from swagger_server import util

import traceback
from werkzeug.exceptions import HTTPException
from flask import abort

def pricing_get(job_id):  # noqa: E501
    """Retrieves information about a pricing job

     # noqa: E501

    :param job_id: The job ID
    :type job_id: str

    :rtype: PricingJobResult
    """
    try:
        result = get_pricing_adapter(job_id)
        return result
    except HTTPException as e:
        raise(e)
    except Exception as e:
        abort(500, description=traceback.format_exc())


def pricing_post(body=None):  # noqa: E501
    """Creates an evaluation of various pricing mechanisms

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: JobSubmitted
    """
    if connexion.request.is_json:
        try:
            body = PricingParams.from_dict(connexion.request.get_json())  # noqa: E501
            result = post_pricing_adapter(body)
            return result
        except HTTPException as e:
            raise(e)
        except Exception as e:
            abort(500, description=traceback.format_exc())

    return "Expecting JSON content type", 400
