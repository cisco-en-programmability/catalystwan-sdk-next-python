# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class ListBuilder:
    """
    Builds and executes requests for operations under /certificate/save/vedge/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def save_v_edge_list(self, payload: Optional[str] = None, **kw) -> str:
        """
        change VedgeList Validity

        :param payload: JSON payload with RootCertChain and Certificate details.
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/certificate/save/vedge/list",
            return_type=str,
            payload=payload,
            **kw,
        )
