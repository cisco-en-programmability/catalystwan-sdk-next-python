# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class UnpauseLocalArbitratorBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/unpauseLocalArbitrator
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def unpause_local_arbitrator(self, **kw) -> Any:
        """
        Unpause DR for Local Arbitrator

        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/disasterrecovery/unpauseLocalArbitrator", **kw)
