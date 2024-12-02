# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ApplicationSiteChartItem


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/perfmon/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_aggregation_data_by_query_15(self):
        class get_post_aggregation_data_by_query_15_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[str] = None, **kw
            ) -> List[ApplicationSiteChartItem]:
                """
                Get one application one site line chart data

                :param payload: Stats query string
                :returns: List[ApplicationSiteChartItem]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/perfmon/aggregation",
                    return_type=List[ApplicationSiteChartItem],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return get_post_aggregation_data_by_query_15_(self._request_adapter)
