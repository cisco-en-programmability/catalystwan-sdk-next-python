# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AsyncBuilder:
    """
    Builds and executes requests for operations under /tenant/bulk/async
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_tenant_async_bulk(self):
        class create_tenant_async_bulk_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create multiple tenants on vManage asynchronously


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Tenant model
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/tenant/bulk/async", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_tenant_async_bulk_(self._request_adapter)

    @property
    def delete_tenant_async_bulk(self):
        class delete_tenant_async_bulk_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Delete multiple tenants on vManage asynchronously


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Tenant model
                :returns: Any
                """
                return self._request_adapter.request(
                    "DELETE", "/dataservice/tenant/bulk/async", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return delete_tenant_async_bulk_(self._request_adapter)
