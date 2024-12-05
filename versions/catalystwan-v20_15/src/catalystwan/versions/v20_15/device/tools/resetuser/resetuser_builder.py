# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ResetuserBuilder:
    """
    Builds and executes requests for operations under /device/tools/resetuser
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_reset_user(self, device_ip: str, payload: Optional[Any] = None, **kw):
        """
        Request reset user

        :param device_ip: Device IP
        :param payload: Device user reset
        :returns: None
        """
        params = {
            "deviceIP": device_ip,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/device/tools/resetuser/{deviceIP}", params=params, payload=payload, **kw
        )
