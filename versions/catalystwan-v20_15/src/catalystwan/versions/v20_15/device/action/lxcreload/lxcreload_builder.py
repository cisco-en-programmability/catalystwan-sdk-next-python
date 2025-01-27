# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class LxcreloadBuilder:
    """
    Builds and executes requests for operations under /device/action/lxcreload
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_lxc_reload(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process a reload operation

        :param payload: Reload request payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/lxcreload", payload=payload, **kw
        )
