# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import SyncStatusResponse


class SyncstatusBuilder:
    """
    Builds and executes requests for operations under /webex/datacenter/syncstatus
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_webex_data_centers_sync_status(self, **kw) -> SyncStatusResponse:
        """
        Get webex data center sync status from DB

        :returns: SyncStatusResponse
        """
        return self._request_adapter.request(
            "GET", "/dataservice/webex/datacenter/syncstatus", return_type=SyncStatusResponse, **kw
        )

    def set_webex_data_centers_sync_status(self, **kw) -> bool:
        """
        Set webex data center sync needed            to false

        :returns: bool
        """
        return self._request_adapter.request("PUT", "/dataservice/webex/datacenter/syncstatus", return_type=bool, **kw)
