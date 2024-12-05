# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DefaultpartitionBuilder:
    """
    Builds and executes requests for operations under /device/action/defaultpartition
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_default_partition(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process marking default partition operation

        :param payload: Request body for Process marking default partition operation
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/defaultpartition", payload=payload, **kw
        )
