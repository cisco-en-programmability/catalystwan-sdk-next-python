# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import NPingRequest, NPingResponse


class NpingBuilder:
    """
    Builds and executes requests for operations under /device/tools/nping
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def nping_device(
        self, device_ip: str, payload: Optional[NPingRequest] = None, **kw
    ) -> NPingResponse:
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
