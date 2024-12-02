# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class StatusBuilder:
    """
    Builds and executes requests for operations under /stream/device/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_device_status(self):
        class process_device_status_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_uuid: str, payload: Optional[str] = None, **kw):
                """
                Get device status stream

                :param device_uuid: Device uuid
                :param payload: Payload
                :returns: None
                """
                params = {
                    "deviceUUID": device_uuid,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/status/{deviceUUID}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return process_device_status_(self._request_adapter)
