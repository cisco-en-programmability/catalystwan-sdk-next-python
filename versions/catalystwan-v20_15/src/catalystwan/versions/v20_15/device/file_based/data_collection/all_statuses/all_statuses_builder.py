# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class AllStatusesBuilder:
    """
    Builds and executes requests for operations under /device/file-based/data-collection/all-statuses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_data_collection_status_for_device(self, device_uuid: str, **kw) -> str:
        """
        Get Data Collection status for given Device UUID

        :param device_uuid: Device UUID
        :returns: str
        """
        params = {
            "deviceUUID": device_uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/file-based/data-collection/all-statuses/{deviceUUID}",
            return_type=str,
            params=params,
            **kw,
        )
