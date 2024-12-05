# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RenewBuilder:
    """
    Builds and executes requests for operations under /sslproxy/renew
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def renew_certificate(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Renew device certificate

        :param payload: Renew device certificate request
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/sslproxy/renew", payload=payload, **kw)
