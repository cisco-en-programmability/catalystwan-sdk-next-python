# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import CountResponse


class DoccountBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/doccount
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_stats_count(self, query: Optional[str] = None, **kw) -> CountResponse:
        """
        Get response count of a query

        :param query: Query
        :returns: CountResponse
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/dpi/doccount",
            return_type=CountResponse,
            params=params,
            **kw,
        )

    @property
    def get_dpi_stats_count_post(self):
        class get_dpi_stats_count_post_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> CountResponse:
                """
                Get response count of a query

                :param payload: User
                :returns: CountResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/dpi/doccount",
                    return_type=CountResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_dpi_stats_count_post_(self._request_adapter)
