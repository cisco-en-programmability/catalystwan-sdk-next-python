# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AppRouteAggResp


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/aggregation
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aggregation_data_by_query_2(
        self, query: Optional[str] = None, **kw
    ) -> List[AppRouteAggResp]:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param query: Query
        :returns: List[AppRouteAggResp]
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/approute/aggregation",
            return_type=List[AppRouteAggResp],
            params=params,
            **kw,
        )

    def get_post_aggregation_data_by_query_2(
        self, payload: Optional[Any] = None, **kw
    ) -> List[AppRouteAggResp]:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param payload: Stats query string
        :returns: List[AppRouteAggResp]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/approute/aggregation",
            return_type=List[AppRouteAggResp],
            payload=payload,
            **kw,
        )
