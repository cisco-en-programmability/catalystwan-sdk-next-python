# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import StatisticsDbQueryParam


class UniqueAggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/eiolte/uniqueAggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def unique_aggregation(self):
        class unique_aggregation_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[StatisticsDbQueryParam] = None, **kw) -> Any:
                """
                Get unique aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Stats query string
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/statistics/eiolte/uniqueAggregation", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> StatisticsDbQueryParam:
                return StatisticsDbQueryParam(*args, **kwargs)

            @property
            def payload_model(self) -> Type[StatisticsDbQueryParam]:
                return StatisticsDbQueryParam

        return unique_aggregation_(self._request_adapter)
