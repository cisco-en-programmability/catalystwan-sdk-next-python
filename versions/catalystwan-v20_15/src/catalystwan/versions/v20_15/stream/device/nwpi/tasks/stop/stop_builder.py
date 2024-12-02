# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import TasksStopResponsePayload


class StopBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/tasks/stop
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def task_stop(self, task_id: str, **kw) -> TasksStopResponsePayload:
        """
        Task Action - Stop

        :param task_id: taskId
        :returns: TasksStopResponsePayload
        """
        params = {
            "taskId": task_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/stream/device/nwpi/tasks/stop/{taskId}",
            return_type=TasksStopResponsePayload,
            params=params,
            **kw,
        )
