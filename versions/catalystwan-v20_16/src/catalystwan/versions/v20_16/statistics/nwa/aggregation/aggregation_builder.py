# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import NetworkAvailabilityResp


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/nwa/aggregation
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_post_aggregation_data_by_query_3(
        self, payload: Optional[Any] = None, **kw
    ) -> List[NetworkAvailabilityResp]:
        """
        Get network availability aggregated data based on input query and filters.

        :param payload: Stats query string
        :returns: List[NetworkAvailabilityResp]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/nwa/aggregation",
            return_type=List[NetworkAvailabilityResp],
            payload=payload,
            **kw,
        )
