# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AsyncBuilder:
    """
    Builds and executes requests for operations under /tenant/async
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_tenant_async(self):
        class create_tenant_async_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create a new tenant in Multi-Tenant vManage asynchronously


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Tenant model
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/tenant/async", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_tenant_async_(self._request_adapter)
