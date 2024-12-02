# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceStatusData


class DevicestatusBuilder:
    """
    Builds and executes requests for operations under /device/devicestatus
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_only_status(self, **kw) -> DeviceStatusData:
        """
        Get devices status per type

        :returns: DeviceStatusData
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/devicestatus",
            return_type=DeviceStatusData,
            **kw,
        )
