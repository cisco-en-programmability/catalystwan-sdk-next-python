# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ModeBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/tenancy/mode
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tenancy_mode(self, **kw) -> Any:
        """
        Get vManage tenancy mode


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/clusterManagement/tenancy/mode", **kw)

    def set_tenancy_mode(self, payload: Optional[Any] = None, **kw):
        """
        Update vManage tenancy mode

        :param payload: Tenancy mode setting
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/clusterManagement/tenancy/mode", payload=payload, **kw
        )
