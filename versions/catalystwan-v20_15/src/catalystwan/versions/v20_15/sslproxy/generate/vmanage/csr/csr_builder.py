# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CsrBuilder:
    """
    Builds and executes requests for operations under /sslproxy/generate/vmanage/csr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_ssl_proxy_csr(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Generate CSR

        :param payload: CSR request
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/generate/vmanage/csr", payload=payload, **kw
        )
