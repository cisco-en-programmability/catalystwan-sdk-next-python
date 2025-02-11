# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DoccountBuilder:
    """
    Builds and executes requests for operations under /statistics/interface/doccount
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_count10(self, query: str, **kw) -> Any:
        """
        Get response count of a query

        :param query: Query
        :returns: Any
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/interface/doccount", params=params, **kw
        )

    def get_count_post_11(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get response count of a query

        :param payload: Query filter
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/statistics/interface/doccount", payload=payload, **kw
        )
