# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AuthtokenBuilder:
    """
    Builds and executes requests for operations under /cloudservices/authtoken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_azure_token(self, payload: Optional[str] = None, **kw) -> Any:
        """
        Get Azure token

        :param payload: Payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/cloudservices/authtoken", payload=payload, **kw
        )
