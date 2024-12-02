# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class EncryptBuilder:
    """
    Builds and executes requests for operations under /template/security/encryptText/encrypt
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_encrypted_string(self):
        class get_encrypted_string_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get Type 6 Encryptedd String for a given value

                :param payload: Type6 Encryption
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/security/encryptText/encrypt",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_encrypted_string_(self._request_adapter)
