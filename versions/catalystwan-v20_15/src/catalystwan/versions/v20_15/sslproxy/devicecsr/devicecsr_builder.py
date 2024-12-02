# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class DevicecsrBuilder:
    """
    Builds and executes requests for operations under /sslproxy/devicecsr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_all_device_csr(self):
        class get_all_device_csr_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get CSR for all cEdges

                :param payload: Device list
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/sslproxy/devicecsr", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_all_device_csr_(self._request_adapter)
