# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
from .models import VpnIdParam
from .models import IfNameParam


class Ndv6Builder:
    """
    Builds and executes requests for operations under /device/ndv6
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_ipv6_interface(
        self,
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        if_name: Optional[IfNameParam] = None,
        mac: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get IPv6 Neighbors from device (Real Time)

        :param vpn_id: VPN Id
        :param if_name: Interface name
        :param mac: Mac address
        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "vpn-id": vpn_id,
            "if-name": if_name,
            "mac": mac,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/ndv6", params=params, **kw
        )
