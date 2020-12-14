import connexion
import six
import traceback
import logging

from swagger_server.models.scenario_params import ScenarioParams  # noqa: E501
from swagger_server.models.scenario_result import ScenarioResult  # noqa: E501
from swagger_server import util


def scenarios_post(body):  # noqa: E501
    """Initiates a simulation scenario

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ScenarioResult
    """
    if connexion.request.is_json:
        try:
            body = ScenarioParams.from_dict(connexion.request.get_json())  # noqa: E501

            result = ScenarioResult.from_dict({
                "sdate": str(body.sdate),
                "flex_offer": {
                    "day_ahead_market_offer": {
                        "values": [
                            {
                                "price": 0,
                                "volume": 0
                            }
                        ],
                        "price_unit": "€/MWh",
                        "volume_unit": "MWh"
                    },
                    "reserve_market_offer": {
                        "values": [
                            {
                                "price": 0,
                                "volume": 0
                            }
                        ],
                        "price_unit": "(€/MWh)^2",
                        "volume_unit": "MWh^2"
                    },
                    "d-LMPs": {
                        "values": [
                            {
                                "price": 0,
                                "volume": 0
                            }
                        ],
                        "price_unit": "€/MWh",
                        "volume_unit": "MWh"
                    },
                    "q-LMPs": {
                        "values": [
                            {
                                "price": 0,
                                "volume": 0
                            }
                        ],
                        "price_unit": "€/MVar",
                        "volume_unit": "MVar"
                    },
                    "balancing_market_offer": {
                        "values": [
                            {
                                "price": 0,
                                "volume": 0
                            }
                        ],
                        "price_unit": "€/MWh",
                        "volume_unit": "MWh"
                    }
                },
                "revenues": {
                    "day_ahead_market_revenues": {
                        "values": [
                            {"volume": 113.3, "price": 23.13},
                            {"volume": 12.4, "price": 23.13},
                            {"volume": 5.5, "price": 23.13},
                            {"volume": 225.3, "price": 23.13},
                            {"volume": 2.6, "price": 23.13},
                            {"volume": 21.1, "price": 23.13},
                            {"volume": 21, "price": 23.13},
                            {"volume": 24.9, "price": 23.13},
                            {"volume": 24.2, "price": 23.13},
                            {"volume": 1.45, "price": 23.13},
                            {"volume": 15.4, "price": 23.13},
                            {"volume": 15.2, "price": 23.13},
                            {"volume": 15.1, "price": 23.13},
                            {"volume": 1.45, "price": 23.13},
                            {"volume": 5.54, "price": 23.13},
                            {"volume": 5.34, "price": 23.13},
                            {"volume": 6.45, "price": 23.13},
                            {"volume": 8.45, "price": 23.13},
                            {"volume": 8.45, "price": 23.13},
                            {"volume": 3.34, "price": 23.13},
                            {"volume": 1.34, "price": 23.13},
                            {"volume": 2.45, "price": 23.13},
                            {"volume": 7.14, "price": 23.13},
                            {"volume": 9.53, "price": 23.13},
                        ],
                        "currency": "€"
                    }
                }
            })

            return result
        except Exception as e:
            logging.error(traceback.format_exc())
            return {'error_message': traceback.format_exc()}, 400

    return "Expecting JSON content type", 400
