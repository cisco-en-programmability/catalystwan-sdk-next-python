# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class SyncBuilder:
    """
    Builds and executes requests for operations under /template/cortex/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_wan_resource_groups(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Sync WAN Resource Groups

        :param payload: WAN resource group
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/template/cortex/sync", payload=payload, **kw)
