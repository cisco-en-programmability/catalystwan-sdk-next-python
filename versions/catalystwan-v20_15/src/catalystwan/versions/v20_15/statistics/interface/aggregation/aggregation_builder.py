# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import InterfaceAggResp, InterfaceAggRespWithPageInfo


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/interface/aggregation
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aggregation_data_by_query_11(
        self, query: str, **kw
    ) -> List[InterfaceAggRespWithPageInfo]:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param query: Query
        :returns: List[InterfaceAggRespWithPageInfo]
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/interface/aggregation",
            return_type=List[InterfaceAggRespWithPageInfo],
            params=params,
            **kw,
        )

    def get_post_aggregation_data_by_query_11(
        self, payload: Optional[Any] = None, **kw
    ) -> List[InterfaceAggResp]:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param payload: Query filter
        :returns: List[InterfaceAggResp]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/interface/aggregation",
            return_type=List[InterfaceAggResp],
            payload=payload,
            **kw,
        )
