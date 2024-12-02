# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class DeviceusageBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/{deviceUUID}/deviceusage
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_data_usage(self, device_uuid: str, **kw) -> str:
        """
        Get device data usage using device uuid

        :param device_uuid: DeviceUUID
        :returns: str
        """
        params = {
            "deviceUUID": device_uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/securedeviceonboarding/{deviceUUID}/deviceusage",
            return_type=str,
            params=params,
            **kw,
        )
