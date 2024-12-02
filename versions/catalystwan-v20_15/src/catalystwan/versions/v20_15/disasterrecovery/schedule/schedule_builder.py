# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class ScheduleBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/schedule
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_disaster_recovery_local_replication_schedule(self, **kw) -> Any:
        """
        Get disaster recovery local replication schedule

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/disasterrecovery/schedule", **kw
        )
