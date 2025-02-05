# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import PowerConsumptionDeviceResp


class DeviceBuilder:
    """
    Builds and executes requests for operations under /statistics/powerconsumption/device
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_power_consumption_device(
        self, payload: Optional[Any] = None, **kw
    ) -> PowerConsumptionDeviceResp:
        """
        Get Power Consumption Per Device stats

        :param payload: Stats query string
        :returns: PowerConsumptionDeviceResp
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/powerconsumption/device",
            return_type=PowerConsumptionDeviceResp,
            payload=payload,
            **kw,
        )
