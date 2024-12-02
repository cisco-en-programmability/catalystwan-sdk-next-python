# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AlarmAggregationResponse


class AggregationBuilder:
    """
    Builds and executes requests for operations under /alarms/aggregation
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aggregation_data(
        self,
        query: str,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
        **kw,
    ) -> AlarmAggregationResponse:
        """
        Get aggregated count of alarms based on given query.

        :param query: Query
        :param site_id: Specify the site-id to filter the alarms
        :param include_tenants: Specify whether the tenant alarms need to be visible or not from provider view.
        :returns: AlarmAggregationResponse
        """
        params = {
            "query": query,
            "site-id": site_id,
            "includeTenants": include_tenants,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/alarms/aggregation",
            return_type=AlarmAggregationResponse,
            params=params,
            **kw,
        )

    def post_aggregation_data(
        self,
        payload: Optional[Any] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
        **kw,
    ) -> AlarmAggregationResponse:
        """
        Get aggregated count of alarms based on given query.

        :param site_id: Specify the site-id to filter the alarms
        :param include_tenants: Specify whether the tenant alarms need to be visible or not from provider view.
        :param payload: Query
        :returns: AlarmAggregationResponse
        """
        params = {
            "site-id": site_id,
            "includeTenants": include_tenants,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/alarms/aggregation",
            return_type=AlarmAggregationResponse,
            params=params,
            payload=payload,
            **kw,
        )
