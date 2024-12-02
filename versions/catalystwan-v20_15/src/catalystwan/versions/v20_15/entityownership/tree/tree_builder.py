# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class TreeBuilder:
    """
    Builds and executes requests for operations under /entityownership/tree
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def entity_ownership_info(self, **kw) -> Any:
        """
        Entity ownership info grouped by buckets

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/entityownership/tree", **kw
        )
