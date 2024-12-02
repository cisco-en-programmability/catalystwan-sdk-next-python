# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class MasterBuilder:
    """
    Builds and executes requests for operations under /alarms/master
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_master_manager_state(self, **kw) -> str:
        """
        Get topic details.

        :returns: str
        """
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/master", return_type=str, **kw
        )
