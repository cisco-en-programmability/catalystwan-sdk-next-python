# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeviceDetailsData


class DevicesBuilder:
    """
    Builds and executes requests for operations under /onboard/devices
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_devices(self, status: str, **kw) -> List[DeviceDetailsData]:
        """
        GET Manual Onboard Device details

        :param status: Status
        :returns: List[DeviceDetailsData]
        """
        params = {
            "status": status,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/onboard/devices",
            return_type=List[DeviceDetailsData],
            params=params,
            **kw,
        )

    def manual_onboard_devices(self, payload: Optional[DeviceDetailsData] = None, **kw) -> Any:
        """
        Manual Onboard added Device details

        :param payload: On board Devices
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/onboard/devices", payload=payload, **kw
        )
