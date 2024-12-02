# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RenewBuilder:
    """
    Builds and executes requests for operations under /sslproxy/renew
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def renew_certificate(self):
        class renew_certificate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Renew device certificate

                :param payload: Renew device certificate request
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/sslproxy/renew", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return renew_certificate_(self._request_adapter)
