# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class TopnBuilder:
    """
    Builds and executes requests for operations under /alarms/topn
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_top_n(self, payload: Optional[Any] = None, site_id: Optional[str] = None, **kw) -> Any:
        """
        Returns top-n alarm count based on given query

        :param site_id: Specify the site-id to filter the alarms
        :param payload: Input query
        :returns: Any
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request("POST", "/dataservice/alarms/topn", params=params, payload=payload, **kw)
