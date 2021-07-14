from typing import List
import requests
import os

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_MyTokenAuth(token):
    if not os.environ.get("SAMPLE_DATA"):
        auth = requests.get('https://db.flexgrid-project.eu/authorization/', params={
            'token': token,
            'resource': 'atp',
            'method': 'post',
        }).content
        if auth != b"OK":
            return None
    return {'scopes': ['read:pets', 'write:pets'], 'uid': 'test_value'}

def validate_scope_MyTokenAuth(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))


