# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class LockUserBuilder:
    """
    Builds and executes requests for operations under /admin/user/lockUser
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def lock_user(self, user_name: str, payload: Optional[Any] = None, **kw):
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
