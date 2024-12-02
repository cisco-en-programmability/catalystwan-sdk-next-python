# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class VedgeBuilder:
    """
    Builds and executes requests for operations under /certificate/generate/enterprise/csr/vedge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def generate_enterprise_csr(self):
        class generate_enterprise_csr_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                generate CSR on hardware WAN edge device

                :param payload: Device UUID
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/certificate/generate/enterprise/csr/vedge",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return generate_enterprise_csr_(self._request_adapter)
