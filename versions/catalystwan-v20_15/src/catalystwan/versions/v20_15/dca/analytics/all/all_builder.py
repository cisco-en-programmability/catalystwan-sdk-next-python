# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AllBuilder:
    """
    Builds and executes requests for operations under /dca/analytics/all
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_stats_data_dca(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get all statistics setting data

        :param payload: Stats setting
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dca/analytics/all", payload=payload, **kw
        )
