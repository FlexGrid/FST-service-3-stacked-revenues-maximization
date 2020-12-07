import connexion
import six

from swagger_server.models.scenario_params_inner import ScenarioParamsInner  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server import util
from swagger_server.models.scenario_result_inner import ScenarioResultInner  # noqa: E501



def scenarios_post(body):  # noqa: E501
    """Initiates a simulation scenario

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ScenarioResult
    """
    if connexion.request.is_json:
        body = [ScenarioParamsInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

        result = [ScenarioResultInner.from_dict(
            {
                "date": str(p.sdate),
                "countries": [],
            }) for p in body]

        return result

    return "Expecting JSON content type", 400

