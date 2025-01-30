# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class UmbrellaConfigBuilder:
    """
    Builds and executes requests for operations under /device/umbrella/umbrella-config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_umbrella_config(self, device_id: str, **kw) -> Any:
        """
        Get Umbrella configuration from device

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/umbrella/umbrella-config", params=params, **kw
        )
