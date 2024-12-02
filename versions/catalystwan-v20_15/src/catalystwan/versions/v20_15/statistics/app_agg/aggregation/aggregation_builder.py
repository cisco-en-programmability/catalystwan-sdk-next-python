# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/app-agg/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_aggregation_app_data_by_query(self):
        class get_post_aggregation_app_data_by_query_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Stats query string
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/app-agg/aggregation",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_aggregation_app_data_by_query_(self._request_adapter)
