# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import TracerouteResponse
from .models import TracerouteRequest


class TracerouteBuilder:
    """
    Builds and executes requests for operations under /device/tools/traceroute
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def traceroute_device(self):
        class traceroute_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, device_ip: str, payload: Optional[TracerouteRequest] = None, **kw
            ) -> TracerouteResponse:
                """
                Traceroute

                :param device_ip: Device IP
                :param payload: Traceroute parameter
                :returns: TracerouteResponse
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/traceroute/{deviceIP}",
                    return_type=TracerouteResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> TracerouteRequest:
                return TracerouteRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[TracerouteRequest]:
                return TracerouteRequest

        return traceroute_device_(self._request_adapter)
