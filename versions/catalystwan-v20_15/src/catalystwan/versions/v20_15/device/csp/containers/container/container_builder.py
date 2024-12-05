# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class ContainerBuilder:
    """
    Builds and executes requests for operations under /device/csp/containers/container
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_device_containers_info(self, device_id: str, **kw) -> Any:
        """
        Get device container from device (Real Time)

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/csp/containers/container", params=params, **kw)
