# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class SignedCertBuilder:
    """
    Builds and executes requests for operations under /certificate/install/signedCert
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def install_certificate(self, payload: Optional[Any] = None, **kw) -> str:
        """
        install Certificate

        :param payload: Certificate
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/certificate/install/signedCert",
            return_type=str,
            payload=payload,
            **kw,
        )
