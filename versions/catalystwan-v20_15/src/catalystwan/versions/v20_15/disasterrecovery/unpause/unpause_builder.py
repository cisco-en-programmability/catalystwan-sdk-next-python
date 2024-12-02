# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class UnpauseBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/unpause
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def unpause_dr(self, **kw) -> Any:
        """
        Unpause DR

        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/disasterrecovery/unpause", **kw
        )
