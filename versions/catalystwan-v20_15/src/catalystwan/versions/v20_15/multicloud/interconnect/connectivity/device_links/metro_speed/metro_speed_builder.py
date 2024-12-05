# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InlineResponse20012, InterconnectDeviceLink, InterconnectTypeParam


class MetroSpeedBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/{interconnect-type}/connectivity/device-links/metro-speed
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_interconnect_device_link_metro_speed(self):
        class get_interconnect_device_link_metro_speed_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, interconnect_type: InterconnectTypeParam, payload: Optional[InterconnectDeviceLink] = None, **kw
            ) -> InlineResponse20012:
                """
                API to get metro speed for Device-Link by Device-Link Configuration.

                :param interconnect_type: Interconnect Provider Type
                :param payload: Request Payload for Multicloud Interconnect Device Links
                :returns: InlineResponse20012
                """
                params = {
                    "interconnect-type": interconnect_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/interconnect/{interconnect-type}/connectivity/device-links/metro-speed",
                    return_type=InlineResponse20012,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectDeviceLink:
                return InterconnectDeviceLink(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectDeviceLink]:
                return InterconnectDeviceLink

        return get_interconnect_device_link_metro_speed_(self._request_adapter)
