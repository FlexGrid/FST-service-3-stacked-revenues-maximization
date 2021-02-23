import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder

import responses
import re
import json
from datetime import datetime, timedelta
import math
import random


class BaseTestCase(TestCase):

    def setUp(self):
        def flexgrid_callback(request):
            if (
                request.params['token'] == '1234' and
                request.params['resource'] == 'atp' and
                request.params['method'] == 'post'
            ):
                return (200, {}, 'OK')
            else:
                return (401, {}, 'ERROR')

        responses.add_callback(responses.GET, 'https://db.flexgrid-project.eu/authorization/',
                               callback=flexgrid_callback)

        def fingrid_callback(request):
            start_time = datetime.fromisoformat(
                request.params["start_time"].replace("Z", "+00:00"))
            end_time = datetime.fromisoformat(
                request.params["end_time"].replace("Z", "+00:00"))
            hours = math.ceil(((end_time - start_time).seconds + 1) / 3600.0)
            resp_body = [{
                "value": random.uniform(0, 50),
                "start_time": (start_time + timedelta(hours=hours)).isoformat(),
                "end_time": (end_time + timedelta(hours=hours + 1)).isoformat(),
            } for i in range(hours)]
            return (200, {}, json.dumps(resp_body))

        responses.add_callback(
            responses.GET, re.compile(
                'https://api.fingrid.fi/v1/variable/(79|244|106)/events/json'),
            callback=fingrid_callback,
        )

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
