# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DoccountBuilder:
    """
    Builds and executes requests for operations under /alarms/doccount
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_doc_count(self, query: str, site_id: Optional[str] = None, **kw) -> Any:
        """
        Get the count of alarms as per the query passed.

        :param query: Query
        :param site_id: Specify the site-id to filter the alarms
        :returns: Any
        """
        params = {
            "query": query,
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/doccount", params=params, **kw
        )

    def post_doc_count(
        self, payload: Optional[Any] = None, site_id: Optional[str] = None, **kw
    ) -> Any:
        """
        Get the count of alarms as per the query passed.

        :param site_id: Specify the site-id to filter the alarms
        :param payload: Query
        :returns: Any
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/alarms/doccount", params=params, payload=payload, **kw
        )
