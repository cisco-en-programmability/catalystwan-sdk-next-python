# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class IptosgtbindingsBuilder:
    """
    Builds and executes requests for operations under /device/policy/iptosgtbindings
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def show_vsmart_ipto_sgt_binding(self, device_id: str, **kw) -> Any:
        """
        show ip to sgt binding from Vsmart

        :param device_id: Device Id
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/policy/iptosgtbindings", params=params, **kw)
