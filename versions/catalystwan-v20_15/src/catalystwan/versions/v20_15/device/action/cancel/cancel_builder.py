# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CancelBuilder:
    """
    Builds and executes requests for operations under /device/action/cancel
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_cancel_task(self, payload: Optional[Any] = None, **kw):
        """
        Cancel tasks

        :param payload: Request body for Device bootstrap configuration
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/cancel", payload=payload, **kw
        )
