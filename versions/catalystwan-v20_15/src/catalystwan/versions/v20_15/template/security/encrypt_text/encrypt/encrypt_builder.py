# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class EncryptBuilder:
    """
    Builds and executes requests for operations under /template/security/encryptText/encrypt
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_encrypted_string(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get Type 6 Encryptedd String for a given value

        :param payload: Type6 Encryption
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/security/encryptText/encrypt", payload=payload, **kw
        )
