# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import TaskHistoryResponsePayload


class TaskHistoryBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/tasks/taskHistory
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_task_history(self, **kw) -> TaskHistoryResponsePayload:
        """
        Get all the auto on tasks

        :returns: TaskHistoryResponsePayload
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/tasks/taskHistory",
            return_type=TaskHistoryResponsePayload,
            **kw,
        )
