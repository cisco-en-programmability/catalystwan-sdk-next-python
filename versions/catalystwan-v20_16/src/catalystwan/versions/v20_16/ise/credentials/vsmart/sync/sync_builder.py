# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import VsmartSyncResponse


class SyncBuilder:
    """
    Builds and executes requests for operations under /ise/credentials/vsmart/sync
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_vsmart(self, **kw) -> VsmartSyncResponse:
        """
        Send pxGrid and ISE server configuration to vSmarts

        :returns: VsmartSyncResponse
        """
        return self._request_adapter.request(
            "POST", "/dataservice/ise/credentials/vsmart/sync", return_type=VsmartSyncResponse, **kw
        )
