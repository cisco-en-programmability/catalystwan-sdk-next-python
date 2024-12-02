# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import NetworkAvailabilityResp


class DetailsBuilder:
    """
    Builds and executes requests for operations under /statistics/nwa/details
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_detail_aggregation_data_by_query(self):
        class get_detail_aggregation_data_by_query_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                include_prev: Optional[bool] = False,
                **kw,
            ) -> List[NetworkAvailabilityResp]:
                """
                Get network availability aggregated data with details based on input query and filters.

                :param include_prev: Include prev
                :param payload: Stats query string
                :returns: List[NetworkAvailabilityResp]
                """
                params = {
                    "includePrev": include_prev,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/nwa/details",
                    return_type=List[NetworkAvailabilityResp],
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_detail_aggregation_data_by_query_(self._request_adapter)
