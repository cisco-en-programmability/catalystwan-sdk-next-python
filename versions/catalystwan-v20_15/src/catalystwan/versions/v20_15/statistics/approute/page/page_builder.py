# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AppRouteAggRespWithPageInfo


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/page
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_bulk_raw_data(
        self,
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> AppRouteAggRespWithPageInfo:
        """
        Get stats raw data

        :param query: Query string
        :param scroll_id: Scroll id
        :param count: Count
        :returns: AppRouteAggRespWithPageInfo
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/approute/page",
            return_type=AppRouteAggRespWithPageInfo,
            params=params,
            **kw,
        )

    def get_post_stat_bulk_raw_data(
        self,
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> AppRouteAggRespWithPageInfo:
        """
        Get stats raw data

        :param scroll_id: Scroll id
        :param count: Count
        :param payload: Stats query string
        :returns: AppRouteAggRespWithPageInfo
        """
        params = {
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/approute/page",
            return_type=AppRouteAggRespWithPageInfo,
            params=params,
            payload=payload,
            **kw,
        )
