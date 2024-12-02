# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DpiAggregationResponse


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/aggregation
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_stats_aggregation_data(
        self, query: Optional[str] = None, **kw
    ) -> DpiAggregationResponse:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param query: Query
        :returns: DpiAggregationResponse
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/dpi/aggregation",
            return_type=DpiAggregationResponse,
            params=params,
            **kw,
        )

    def get_dpi_stats_aggregation_data_post(
        self, payload: Optional[Any] = None, **kw
    ) -> DpiAggregationResponse:
        """
        Get raw aggregated data and display applications with the highest utilization for a device

        :param payload: User
        :returns: DpiAggregationResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/dpi/aggregation",
            return_type=DpiAggregationResponse,
            payload=payload,
            **kw,
        )
