# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AlarmResponse


class PageBuilder:
    """
    Builds and executes requests for operations under /event/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_page_1(
        self,
        query: str,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
        **kw,
    ) -> AlarmResponse:
        """
        Get paginated events

        :param query: Query
        :param scroll_id: Scroll ID
        :param count: Number of alarms per page
        :param site_id: Specify the site-id to filter the events
        :returns: AlarmResponse
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/event/page",
            return_type=AlarmResponse,
            params=params,
            **kw,
        )

    @property
    def post_page_1(self):
        class post_page_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                count: Optional[int] = None,
                site_id: Optional[str] = None,
                **kw,
            ) -> AlarmResponse:
                """
                Get paginated events

                :param scroll_id: Scroll ID
                :param count: Number of alarms per page
                :param site_id: Specify the site-id to filter the events
                :param payload: Event query string
                :returns: AlarmResponse
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                    "site-id": site_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/event/page",
                    return_type=AlarmResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return post_page_1_(self._request_adapter)
