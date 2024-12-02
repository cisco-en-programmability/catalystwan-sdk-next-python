# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class CloudxBuilder:
    """
    Builds and executes requests for operations under /device/omp/cloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_omp_cloud_x_recv(self, device_id: str, **kw) -> List[Any]:
        """
        Get CloudExpress routes received list

        :param device_id: deviceId - Device IP
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/omp/cloudx",
            return_type=List[Any],
            params=params,
            **kw,
        )
