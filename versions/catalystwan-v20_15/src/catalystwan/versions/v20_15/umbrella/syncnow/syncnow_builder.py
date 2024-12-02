# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class SyncnowBuilder:
    """
    Builds and executes requests for operations under /umbrella/syncnow
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def send_meta_data_to_umbrella(self, **kw):
        """
        Get metadata from db and send to Umbrella

        :returns: None
        """
        return self._request_adapter.request(
            "GET", "/dataservice/umbrella/syncnow", **kw
        )
