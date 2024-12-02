# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class ApproutepolicyfilterBuilder:
    """
    Builds and executes requests for operations under /device/policy/approutepolicyfilter
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_policy_app_route_policy_filter(self, device_id: str, **kw) -> Any:
        """
        Get approute policy filter from device

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/policy/approutepolicyfilter", params=params, **kw
        )
