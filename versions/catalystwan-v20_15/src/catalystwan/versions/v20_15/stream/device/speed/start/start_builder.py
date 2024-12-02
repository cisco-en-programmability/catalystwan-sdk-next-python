# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import SpeedTestStatusResponse
from .models import Uuid


class StartBuilder:
    """
    Builds and executes requests for operations under /stream/device/speed/start
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def start_speed_test(self, session_id: Uuid, **kw) -> SpeedTestStatusResponse:
        """
        Start speed test

        :param session_id: sessionId
        :returns: SpeedTestStatusResponse
        """
        params = {
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/speed/start/{sessionId}",
            return_type=SpeedTestStatusResponse,
            params=params,
            **kw,
        )
