# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class StatusBuilder:
    """
    Builds and executes requests for operations under /stream/device/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_device_status(self, device_uuid: str, payload: Optional[str] = None, **kw):
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
