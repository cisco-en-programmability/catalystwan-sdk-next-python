# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import CreateVpnList


class VpnBuilder:
    """
    Builds and executes requests for operations under /device/action/vpn
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_vpn_list(self, **kw) -> CreateVpnList:
        """
        Create VPN list

        :returns: CreateVpnList
        """
        return self._request_adapter.request("GET", "/dataservice/device/action/vpn", return_type=CreateVpnList, **kw)
