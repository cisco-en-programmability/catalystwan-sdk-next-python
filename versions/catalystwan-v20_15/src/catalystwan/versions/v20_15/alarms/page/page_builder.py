# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import Alarm


class PageBuilder:
    """
    Builds and executes requests for operations under /alarms/page
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_page(
        self,
        query: str,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
        **kw,
    ) -> List[Alarm]:
        """
        Get paginated alarms

        :param query: Query
        :param scroll_id: Scroll ID
        :param count: Number of alarms per page
        :param site_id: Specify the site-id to filter the alarms
        :returns: List[Alarm]
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/page", return_type=List[Alarm], params=params, **kw
        )

    def post_page(
        self,
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        site_id: Optional[str] = None,
        **kw,
    ) -> List[Alarm]:
        """
        Get paginated alarm raw data

        :param scroll_id: Scroll ID
        :param count: Number of alarms per page
        :param site_id: Specify the site-id to filter the alarms
        :param payload: Alarm query string
        :returns: List[Alarm]
        """
        params = {
            "scrollId": scroll_id,
            "count": count,
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/alarms/page",
            return_type=List[Alarm],
            params=params,
            payload=payload,
            **kw,
        )
