# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class LxcdeleteBuilder:
    """
    Builds and executes requests for operations under /device/action/lxcdelete
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_lxc_delete(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process a delete operation

        :param payload: Delete request payload
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/device/action/lxcdelete", payload=payload, **kw)
