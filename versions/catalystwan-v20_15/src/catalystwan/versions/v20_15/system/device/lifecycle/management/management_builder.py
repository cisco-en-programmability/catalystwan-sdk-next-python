# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import SetLifeCycle


class ManagementBuilder:
    """
    Builds and executes requests for operations under /system/device/lifecycle/management
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def set_life_cycle(
        self, uuid: str, enable: Optional[bool] = None, **kw
    ) -> SetLifeCycle:
        """
        Set device lifecycle needed flag

        :param uuid: Device uuid
        :param enable: Enable
        :returns: SetLifeCycle
        """
        params = {
            "uuid": uuid,
            "enable": enable,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/system/device/lifecycle/management/{uuid}",
            return_type=SetLifeCycle,
            params=params,
            **kw,
        )
