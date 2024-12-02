# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class CsrBuilder:
    """
    Builds and executes requests for operations under /certificate/generate/csr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def generate_csr(self):
        class generate_csr_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                get certificaate details

                :param payload: Device IP
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/certificate/generate/csr",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return generate_csr_(self._request_adapter)
