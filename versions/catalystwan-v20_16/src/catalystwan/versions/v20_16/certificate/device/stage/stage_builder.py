# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class StageBuilder:
    """
    Builds and executes requests for operations under /certificate/device/stage
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def stage_device(self, payload: Optional[Any] = None, **kw) -> str:
        """
        Stop data traffic to device

        :param payload: Payload
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/certificate/device/stage", return_type=str, payload=payload, **kw
        )
