# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class LineSpecificStatsBuilder:
    """
    Builds and executes requests for operations under /device/vdslService/lineSpecificStats
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_line_specific_stats(self, device_id: str, **kw) -> Any:
        """
        Get VDSL service line specific stats from device

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/vdslService/lineSpecificStats",
            params=params,
            **kw,
        )
