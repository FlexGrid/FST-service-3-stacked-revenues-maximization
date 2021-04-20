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

        def nordpool_auth_callback(request):
            resp_body = {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik5CdWg4VFhkY0gzOHN0TzNaTjV3MmQtdU8zOCIsImtpZCI6Ik5CdWg4VFhkY0gzOHN0TzNaTjV3MmQtdU8zOCJ9.eyJpc3MiOiJodHRwczovL3Nzby5ub3JkcG9vbGdyb3VwLmNvbSIsImF1ZCI6Imh0dHBzOi8vc3NvLm5vcmRwb29sZ3JvdXAuY29tL3Jlc291cmNlcyIsImV4cCI6MTYxODkyODg0MCwibmJmIjoxNjE4OTI1MjQwLCJjbGllbnRfaWQiOiJjbGllbnRfbWFya2V0ZGF0YV9hcGkiLCJzY29wZSI6Im1hcmtldGRhdGFfYXBpIiwic3ViIjoiOWIxMjc2M2UtOTdjMi00MzIyLTk5ODMtM2ZmMGM5ODVmZWU0IiwiYXV0aF90aW1lIjoxNjE4OTI1MjQwLCJpZHAiOiJpZHNydiIsInByZWZlcnJlZF91c2VybmFtZSI6IkFQSV9EQVRBX0ZMRVhHUklEIiwiYXBwbGljYXRpb25fc3Vic2NyaXB0aW9uIjoibWFya2V0ZGF0YV9hcGlfbm9yZGljYmFsdGljIiwiYW1yIjpbInBhc3N3b3JkIl19.utBY6Gmu5lRzyRnovOlQhdVZ17H9z_MCfCotomVJ4J5vRDndqZFHx7UONI8Xkg3YSxIeIK2dwfbdXNVvD11-wKN1X05x7wJ75Ln08YtB3T5wUHYrX5GYxcP2HlPbjHaw5W_575CcxKqGDJfcz22X2XR9_G1_c5NnCRoP-pVjFdMGNwoStgvEv5rMQrlNDEdMn1hoBUuizOHtTVeymyReQTR7L9OKKl7dRrBhlz8v6KkkZmLPXZq223iASQIJ5hX2QIPdqXxnz1LnaZa5flQp7bDGhY5jdlm5Q9nqu4jzk1e0dFoheEuZSKEnDOjeXrjerqA8to3KC7mnpQoNuk-Z34s9hWCUaMzqTfdSl-ubZeWdZOaoH-rS1d62jggki-BwIwwOkSqsQNQYXzEmEDy1bILDBgBiBlRB511LA6rCyThEb3Z8mu0dACYnnfrwK9qmbtJy6XNGBP_X3MPp1optVuUrP7HDhlElshJxHoP0lr2MFsQUywtpTajDoxQISJlKsVpSXb1qeyJrEiphT2yq1CQZk62OdvAyxrfbBekObPhQaJ8W1KhZkKUgsnpPGq18AyKH5175E1NEelnOxT2i-WX8FjlRr3-Rhb7z-QL2sJiA8Wlcd7RHPP96azXEmeHkoHs-1rUOcfRVwQ03oJqtiTYUJ37gX1OnT5b9LpyDxkY",
                "expires_in": 3600,
                "token_type": "Bearer"
            }

            return (200, {}, json.dumps(resp_body))

        responses.add_callback(
            responses.POST, re.compile(
                'https://sts.nordpoolgroup.com/connect/token'),
            callback=nordpool_auth_callback,
        )

        def nordpool_callback(request):
            # print(f"The params are {request.params}")
            start_time = datetime.fromisoformat(
                request.params["startTime"].replace("Z", "+00:00"))
            end_time = datetime.fromisoformat(
                request.params["endTime"].replace("Z", "+00:00"))
            hours = math.ceil(
                ((end_time - start_time - timedelta(hours=1)).seconds + 1) / 3600.0)
            resp_body = [
                {
                    "category": "dayAhead",
                    "createdTime": 1601462571635,
                    "type": "price",
                    "SubType": "area",
                    "resolution": "PT1H",
                    "unit": "EUR/MWh",
                    "scale": 2,
                    "startTime": "2020-10-15T21:00:00Z",
                    "endTime": "2020-10-16T21:00:00Z",
                    "values": [{
                            "value": random.uniform(0, 50),
                            "startTime": (start_time + timedelta(hours=hours)).isoformat(),
                            "endTime": (end_time + timedelta(hours=hours + 1)).isoformat(),
                    } for i in range(hours)],
                    "attributes": [
                        {
                            "role": None,
                            "name": "deliveryArea",
                            "value": "FI"
                        },
                        {
                            "role": None,
                            "name": "status",
                            "value": "O"
                        },
                        {
                            "role": None,
                            "name": "currency",
                            "value": "EUR"
                        }
                    ]
                }
            ]
            return (200, {}, json.dumps(resp_body))

        responses.add_callback(
            responses.GET, re.compile(
                'https://marketdata-api.nordpoolgroup.com/dayahead/prices/area'),
            callback=nordpool_callback,
        )

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
