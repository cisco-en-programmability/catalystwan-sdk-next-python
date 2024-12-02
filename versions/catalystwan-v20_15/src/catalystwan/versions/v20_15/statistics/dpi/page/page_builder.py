# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DpiPaginationResponse


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_stats_pagination_raw_data(
        self,
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> DpiPaginationResponse:
        """
        Get DPI stats pagination raw data

        :param query: Query
        :param scroll_id: Scroll id
        :param count: Count
        :returns: DpiPaginationResponse
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/dpi/page",
            return_type=DpiPaginationResponse,
            params=params,
            **kw,
        )

    @property
    def get_dpi_stats_pagination_raw_data_post(self):
        class get_dpi_stats_pagination_raw_data_post_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                count: Optional[int] = None,
                **kw,
            ) -> DpiPaginationResponse:
                """
                Get DPI stats pagination raw data

                :param scroll_id: Scroll id
                :param count: Count
                :param payload: User
                :returns: DpiPaginationResponse
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/dpi/page",
                    return_type=DpiPaginationResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_dpi_stats_pagination_raw_data_post_(self._request_adapter)
