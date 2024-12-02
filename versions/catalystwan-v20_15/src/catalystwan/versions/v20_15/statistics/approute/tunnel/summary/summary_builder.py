# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
from .models import AppRouteRespWithPageInfo


class SummaryBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/tunnel/{type}/summary
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_app_route_tunnel_summary_type(
        self, type_: str, query: Optional[str] = None, **kw
    ) -> List[AppRouteRespWithPageInfo]:
        """
        Get tunnel top statistics in as chart

        :param type_: Type
        :param query: Query
        :returns: List[AppRouteRespWithPageInfo]
        """
        params = {
            "type": type_,
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/approute/tunnel/{type}/summary",
            return_type=List[AppRouteRespWithPageInfo],
            params=params,
            **kw,
        )
