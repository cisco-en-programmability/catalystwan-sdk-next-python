# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import GenerateDeviceActionListInner


class ListBuilder:
    """
    Builds and executes requests for operations under /device/action/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_device_action_list(self, **kw) -> List[GenerateDeviceActionListInner]:
        """
        Get device action list

        :returns: List[GenerateDeviceActionListInner]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/list",
            return_type=List[GenerateDeviceActionListInner],
            **kw,
        )
