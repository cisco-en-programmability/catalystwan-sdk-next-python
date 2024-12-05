# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class RsaBuilder:
    """
    Builds and executes requests for operations under /certificate/reset/rsa
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def reset_rsa(self):
        class reset_rsa_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                resetRSA for controllers

                :param payload: JSON payload with deviceIP details for rsa reset
                :returns: str
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/certificate/reset/rsa", return_type=str, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return reset_rsa_(self._request_adapter)
