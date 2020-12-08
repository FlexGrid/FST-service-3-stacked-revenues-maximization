import connexion
import six
import traceback
import logging

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
        try:
          body = [ScenarioParamsInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501

          result = [ScenarioResultInner.from_dict(
              {
                "date": str(p.sdate),
                "countries": [],
              }) for p in body]

          return result
        except Exception as e:
          logging.error(traceback.format_exc())
          return {'error_message': traceback.format_exc()}, 400

    return "Expecting JSON content type", 400

