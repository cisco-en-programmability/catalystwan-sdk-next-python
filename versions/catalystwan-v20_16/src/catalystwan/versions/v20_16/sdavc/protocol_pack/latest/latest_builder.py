# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class LatestBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/latest
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_latest_system_pack(self, **kw) -> Any:
        """
        Get current latest protocol pack details

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/sdavc/protocol-pack/latest", **kw)
