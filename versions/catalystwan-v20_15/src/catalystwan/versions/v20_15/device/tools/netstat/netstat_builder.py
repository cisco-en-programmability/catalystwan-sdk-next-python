# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
from .models import VpnParam


class NetstatBuilder:
    """
    Builds and executes requests for operations under /device/tools/netstat
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_tools_netstat(
        self,
        device_id: str,
        vpn: Optional[VpnParam] = None,
        options: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get device tool net stat

        :param vpn: VPN
        :param options: Options
        :param device_id: Device Id
        :returns: Any
        """
        params = {
            "vpn": vpn,
            "options": options,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/tools/netstat", params=params, **kw
        )
