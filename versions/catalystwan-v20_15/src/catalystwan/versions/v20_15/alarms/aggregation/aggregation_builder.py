# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import AlarmAggregationResponse


class AggregationBuilder:
    """
    Builds and executes requests for operations under /alarms/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aggregation_data(
        self, query: str, site_id: Optional[str] = None, **kw
    ) -> AlarmAggregationResponse:
        """
        Get aggregated count of alarms based on given query.

        :param query: Query
        :param site_id: Specify the site-id to filter the alarms
        :returns: AlarmAggregationResponse
        """
        params = {
            "query": query,
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/alarms/aggregation",
            return_type=AlarmAggregationResponse,
            params=params,
            **kw,
        )

    @property
    def post_aggregation_data(self):
        class post_aggregation_data_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, site_id: Optional[str] = None, **kw
            ) -> AlarmAggregationResponse:
                """
                Get aggregated count of alarms based on given query.

                :param site_id: Specify the site-id to filter the alarms
                :param payload: Query
                :returns: AlarmAggregationResponse
                """
                params = {
                    "site-id": site_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/alarms/aggregation",
                    return_type=AlarmAggregationResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return post_aggregation_data_(self._request_adapter)
