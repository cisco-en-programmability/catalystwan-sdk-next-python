# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import SpeedTestStatusResponse
from .models import Uuid


class DisableBuilder:
    """
    Builds and executes requests for operations under /stream/device/speed/disable
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def disable_speed_test_session(
        self, session_id: Uuid, **kw
    ) -> SpeedTestStatusResponse:
        """
        Disable speed test session

        :param session_id: sessionId
        :returns: SpeedTestStatusResponse
        """
        params = {
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/speed/disable/{sessionId}",
            return_type=SpeedTestStatusResponse,
            params=params,
            **kw,
        )
