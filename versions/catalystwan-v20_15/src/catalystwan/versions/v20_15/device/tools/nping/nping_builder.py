# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import NPingRequest, NPingResponse


class NpingBuilder:
    """
    Builds and executes requests for operations under /device/tools/nping
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def nping_device(self):
        class nping_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_ip: str, payload: Optional[NPingRequest] = None, **kw) -> NPingResponse:
                """
                NPing device

                :param device_ip: Device IP
                :param payload: Ping parameter
                :returns: NPingResponse
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/nping/{deviceIP}",
                    return_type=NPingResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> NPingRequest:
                return NPingRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NPingRequest]:
                return NPingRequest

        return nping_device_(self._request_adapter)
