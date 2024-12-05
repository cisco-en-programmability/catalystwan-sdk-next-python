# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class SslproxyBuilder:
    """
    Builds and executes requests for operations under /sslproxy/generate/csr/sslproxy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_ssl_proxy_csr(self, payload: Optional[Any] = None, **kw):
        """
        CSR request SSL proxy for edge

        :param payload: CSR request for edge
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "generateSslProxyCSR")
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/generate/csr/sslproxy", payload=payload, **kw
        )
