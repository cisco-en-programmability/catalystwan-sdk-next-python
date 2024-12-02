# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InterfaceAggResp


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/interface/app-agg/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_aggregation_app_data_by_query_1(self):
        class get_post_aggregation_app_data_by_query_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> List[InterfaceAggResp]:
                """
                Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Query filter
                :returns: List[InterfaceAggResp]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/interface/app-agg/aggregation",
                    return_type=List[InterfaceAggResp],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_aggregation_app_data_by_query_1_(self._request_adapter)
