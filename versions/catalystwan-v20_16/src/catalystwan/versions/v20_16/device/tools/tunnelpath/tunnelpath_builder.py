# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class TunnelpathBuilder:
    """
    Builds and executes requests for operations under /device/tools/tunnelpath
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def tunnel_path(self, device_ip: str, payload: Optional[Any] = None, **kw):
        """
        TunnelPath

        :param device_ip: Device IP
        :param payload: TunnelPath parameter
        :returns: None
        """
        params = {
            "deviceIP": device_ip,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/device/tools/tunnelpath/{deviceIP}",
            params=params,
            payload=payload,
            **kw,
        )
