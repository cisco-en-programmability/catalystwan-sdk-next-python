# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import DpiAggregationResponse


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/agg-app/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_agg_app_data_post(
        self, payload: Optional[Any] = None, site_id: Optional[str] = None, **kw
    ) -> DpiAggregationResponse:
        """
        Get raw aggregated data and display applications with the highest utilization for a device

        :param site_id: Site id
        :param payload: Query filter
        :returns: DpiAggregationResponse
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/dpi/agg-app/aggregation",
            return_type=DpiAggregationResponse,
            params=params,
            payload=payload,
            **kw,
        )
