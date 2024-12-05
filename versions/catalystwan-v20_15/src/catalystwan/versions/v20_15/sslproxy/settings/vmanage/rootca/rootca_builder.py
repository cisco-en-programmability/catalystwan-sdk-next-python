# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RootcaBuilder:
    """
    Builds and executes requests for operations under /sslproxy/settings/vmanage/rootca
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def getv_manage_root_ca(self, **kw) -> Any:
        """
        Get vManage root certificate

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/sslproxy/settings/vmanage/rootca", **kw)

    def setv_manage_root_ca(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Set vManage root certificate

        :param payload: Set vManage root CA request
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/settings/vmanage/rootca", payload=payload, **kw
        )
