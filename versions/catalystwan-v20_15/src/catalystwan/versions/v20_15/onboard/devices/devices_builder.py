# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceDetailsData


class DevicesBuilder:
    """
    Builds and executes requests for operations under /onboard/devices
    """

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
            "GET", "/dataservice/onboard/devices", return_type=List[DeviceDetailsData], params=params, **kw
        )

    @property
    def manual_onboard_devices(self):
        class manual_onboard_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[DeviceDetailsData] = None, **kw) -> Any:
                """
                Manual Onboard added Device details

                :param payload: On board Devices
                :returns: Any
                """
                return self._request_adapter.request("POST", "/dataservice/onboard/devices", payload=payload, **kw)

            def create_payload(self, *args, **kwargs) -> DeviceDetailsData:
                return DeviceDetailsData(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeviceDetailsData]:
                return DeviceDetailsData

        return manual_onboard_devices_(self._request_adapter)
