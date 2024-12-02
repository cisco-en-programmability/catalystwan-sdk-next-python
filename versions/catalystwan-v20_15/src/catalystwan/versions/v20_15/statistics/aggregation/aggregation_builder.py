# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aggregation_data_by_query_14(
        self, query: Optional[str] = None, **kw
    ) -> Any:
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

        :param query: Query filter
        :returns: Any
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/aggregation", params=params, **kw
        )

    @property
    def get_post_aggregation_data_by_query_14(self):
        class get_post_aggregation_data_by_query_14_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Stats query string
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/statistics/aggregation", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_aggregation_data_by_query_14_(self._request_adapter)
