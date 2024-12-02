# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class InvalidateBuilder:
    """
    Builds and executes requests for operations under /certificate/device/invalidate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def invalidate_device(self):
        class invalidate_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                invalidate the device

                :param payload: Device UUID
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/certificate/device/invalidate",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return invalidate_device_(self._request_adapter)
