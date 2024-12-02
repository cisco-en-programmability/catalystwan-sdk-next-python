# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import EventQueryInputResponse


class InputBuilder:
    """
    Builds and executes requests for operations under /event/query/input
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_events_query_config(self, **kw) -> EventQueryInputResponse:
        """
        Get event field details

        :returns: EventQueryInputResponse
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/event/query/input",
            return_type=EventQueryInputResponse,
            **kw,
        )
