# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class InterfacesBuilder:
    """
    Builds and executes requests for operations under /template/cloudx/interfaces
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_cloudx_interfaces(self):
        class add_cloudx_interfaces_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Enable cloudx gateway

                :param payload: Cloudx
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cloudx/interfaces",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_cloudx_interfaces_(self._request_adapter)
