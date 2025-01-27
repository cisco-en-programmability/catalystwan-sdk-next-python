# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AsyncBuilder:
    """
    Builds and executes requests for operations under /tenant/async
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_tenant_async(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create a new tenant in Multi-Tenant vManage asynchronously


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Tenant model
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/tenant/async", payload=payload, **kw
        )
