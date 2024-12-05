# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceDetailsData


class DetailsBuilder:
    """
    Builds and executes requests for operations under /onboard/details
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_devices(self):
        class add_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[DeviceDetailsData] = None, **kw):
                """
                Add Manual Onboard Device details

                :param payload: On board Device details
                :returns: None
                """
                return self._request_adapter.request("POST", "/dataservice/onboard/details", payload=payload, **kw)

            def create_payload(self, *args, **kwargs) -> DeviceDetailsData:
                return DeviceDetailsData(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeviceDetailsData]:
                return DeviceDetailsData

        return add_devices_(self._request_adapter)
