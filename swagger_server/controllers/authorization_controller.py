from typing import List
import requests
import os

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_oAuth2(token):
    if not os.environ.get("SAMPLE_DATA"):
        auth = requests.get('https://db.flexgrid-project.eu/authorization/', params={
            'token': token,
            'resource': 'atp',
            'method': 'post',
        }).content
        print("auth", )
        if auth != b"OK":
            return None
    return {'scopes': ['post_flex_offers'], 'uid': 'test_value'}

def validate_scope_oAuth2(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))


