# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/cflowd/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stats_pagination_raw_data_7(
        self,
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> Any:
        """
        Get stats raw data

        :param query: Query string
        :param scroll_id: ES scroll Id
        :param count: Result size
        :returns: Any
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/cflowd/page", params=params, **kw
        )

    @property
    def get_post_stats_pagination_raw_data_7(self):
        class get_post_stats_pagination_raw_data_7_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                count: Optional[int] = None,
                **kw,
            ) -> Any:
                """
                Get stats raw data

                :param scroll_id: ES scroll Id
                :param count: Result size
                :param payload: Stats query string
                :returns: Any
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/cflowd/page",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_stats_pagination_raw_data_7_(self._request_adapter)
