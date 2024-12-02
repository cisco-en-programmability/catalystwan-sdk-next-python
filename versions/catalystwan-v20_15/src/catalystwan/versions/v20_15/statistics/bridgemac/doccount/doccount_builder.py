# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class DoccountBuilder:
    """
    Builds and executes requests for operations under /statistics/bridgemac/doccount
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_count_8(self, query: str, **kw) -> Any:
        """
        Get response count of a query

        :param query: Query
        :returns: Any
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/bridgemac/doccount", params=params, **kw
        )

    @property
    def get_count_post_7(self):
        class get_count_post_7_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get response count of a query

                :param payload: Query
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/bridgemac/doccount",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_count_post_7_(self._request_adapter)
