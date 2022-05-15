import base64
import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


class NordpoolAuthClient:

    token = {}
    # url = f"https://sts.nordpoolgroup.com/connect/token"

    def __init__(self):
        load_dotenv()

    def get_token(self):
        headers = {
            'Authorization': f"Basic {base64.b64encode('client_marketdata_api:client_marketdata_api'.encode('utf-8')).decode('utf-8')}",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # print(f"headers: {headers} user {os.environ.get('NORDPOOL_USERNAME')} pass {os.environ.get('NORDPOOL_PASSWORD')}")
        __class__.token = json.loads(
            requests.post(
                'https://sts.nordpoolgroup.com/connect/token',
                data={
                    'grant_type': 'password',
                    'scope': 'marketdata_api',
                    'username': os.environ.get("NORDPOOL_USERNAME"),
                    'password': os.environ.get("NORDPOOL_PASSWORD"),
                },
                headers=headers
            ).content)
        __class__.token['acquired_at'] = datetime.utcnow()

    def have_valid_token(self):
        return __class__.token and 'acquired_at' in __class__.token and 'expires_in' in __class__.token and (__class__.token['acquired_at'] + timedelta(seconds=__class__.token['expires_in'] - 30) > datetime.utcnow())

    def auth_headers(self):

        if not self.have_valid_token():
            self.get_token()

        return {'Ocp-Apim-Subscription-Key':  os.environ.get("NORDPOOL_SUBSCRIPTION_KEY"),
                'Authorization': f"Bearer {__class__.token['access_token']}"}
