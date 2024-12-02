# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import InlineResponse2001


class AggregationBuilder:
    """
    Builds and executes requests for operations under /multicloud/statistics/interface/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_post_aggregation_data_by_query_28(self):
        class get_post_aggregation_data_by_query_28_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> InlineResponse2001:
                """
                Get aggregated data based on input query and filter. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Stats query string
                :returns: InlineResponse2001
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/statistics/interface/aggregation",
                    return_type=InlineResponse2001,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_aggregation_data_by_query_28_(self._request_adapter)
