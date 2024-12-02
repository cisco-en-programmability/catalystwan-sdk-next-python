# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AuthtokenBuilder:
    """
    Builds and executes requests for operations under /cloudservices/authtoken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_azure_token(self):
        class get_azure_token_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Get Azure token

                :param payload: Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/cloudservices/authtoken",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return get_azure_token_(self._request_adapter)
