# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceIp


class StatisticBuilder:
    """
    Builds and executes requests for operations under /device/pppoe/statistic
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_pp_po_e_neighbor_list(self, device_id: DeviceIp, **kw) -> Any:
        """
        Get PPPoE statistics from device

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/pppoe/statistic", params=params, **kw)
