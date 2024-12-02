# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceIp


class IoxconfigBuilder:
    """
    Builds and executes requests for operations under /device/action/test/ioxconfig
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def test_iox_config(self, device_ip: DeviceIp, **kw):
        """
        testIoxConfig

        :param device_ip: Device IP
        :returns: None
        """
        params = {
            "deviceIP": device_ip,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/test/ioxconfig/{deviceIP}",
            params=params,
            **kw,
        )
