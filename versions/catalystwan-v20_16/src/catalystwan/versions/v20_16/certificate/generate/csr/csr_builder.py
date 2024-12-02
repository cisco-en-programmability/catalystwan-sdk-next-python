# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CsrBuilder:
    """
    Builds and executes requests for operations under /certificate/generate/csr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_csr(self, payload: Optional[Any] = None, **kw) -> str:
        """
        get certificaate details

        :param payload: Device IP
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/certificate/generate/csr", return_type=str, payload=payload, **kw
        )
