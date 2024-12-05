# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceIp

if TYPE_CHECKING:
    from .devices.devices_builder import DevicesBuilder


class InstallBuilder:
    """
    Builds and executes requests for operations under /device/action/install
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_install_info(self, device_id: List[DeviceIp], **kw):
        """
        Generate install info

        :param device_id: deviceId - Device IP
        :returns: None
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/action/install", params=params, **kw)

    def process_install(self, payload: Optional[Any] = None, **kw):
        """
        Process an installation operation

        :param payload: Request body for Device bootstrap configuration
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/device/action/install", payload=payload, **kw)

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)
