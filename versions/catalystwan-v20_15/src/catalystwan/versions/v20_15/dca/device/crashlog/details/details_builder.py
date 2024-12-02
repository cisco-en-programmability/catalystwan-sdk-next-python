# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DetailsBuilder:
    """
    Builds and executes requests for operations under /dca/device/crashlog/details
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_crash_logs(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get crash log

        :param payload: Query string
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dca/device/crashlog/details", payload=payload, **kw
        )
