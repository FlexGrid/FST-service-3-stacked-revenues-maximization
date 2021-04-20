# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase
from swagger_server.adapters.nordpool_auth_client import NordpoolAuthClient
import responses


class TestNordpoolAuthClient(BaseTestCase):
    """NordpoolAuthClientAdapter integration test stubs"""

    def __init__(self, args):
        super().__init__(args)

    @responses.activate
    def test_run(self):
        """Test case for stacked_revenues_post

        Initiates a simulation scenario
        """

        token1 = NordpoolAuthClient().auth_headers()['Authorization']
        token2 = NordpoolAuthClient().auth_headers()['Authorization']

        assert token1 == token2
        assert len(token1) == 1332

if __name__ == '__main__':
    import unittest
    unittest.main()
