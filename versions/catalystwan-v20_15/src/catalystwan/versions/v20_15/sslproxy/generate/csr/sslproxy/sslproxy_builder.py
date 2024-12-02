# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class SslproxyBuilder:
    """
    Builds and executes requests for operations under /sslproxy/generate/csr/sslproxy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def generate_ssl_proxy_csr(self):
        class generate_ssl_proxy_csr_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                CSR request SSL proxy for edge

                :param payload: CSR request for edge
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "generateSslProxyCSR")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sslproxy/generate/csr/sslproxy",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return generate_ssl_proxy_csr_(self._request_adapter)
