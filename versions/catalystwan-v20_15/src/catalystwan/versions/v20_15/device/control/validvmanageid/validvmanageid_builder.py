# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class ValidvmanageidBuilder:
    """
    Builds and executes requests for operations under /device/control/validvmanageid
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_valid_v_manage_id_real_time(self, device_id: str, **kw) -> Any:
        """
        Get valid vManage from device (Real Time)

        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/control/validvmanageid", params=params, **kw
        )
