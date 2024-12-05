# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class JksBuilder:
    """
    Builds and executes requests for operations under /certificate/jks
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_jks(self):
        class update_jks_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                update JKS

                :param payload: JSON payload with encoded JKS.
                :returns: str
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/certificate/jks", return_type=str, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return update_jks_(self._request_adapter)
