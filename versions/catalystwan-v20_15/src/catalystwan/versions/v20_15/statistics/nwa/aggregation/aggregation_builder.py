# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import NetworkAvailabilityResp


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/nwa/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_aggregation_data_by_query_3(self):
        class get_post_aggregation_data_by_query_3_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
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

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_aggregation_data_by_query_3_(self._request_adapter)
