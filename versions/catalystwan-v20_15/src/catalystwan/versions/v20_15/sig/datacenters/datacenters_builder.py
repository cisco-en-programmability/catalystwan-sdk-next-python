# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface
from .models import GetDataCenters


class DatacentersBuilder:
    """
    Builds and executes requests for operations under /sig/datacenters
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sig_dynamic_data_center_list(
        self, type_: str, tunneltype: str, **kw
    ) -> GetDataCenters:
        """
        The API to get all sig data center for given provider type

        :param type_: Type
        :param tunneltype: Tunneltype
        :returns: GetDataCenters
        """
        params = {
            "type": type_,
            "tunneltype": tunneltype,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/sig/datacenters/{type}/{tunneltype}",
            return_type=GetDataCenters,
            params=params,
            **kw,
        )

    def get_sig_data_center_list(
        self, type_: str, tunneltype: str, devicetype: str, **kw
    ) -> Any:
        """
        Get list of data centers for zscaler or umbrella

        :param type_: Provider type
        :param tunneltype: Type of the tunnel ipsec/gre
        :param devicetype: Type of the device vedge/cedge
        :returns: Any
        """
        params = {
            "type": type_,
            "tunneltype": tunneltype,
            "devicetype": devicetype,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/sig/datacenters/{type}/{tunneltype}/{devicetype}",
            params=params,
            **kw,
        )
