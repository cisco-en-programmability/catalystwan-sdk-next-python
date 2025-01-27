# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class RediscoverallBuilder:
    """
    Builds and executes requests for operations under /device/action/rediscoverall
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def re_discover_all_device(self, **kw):
        """
        Rediscover all devices

        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/rediscoverall", **kw
        )
