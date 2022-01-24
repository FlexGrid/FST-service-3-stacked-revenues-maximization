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

    This query is used for obtaining the simulation results that have been posted by the request defined at [https://pricing-api.flexgrid-project.eu/swagger/#/Pricing (UCS 4.2)/pricing_post](https://pricing-api.flexgrid-project.eu/swagger/#/Pricing%20(UCS%204.2)/pricing_post)  The &#x60;job_id&#x60; URL parameter is returned from the above mentioned request  # noqa: E501
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

    This endpoint is for submitting a simulation for pricing mechanisms  The &#x60;dr_prosumers&#x60; field contains the &#x60;name&#x60; fields of the &#x60;dr_prosumers&#x60; that will be simulated. To obtain the names use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getdr_prosumers](https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getdr_prosumers)  The &#x60;flex_request&#x60; field contains the &#x60;name&#x60; field of the &#x60;flex_request&#x60; that will be simulated. To obtain the name use the central DB api defined here: [https://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests](hhttps://db.flexgrid-project.eu/swagger/#/Flex_request/getflex_requests)  If the &#x60;callback&#x60; object is defined, the simulation results will be posted at the URL that is defined in it, with the request body encoded as JSON, with the structure defined as &#x60;PricingData&#x60; in this document. You may also pass HTTP headers that will be used for the callback post. The HTTP method used will be &#x60;POST&#x60;.  It returns the &#x60;job_id&#x60;, which can be used to query for the results, with the request defined at [https://pricing-api.flexgrid-project.eu/swagger/#/Pricing (UCS 4.2)/pricing_get](https://pricing-api.flexgrid-project.eu/swagger/#/Pricing%20(UCS%204.2)/pricing_get)  # noqa: E501

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
