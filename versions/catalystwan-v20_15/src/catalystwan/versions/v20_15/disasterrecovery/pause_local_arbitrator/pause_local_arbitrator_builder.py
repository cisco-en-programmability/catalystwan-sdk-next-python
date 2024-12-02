# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class PauseLocalArbitratorBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/pauseLocalArbitrator
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def pause_local_arbitrator(self, **kw) -> Any:
        """
        Pause DR for Local Arbitrator

        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/disasterrecovery/pauseLocalArbitrator", **kw
        )
