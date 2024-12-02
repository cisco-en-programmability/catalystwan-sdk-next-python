# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceAppDetailResponse


class ApplicationsBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/device/details/applications
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_device_app_details(self, query: str, **kw) -> DeviceAppDetailResponse:
        """
        Get detailed DPI device and application list

        :param query: Query
        :returns: DeviceAppDetailResponse
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/dpi/device/details/applications",
            return_type=DeviceAppDetailResponse,
            params=params,
            **kw,
        )
