# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class SyncBuilder:
    """
    Builds and executes requests for operations under /msla/licenses/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_licenses_1(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Retrieve MSLA subscription/licenses

        :param payload: Sync license
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/msla/licenses/sync", payload=payload, **kw
        )
