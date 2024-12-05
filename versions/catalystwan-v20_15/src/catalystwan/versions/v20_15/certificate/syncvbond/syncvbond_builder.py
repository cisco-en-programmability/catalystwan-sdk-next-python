# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class SyncvbondBuilder:
    """
    Builds and executes requests for operations under /certificate/syncvbond
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def syncv_bond(self, **kw) -> str:
        """
        sync vManage UUID to all vBond

        :returns: str
        """
        return self._request_adapter.request("GET", "/dataservice/certificate/syncvbond", return_type=str, **kw)
