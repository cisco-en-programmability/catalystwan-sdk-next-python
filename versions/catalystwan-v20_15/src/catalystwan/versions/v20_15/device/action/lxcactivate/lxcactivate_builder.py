# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class LxcactivateBuilder:
    """
    Builds and executes requests for operations under /device/action/lxcactivate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_lxc_activate(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process an activation operation

        :param payload: Activation request payload
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/device/action/lxcactivate", payload=payload, **kw)
