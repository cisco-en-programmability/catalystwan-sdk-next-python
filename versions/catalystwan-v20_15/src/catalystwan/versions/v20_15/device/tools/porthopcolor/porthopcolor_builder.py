# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class PorthopcolorBuilder:
    """
    Builds and executes requests for operations under /device/tools/porthopcolor
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_port_hop_color(self):
        class process_port_hop_color_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_ip: str, payload: Optional[Any] = None, **kw):
                """
                Request port hop color

                :param device_ip: Device IP
                :param payload: Device port hop color
                :returns: None
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/porthopcolor/{deviceIP}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_port_hop_color_(self._request_adapter)
