# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class ListBuilder:
    """
    Builds and executes requests for operations under /certificate/vsmart/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def getv_smart_list(self, **kw) -> str:
        """
        get vSmart list

        :returns: str
        """
        return self._request_adapter.request(
            "GET", "/dataservice/certificate/vsmart/list", return_type=str, **kw
        )

    def setv_smart_list(self, **kw) -> str:
        """
        save vSmart List(handleSendToVbond)

        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/certificate/vsmart/list", return_type=str, **kw
        )
