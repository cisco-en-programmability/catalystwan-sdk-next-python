# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class MemorydbBuilder:
    """
    Builds and executes requests for operations under /device/syncall/memorydb
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_all_devices_mem_db(self, **kw):
        """
        Synchronize memory database for all devices

        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/device/syncall/memorydb", **kw)
