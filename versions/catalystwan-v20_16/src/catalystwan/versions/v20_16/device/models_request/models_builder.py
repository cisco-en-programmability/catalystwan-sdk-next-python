# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeviceModelsResponse


class ModelsBuilder:
    """
    Builds and executes requests for operations under /device/models
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_all_device_models(self, **kw) -> DeviceModelsResponse:
        """
        Get all device models supported by the vManage

        :returns: DeviceModelsResponse
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/models", return_type=DeviceModelsResponse, **kw
        )

    def get_device_models(self, uuid: str, **kw) -> Any:
        """
        Get device model for the device

        :param uuid: Device uuid
        :returns: Any
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/models/{uuid}", params=params, **kw
        )
