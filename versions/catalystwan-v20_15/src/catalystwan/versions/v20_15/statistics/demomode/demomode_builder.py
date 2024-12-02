# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface


class DemomodeBuilder:
    """
    Builds and executes requests for operations under /statistics/demomode
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def enable_statistics_demo_mode(self, enable: Optional[bool] = True, **kw) -> Any:
        """
        Enable statistic demo mode

        :param enable: Demo mode flag
        :returns: Any
        """
        params = {
            "enable": enable,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/demomode", params=params, **kw
        )
