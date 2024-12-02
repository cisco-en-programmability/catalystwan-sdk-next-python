# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class LockUserBuilder:
    """
    Builds and executes requests for operations under /admin/user/lockUser
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def lock_user(self):
        class lock_user_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, user_name: str, payload: Optional[Any] = None, **kw):
                """
                Lock a user account

                :param user_name: User name
                :param payload: User
                :returns: None
                """
                params = {
                    "userName": user_name,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/admin/user/lockUser/{userName}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return lock_user_(self._request_adapter)
