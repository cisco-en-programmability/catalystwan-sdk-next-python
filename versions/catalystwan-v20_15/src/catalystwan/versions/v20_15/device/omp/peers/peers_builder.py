# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class PeersBuilder:
    """
    Builds and executes requests for operations under /device/omp/peers
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_omp_session_list(self, device_id: str, **kw) -> List[Any]:
        """
        Get OMP session list (Real Time)

        :param device_id: deviceId - Device IP
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/omp/peers",
            return_type=List[Any],
            params=params,
            **kw,
        )
