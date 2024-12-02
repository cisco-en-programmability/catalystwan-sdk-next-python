# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import DeviceTaskStatus


class CleanBuilder:
    """
    Builds and executes requests for operations under /device/action/status/tasks/clean
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_clean_status(self, process_id: str, **kw) -> DeviceTaskStatus:
        """
        Delete task and status vertex

        :param process_id: Process Id
        :returns: DeviceTaskStatus
        """
        params = {
            "processId": process_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/status/tasks/clean",
            return_type=DeviceTaskStatus,
            params=params,
            **kw,
        )
