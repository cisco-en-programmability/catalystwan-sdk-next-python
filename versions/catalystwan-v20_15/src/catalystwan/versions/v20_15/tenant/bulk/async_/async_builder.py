# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AsyncBuilder:
    """
    Builds and executes requests for operations under /tenant/bulk/async
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_tenant_async_bulk(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create multiple tenants on vManage asynchronously


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Tenant model
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/tenant/bulk/async", payload=payload, **kw)

    def delete_tenant_async_bulk(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Delete multiple tenants on vManage asynchronously


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Tenant model
        :returns: Any
        """
        return self._request_adapter.request("DELETE", "/dataservice/tenant/bulk/async", payload=payload, **kw)
