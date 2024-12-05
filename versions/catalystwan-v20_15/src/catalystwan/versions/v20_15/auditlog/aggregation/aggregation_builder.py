# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import GetAuditLogAggregation


class AggregationBuilder:
    """
    Builds and executes requests for operations under /auditlog/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_property_aggregation_data(self, query: str, **kw) -> GetAuditLogAggregation:
        """
        Get raw property data aggregated

        :param query: Query
        :returns: GetAuditLogAggregation
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/auditlog/aggregation", return_type=GetAuditLogAggregation, params=params, **kw
        )

    def get_post_property_aggregation_data(self, payload: Optional[Any] = None, **kw) -> GetAuditLogAggregation:
        """
        Get raw property data aggregated with post action

        :param payload: Stats query string
        :returns: GetAuditLogAggregation
        """
        return self._request_adapter.request(
            "POST", "/dataservice/auditlog/aggregation", return_type=GetAuditLogAggregation, payload=payload, **kw
        )
