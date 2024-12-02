# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RemoveSessionsBuilder:
    """
    Builds and executes requests for operations under /admin/user/removeSessions
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def remove_sessions_1(self):
        class remove_sessions_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[List[Any]] = None, **kw) -> Any:
                """
                Remove sessions

                :param payload: User
                :returns: Any
                """
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/admin/user/removeSessions",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> List[Any]:
                return List[Any](*args, **kwargs)

            @property
            def payload_model(self) -> Type[List[Any]]:
                return List[Any]

        return remove_sessions_1_(self._request_adapter)
