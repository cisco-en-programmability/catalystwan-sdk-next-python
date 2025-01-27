# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class JksBuilder:
    """
    Builds and executes requests for operations under /certificate/jks
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_jks(self, payload: Optional[str] = None, **kw) -> str:
        """
        update JKS

        :param payload: JSON payload with encoded JKS.
        :returns: str
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/certificate/jks", return_type=str, payload=payload, **kw
        )
