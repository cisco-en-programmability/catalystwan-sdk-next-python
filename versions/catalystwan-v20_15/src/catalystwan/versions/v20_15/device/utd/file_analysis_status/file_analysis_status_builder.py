# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class FileAnalysisStatusBuilder:
    """
    Builds and executes requests for operations under /device/utd/file-analysis-status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_utd_file_analysis_status(self, device_id: str, **kw) -> Any:
        """
        Get UTD file analysis status from device (Real Time)

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/utd/file-analysis-status", params=params, **kw
        )
