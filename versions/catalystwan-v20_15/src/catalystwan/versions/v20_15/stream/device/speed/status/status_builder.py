# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import SpeedTestStatusResponse, Uuid


class StatusBuilder:
    """
    Builds and executes requests for operations under /stream/device/speed/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_speed_test_status(self, session_id: Uuid, **kw) -> SpeedTestStatusResponse:
        """
        Get speed test status

        :param session_id: sessionId
        :returns: SpeedTestStatusResponse
        """
        params = {
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/speed/status/{sessionId}",
            return_type=SpeedTestStatusResponse,
            params=params,
            **kw,
        )
