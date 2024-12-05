# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CertificatesBuilder:
    """
    Builds and executes requests for operations under /sslproxy/certificates
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def upload_certificiates(self, payload: Optional[Any] = None, **kw):
        """
        Upload device certificates

        :param payload: Certificate file
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/sslproxy/certificates", payload=payload, **kw)
