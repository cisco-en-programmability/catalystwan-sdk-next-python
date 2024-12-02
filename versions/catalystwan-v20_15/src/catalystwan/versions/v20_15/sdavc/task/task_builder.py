# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class TaskBuilder:
    """
    Builds and executes requests for operations under /sdavc/task
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def activate_container(self):
        class activate_container_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, task_id: str, payload: Optional[Any] = None, **kw):
                """
                Activate container

                :param task_id: Task Id
                :param payload: Container task config
                :returns: None
                """
                params = {
                    "taskId": task_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sdavc/task/{taskId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return activate_container_(self._request_adapter)
