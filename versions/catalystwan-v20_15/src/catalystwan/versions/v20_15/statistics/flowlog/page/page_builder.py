# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import FlowlogPaginationResponse


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/flowlog/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stats_pagination_raw_data_23(
        self,
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> FlowlogPaginationResponse:
        """
        Get stats pagination raw data

        :param query: Query string
        :param scroll_id: Scroll Id
        :param count: Result size
        :returns: FlowlogPaginationResponse
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/flowlog/page",
            return_type=FlowlogPaginationResponse,
            params=params,
            **kw,
        )

    @property
    def get_stats_pagination_raw_data_post(self):
        class get_stats_pagination_raw_data_post_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                count: Optional[int] = None,
                **kw,
            ) -> FlowlogPaginationResponse:
                """
                Get stats pagination raw data

                :param scroll_id: Scroll Id
                :param count: Result size
                :param payload: Stats query string
                :returns: FlowlogPaginationResponse
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/flowlog/page",
                    return_type=FlowlogPaginationResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_stats_pagination_raw_data_post_(self._request_adapter)
