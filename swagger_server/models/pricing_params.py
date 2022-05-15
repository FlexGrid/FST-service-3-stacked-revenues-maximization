# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.pricing_params_curtailable_loads import PricingParamsCurtailableLoads  # noqa: F401,E501
from swagger_server.models.pricing_params_flex_assets import PricingParamsFlexAssets  # noqa: F401,E501
from swagger_server.models.pricing_params_flex_contracts import PricingParamsFlexContracts  # noqa: F401,E501
from swagger_server.models.pricing_params_time_granularity import PricingParamsTimeGranularity  # noqa: F401,E501
from swagger_server.models.storage_unit import StorageUnit  # noqa: F401,E501
from swagger_server import util


class PricingParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, country: str=None, start_datetime: datetime=None, end_datetime: datetime=None, time_granularity: PricingParamsTimeGranularity=None, dr_prosumers: List[str]=None, flex_request: str=None, gamma_values: List[float]=None, profit_margin: float=None, flex_assets: List[PricingParamsFlexAssets]=None, storage_units: List[StorageUnit]=None, curtailable_loads: List[PricingParamsCurtailableLoads]=None, flex_contracts: List[PricingParamsFlexContracts]=None, store_data: bool=None):  # noqa: E501
        """PricingParams - a model defined in Swagger

        :param country: The country of this PricingParams.  # noqa: E501
        :type country: str
        :param start_datetime: The start_datetime of this PricingParams.  # noqa: E501
        :type start_datetime: datetime
        :param end_datetime: The end_datetime of this PricingParams.  # noqa: E501
        :type end_datetime: datetime
        :param time_granularity: The time_granularity of this PricingParams.  # noqa: E501
        :type time_granularity: PricingParamsTimeGranularity
        :param dr_prosumers: The dr_prosumers of this PricingParams.  # noqa: E501
        :type dr_prosumers: List[str]
        :param flex_request: The flex_request of this PricingParams.  # noqa: E501
        :type flex_request: str
        :param gamma_values: The gamma_values of this PricingParams.  # noqa: E501
        :type gamma_values: List[float]
        :param profit_margin: The profit_margin of this PricingParams.  # noqa: E501
        :type profit_margin: float
        :param flex_assets: The flex_assets of this PricingParams.  # noqa: E501
        :type flex_assets: List[PricingParamsFlexAssets]
        :param storage_units: The storage_units of this PricingParams.  # noqa: E501
        :type storage_units: List[StorageUnit]
        :param curtailable_loads: The curtailable_loads of this PricingParams.  # noqa: E501
        :type curtailable_loads: List[PricingParamsCurtailableLoads]
        :param flex_contracts: The flex_contracts of this PricingParams.  # noqa: E501
        :type flex_contracts: List[PricingParamsFlexContracts]
        :param store_data: The store_data of this PricingParams.  # noqa: E501
        :type store_data: bool
        """
        self.swagger_types = {
            'country': str,
            'start_datetime': datetime,
            'end_datetime': datetime,
            'time_granularity': PricingParamsTimeGranularity,
            'dr_prosumers': List[str],
            'flex_request': str,
            'gamma_values': List[float],
            'profit_margin': float,
            'flex_assets': List[PricingParamsFlexAssets],
            'storage_units': List[StorageUnit],
            'curtailable_loads': List[PricingParamsCurtailableLoads],
            'flex_contracts': List[PricingParamsFlexContracts],
            'store_data': bool
        }

        self.attribute_map = {
            'country': 'country',
            'start_datetime': 'start_datetime',
            'end_datetime': 'end_datetime',
            'time_granularity': 'time_granularity',
            'dr_prosumers': 'dr_prosumers',
            'flex_request': 'flex_request',
            'gamma_values': 'gamma_values',
            'profit_margin': 'profit_margin',
            'flex_assets': 'flex_assets',
            'storage_units': 'storage_units',
            'curtailable_loads': 'curtailable_loads',
            'flex_contracts': 'flex_contracts',
            'store_data': 'store_data'
        }
        self._country = country
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._time_granularity = time_granularity
        self._dr_prosumers = dr_prosumers
        self._flex_request = flex_request
        self._gamma_values = gamma_values
        self._profit_margin = profit_margin
        self._flex_assets = flex_assets
        self._storage_units = storage_units
        self._curtailable_loads = curtailable_loads
        self._flex_contracts = flex_contracts
        self._store_data = store_data

    @classmethod
    def from_dict(cls, dikt) -> 'PricingParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PricingParams of this PricingParams.  # noqa: E501
        :rtype: PricingParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country(self) -> str:
        """Gets the country of this PricingParams.


        :return: The country of this PricingParams.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this PricingParams.


        :param country: The country of this PricingParams.
        :type country: str
        """

        self._country = country

    @property
    def start_datetime(self) -> datetime:
        """Gets the start_datetime of this PricingParams.


        :return: The start_datetime of this PricingParams.
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime: datetime):
        """Sets the start_datetime of this PricingParams.


        :param start_datetime: The start_datetime of this PricingParams.
        :type start_datetime: datetime
        """
        if start_datetime is None:
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def end_datetime(self) -> datetime:
        """Gets the end_datetime of this PricingParams.


        :return: The end_datetime of this PricingParams.
        :rtype: datetime
        """
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, end_datetime: datetime):
        """Sets the end_datetime of this PricingParams.


        :param end_datetime: The end_datetime of this PricingParams.
        :type end_datetime: datetime
        """
        if end_datetime is None:
            raise ValueError("Invalid value for `end_datetime`, must not be `None`")  # noqa: E501

        self._end_datetime = end_datetime

    @property
    def time_granularity(self) -> PricingParamsTimeGranularity:
        """Gets the time_granularity of this PricingParams.


        :return: The time_granularity of this PricingParams.
        :rtype: PricingParamsTimeGranularity
        """
        return self._time_granularity

    @time_granularity.setter
    def time_granularity(self, time_granularity: PricingParamsTimeGranularity):
        """Sets the time_granularity of this PricingParams.


        :param time_granularity: The time_granularity of this PricingParams.
        :type time_granularity: PricingParamsTimeGranularity
        """

        self._time_granularity = time_granularity

    @property
    def dr_prosumers(self) -> List[str]:
        """Gets the dr_prosumers of this PricingParams.


        :return: The dr_prosumers of this PricingParams.
        :rtype: List[str]
        """
        return self._dr_prosumers

    @dr_prosumers.setter
    def dr_prosumers(self, dr_prosumers: List[str]):
        """Sets the dr_prosumers of this PricingParams.


        :param dr_prosumers: The dr_prosumers of this PricingParams.
        :type dr_prosumers: List[str]
        """
        if dr_prosumers is None:
            raise ValueError("Invalid value for `dr_prosumers`, must not be `None`")  # noqa: E501

        self._dr_prosumers = dr_prosumers

    @property
    def flex_request(self) -> str:
        """Gets the flex_request of this PricingParams.


        :return: The flex_request of this PricingParams.
        :rtype: str
        """
        return self._flex_request

    @flex_request.setter
    def flex_request(self, flex_request: str):
        """Sets the flex_request of this PricingParams.


        :param flex_request: The flex_request of this PricingParams.
        :type flex_request: str
        """
        if flex_request is None:
            raise ValueError("Invalid value for `flex_request`, must not be `None`")  # noqa: E501

        self._flex_request = flex_request

    @property
    def gamma_values(self) -> List[float]:
        """Gets the gamma_values of this PricingParams.


        :return: The gamma_values of this PricingParams.
        :rtype: List[float]
        """
        return self._gamma_values

    @gamma_values.setter
    def gamma_values(self, gamma_values: List[float]):
        """Sets the gamma_values of this PricingParams.


        :param gamma_values: The gamma_values of this PricingParams.
        :type gamma_values: List[float]
        """
        if gamma_values is None:
            raise ValueError("Invalid value for `gamma_values`, must not be `None`")  # noqa: E501

        self._gamma_values = gamma_values

    @property
    def profit_margin(self) -> float:
        """Gets the profit_margin of this PricingParams.


        :return: The profit_margin of this PricingParams.
        :rtype: float
        """
        return self._profit_margin

    @profit_margin.setter
    def profit_margin(self, profit_margin: float):
        """Sets the profit_margin of this PricingParams.


        :param profit_margin: The profit_margin of this PricingParams.
        :type profit_margin: float
        """
        if profit_margin is None:
            raise ValueError("Invalid value for `profit_margin`, must not be `None`")  # noqa: E501

        self._profit_margin = profit_margin

    @property
    def flex_assets(self) -> List[PricingParamsFlexAssets]:
        """Gets the flex_assets of this PricingParams.


        :return: The flex_assets of this PricingParams.
        :rtype: List[PricingParamsFlexAssets]
        """
        return self._flex_assets

    @flex_assets.setter
    def flex_assets(self, flex_assets: List[PricingParamsFlexAssets]):
        """Sets the flex_assets of this PricingParams.


        :param flex_assets: The flex_assets of this PricingParams.
        :type flex_assets: List[PricingParamsFlexAssets]
        """

        self._flex_assets = flex_assets

    @property
    def storage_units(self) -> List[StorageUnit]:
        """Gets the storage_units of this PricingParams.


        :return: The storage_units of this PricingParams.
        :rtype: List[StorageUnit]
        """
        return self._storage_units

    @storage_units.setter
    def storage_units(self, storage_units: List[StorageUnit]):
        """Sets the storage_units of this PricingParams.


        :param storage_units: The storage_units of this PricingParams.
        :type storage_units: List[StorageUnit]
        """

        self._storage_units = storage_units

    @property
    def curtailable_loads(self) -> List[PricingParamsCurtailableLoads]:
        """Gets the curtailable_loads of this PricingParams.


        :return: The curtailable_loads of this PricingParams.
        :rtype: List[PricingParamsCurtailableLoads]
        """
        return self._curtailable_loads

    @curtailable_loads.setter
    def curtailable_loads(self, curtailable_loads: List[PricingParamsCurtailableLoads]):
        """Sets the curtailable_loads of this PricingParams.


        :param curtailable_loads: The curtailable_loads of this PricingParams.
        :type curtailable_loads: List[PricingParamsCurtailableLoads]
        """

        self._curtailable_loads = curtailable_loads

    @property
    def flex_contracts(self) -> List[PricingParamsFlexContracts]:
        """Gets the flex_contracts of this PricingParams.


        :return: The flex_contracts of this PricingParams.
        :rtype: List[PricingParamsFlexContracts]
        """
        return self._flex_contracts

    @flex_contracts.setter
    def flex_contracts(self, flex_contracts: List[PricingParamsFlexContracts]):
        """Sets the flex_contracts of this PricingParams.


        :param flex_contracts: The flex_contracts of this PricingParams.
        :type flex_contracts: List[PricingParamsFlexContracts]
        """

        self._flex_contracts = flex_contracts

    @property
    def store_data(self) -> bool:
        """Gets the store_data of this PricingParams.


        :return: The store_data of this PricingParams.
        :rtype: bool
        """
        return self._store_data

    @store_data.setter
    def store_data(self, store_data: bool):
        """Sets the store_data of this PricingParams.


        :param store_data: The store_data of this PricingParams.
        :type store_data: bool
        """

        self._store_data = store_data