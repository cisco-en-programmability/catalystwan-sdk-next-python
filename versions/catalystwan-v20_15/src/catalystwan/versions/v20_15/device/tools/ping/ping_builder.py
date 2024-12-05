# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import PingRequest, PingResponse


class PingBuilder:
    """
    Builds and executes requests for operations under /device/tools/ping
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def ping_device(self):
        class ping_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_ip: str, payload: Optional[PingRequest] = None, **kw) -> PingResponse:
                """
                Ping device

                :param device_ip: Device IP
                :param payload: Ping parameter
                :returns: PingResponse
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/ping/{deviceIP}",
                    return_type=PingResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PingRequest:
                return PingRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PingRequest]:
                return PingRequest

        return ping_device_(self._request_adapter)
