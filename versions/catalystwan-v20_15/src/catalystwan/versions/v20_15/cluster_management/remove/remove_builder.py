# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RemoveBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/remove
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def remove_vmanage(self, payload: Optional[Any] = None, **kw):
        """
        Remove vManage from cluster


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: vManage server info
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/clusterManagement/remove", payload=payload, **kw)
