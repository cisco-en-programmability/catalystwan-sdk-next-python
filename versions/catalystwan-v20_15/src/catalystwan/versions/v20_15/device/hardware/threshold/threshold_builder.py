# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class ThresholdBuilder:
    """
    Builds and executes requests for operations under /device/hardware/threshold
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_temp_threshold_list(self, device_id: str, **kw) -> Any:
        """
        Get hardware temperature list from device

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/hardware/threshold", params=params, **kw
        )
