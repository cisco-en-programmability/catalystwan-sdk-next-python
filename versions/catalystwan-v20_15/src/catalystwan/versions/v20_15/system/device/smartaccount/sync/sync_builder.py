# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import SyncDevicesResp


class SyncBuilder:
    """
    Builds and executes requests for operations under /system/device/smartaccount/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_devices(self, payload: Optional[Any] = None, **kw) -> SyncDevicesResp:
        """
        Sync devices from Smart-Account

        :param payload: Request body for Sync devices from Smart-Account
        :returns: SyncDevicesResp
        """
        return self._request_adapter.request(
            "POST", "/dataservice/system/device/smartaccount/sync", return_type=SyncDevicesResp, payload=payload, **kw
        )
