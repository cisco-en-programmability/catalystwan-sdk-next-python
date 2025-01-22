# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RangefromBuilder:
    """
    Builds and executes requests for operations under /util/olapdb/migration/rangefrom
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stats_migration_range_config(self, **kw) -> Any:
        """
        Get migration historical data range configuration from upgrade time

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/util/olapdb/migration/rangefrom", **kw
        )

    def post_stats_migration_range_config(self, payload: Optional[str] = None, **kw) -> Any:
        """
        Config migration historical data range from upgrade time in seconds. -1 to keep all.

        :param payload: Range from config
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/util/olapdb/migration/rangefrom", payload=payload, **kw
        )
