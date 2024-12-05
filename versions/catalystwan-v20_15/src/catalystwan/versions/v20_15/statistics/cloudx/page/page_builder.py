# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/cloudx/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stats_pagination_raw_data_8(
        self, query: Optional[str] = None, scroll_id: Optional[str] = None, count: Optional[int] = None, **kw
    ) -> Any:
        """
        Get stats raw data

        :param query: Query string
        :param scroll_id: ES scroll Id
        :param count: Result size
        :returns: Any
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request("GET", "/dataservice/statistics/cloudx/page", params=params, **kw)

    def get_post_stats_pagination_raw_data_8(
        self, payload: Optional[Any] = None, scroll_id: Optional[str] = None, count: Optional[int] = None, **kw
    ) -> Any:
        """
        Get stats raw data

        :param scroll_id: ES scroll Id
        :param count: Result size
        :param payload: Stats query string
        :returns: Any
        """
        params = {
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/statistics/cloudx/page", params=params, payload=payload, **kw
        )
