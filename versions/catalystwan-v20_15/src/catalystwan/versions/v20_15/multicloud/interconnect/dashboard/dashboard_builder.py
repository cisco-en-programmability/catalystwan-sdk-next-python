# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import InterconnectDashboard


class DashboardBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/dashboard
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_dashboard(self, **kw) -> List[InterconnectDashboard]:
        """
        API to retrieve Multicloud Interconnect dashboard view.

        :returns: List[InterconnectDashboard]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/dashboard",
            return_type=List[InterconnectDashboard],
            **kw,
        )
