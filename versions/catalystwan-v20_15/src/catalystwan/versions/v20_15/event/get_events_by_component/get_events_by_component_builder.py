# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import ComponentEventMapping


class GetEventsByComponentBuilder:
    """
    Builds and executes requests for operations under /event/getEventsByComponent
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_event_names_by_component(self, query: str, **kw) -> ComponentEventMapping:
        """
        Get event names by component.

        :param query: Event component name
        :returns: ComponentEventMapping
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/event/getEventsByComponent", return_type=ComponentEventMapping, params=params, **kw
        )
