# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeviceIp, GenerateDeactivateInfo


class DeactivateBuilder:
    """
    Builds and executes requests for operations under /device/action/deactivate
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_deactivate_info(self, device_id: List[DeviceIp], **kw) -> GenerateDeactivateInfo:
        """
        Get deactivate partition information

        :param device_id: deviceId - Device IP
        :returns: GenerateDeactivateInfo
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/deactivate",
            return_type=GenerateDeactivateInfo,
            params=params,
            **kw,
        )

    def process_deactivate_smu(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process deactivate operation for smu image

        :param payload: Device smu image deactivate request
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/deactivate", payload=payload, **kw
        )
