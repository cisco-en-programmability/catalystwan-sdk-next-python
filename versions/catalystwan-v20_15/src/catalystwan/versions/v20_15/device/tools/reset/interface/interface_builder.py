# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import ResetInterfaceReq


class InterfaceBuilder:
    """
    Builds and executes requests for operations under /device/tools/reset/interface
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_interface_reset(self):
        class process_interface_reset_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, device_ip: str, payload: Optional[ResetInterfaceReq] = None, **kw
            ):
                """
                Reset device interface

                :param device_ip: Device IP
                :param payload: Device interface
                :returns: None
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/reset/interface/{deviceIP}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ResetInterfaceReq:
                return ResetInterfaceReq(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ResetInterfaceReq]:
                return ResetInterfaceReq

        return process_interface_reset_(self._request_adapter)
