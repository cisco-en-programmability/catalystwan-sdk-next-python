# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import SoftwareVersion


class AutonomousversionBuilder:
    """
    Builds and executes requests for operations under /device/autonomousversion
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_autonomous_software_version(self, device_id: str, **kw) -> SoftwareVersion:
        """
        Get Software version from device

        :param device_id: deviceId - Device IP
        :returns: SoftwareVersion
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/autonomousversion",
            return_type=SoftwareVersion,
            params=params,
            **kw,
        )
