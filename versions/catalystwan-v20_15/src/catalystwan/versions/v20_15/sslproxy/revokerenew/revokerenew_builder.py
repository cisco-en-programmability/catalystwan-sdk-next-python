# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RevokerenewBuilder:
    """
    Builds and executes requests for operations under /sslproxy/revokerenew
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def revoke_renew_certificate(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Revoke and renew device certificate

        :param payload: Revoke device certificate request
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/sslproxy/revokerenew", payload=payload, **kw)
