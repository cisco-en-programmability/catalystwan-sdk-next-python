# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class SyncedBuilder:
    """
    Builds and executes requests for operations under /device/software/synced
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_synced_software_list(self, device_id: str, **kw) -> List[Any]:
        """
        Get software list from device synchronously

        :param device_id: deviceId - Device IP
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/software/synced",
            return_type=List[Any],
            params=params,
            **kw,
        )
