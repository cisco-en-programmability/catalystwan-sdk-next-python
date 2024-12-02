# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class DevicecertificatesBuilder:
    """
    Builds and executes requests for operations under /sslproxy/devicecertificates
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_all_device_certificates(self):
        class get_all_device_certificates_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get certificate for all cEdges

                :param payload: Device list
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sslproxy/devicecertificates",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_all_device_certificates_(self._request_adapter)
