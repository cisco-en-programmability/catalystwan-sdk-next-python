# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class StatusBuilder:
    """
    Builds and executes requests for operations under /device/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_device_status(self, **kw) -> List[Any]:
        """
        Get devices status for vSmart,vBond,vEdge, and cEdge

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/status", return_type=List[Any], **kw
        )
