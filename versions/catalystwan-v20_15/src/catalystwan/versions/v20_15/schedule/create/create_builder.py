# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class CreateBuilder:
    """
    Builds and executes requests for operations under /schedule/create
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def schedule_backup(self):
        class schedule_backup_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                create  backup scheduler config-db and statstics database with startDateTime and persist to config-db

                :param payload: schedule request information
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/schedule/create", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return schedule_backup_(self._request_adapter)
