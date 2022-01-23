import connexion
import six

from swagger_server.models.job_submitted import JobSubmitted  # noqa: E501
from swagger_server.models.pricing_job_result import PricingJobResult  # noqa: E501
from swagger_server.models.pricing_params import PricingParams  # noqa: E501
from swagger_server import util


def pricing_get(job_id):  # noqa: E501
    """Retrieves information about a pricing job

     # noqa: E501

    :param job_id: The job ID
    :type job_id: str

    :rtype: PricingJobResult
    """
    return 'do some magic!'


def pricing_post(body=None):  # noqa: E501
    """Creates an evaluation of various pricing mechanisms

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: JobSubmitted
    """
    if connexion.request.is_json:
        body = PricingParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
