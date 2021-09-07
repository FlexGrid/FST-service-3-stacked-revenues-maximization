# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.day_offer_matrix_euro_m_wh import DayOfferMatrixEuroMWh  # noqa: F401,E501
from swagger_server.models.location import Location  # noqa: F401,E501
from swagger_server import util


class FlexAsset(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, consumer_id: str=None, reserve_market_offer_up: DayOfferMatrixEuroMWh=None, reserve_market_offer_down: DayOfferMatrixEuroMWh=None, location: Location=None):  # noqa: E501
        """FlexAsset - a model defined in Swagger

        :param consumer_id: The consumer_id of this FlexAsset.  # noqa: E501
        :type consumer_id: str
        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexAsset.  # noqa: E501
        :type reserve_market_offer_up: DayOfferMatrixEuroMWh
        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexAsset.  # noqa: E501
        :type reserve_market_offer_down: DayOfferMatrixEuroMWh
        :param location: The location of this FlexAsset.  # noqa: E501
        :type location: Location
        """
        self.swagger_types = {
            'consumer_id': str,
            'reserve_market_offer_up': DayOfferMatrixEuroMWh,
            'reserve_market_offer_down': DayOfferMatrixEuroMWh,
            'location': Location
        }

        self.attribute_map = {
            'consumer_id': 'consumer_id',
            'reserve_market_offer_up': 'reserve_market_offer_up',
            'reserve_market_offer_down': 'reserve_market_offer_down',
            'location': 'location'
        }
        self._consumer_id = consumer_id
        self._reserve_market_offer_up = reserve_market_offer_up
        self._reserve_market_offer_down = reserve_market_offer_down
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'FlexAsset':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FlexAsset of this FlexAsset.  # noqa: E501
        :rtype: FlexAsset
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consumer_id(self) -> str:
        """Gets the consumer_id of this FlexAsset.


        :return: The consumer_id of this FlexAsset.
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id: str):
        """Sets the consumer_id of this FlexAsset.


        :param consumer_id: The consumer_id of this FlexAsset.
        :type consumer_id: str
        """
        if consumer_id is None:
            raise ValueError("Invalid value for `consumer_id`, must not be `None`")  # noqa: E501

        self._consumer_id = consumer_id

    @property
    def reserve_market_offer_up(self) -> DayOfferMatrixEuroMWh:
        """Gets the reserve_market_offer_up of this FlexAsset.


        :return: The reserve_market_offer_up of this FlexAsset.
        :rtype: DayOfferMatrixEuroMWh
        """
        return self._reserve_market_offer_up

    @reserve_market_offer_up.setter
    def reserve_market_offer_up(self, reserve_market_offer_up: DayOfferMatrixEuroMWh):
        """Sets the reserve_market_offer_up of this FlexAsset.


        :param reserve_market_offer_up: The reserve_market_offer_up of this FlexAsset.
        :type reserve_market_offer_up: DayOfferMatrixEuroMWh
        """

        self._reserve_market_offer_up = reserve_market_offer_up

    @property
    def reserve_market_offer_down(self) -> DayOfferMatrixEuroMWh:
        """Gets the reserve_market_offer_down of this FlexAsset.


        :return: The reserve_market_offer_down of this FlexAsset.
        :rtype: DayOfferMatrixEuroMWh
        """
        return self._reserve_market_offer_down

    @reserve_market_offer_down.setter
    def reserve_market_offer_down(self, reserve_market_offer_down: DayOfferMatrixEuroMWh):
        """Sets the reserve_market_offer_down of this FlexAsset.


        :param reserve_market_offer_down: The reserve_market_offer_down of this FlexAsset.
        :type reserve_market_offer_down: DayOfferMatrixEuroMWh
        """

        self._reserve_market_offer_down = reserve_market_offer_down

    @property
    def location(self) -> Location:
        """Gets the location of this FlexAsset.


        :return: The location of this FlexAsset.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location: Location):
        """Sets the location of this FlexAsset.


        :param location: The location of this FlexAsset.
        :type location: Location
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location
