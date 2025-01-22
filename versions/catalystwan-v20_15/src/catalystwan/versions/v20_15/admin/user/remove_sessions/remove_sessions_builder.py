# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class RemoveSessionsBuilder:
    """
    Builds and executes requests for operations under /admin/user/removeSessions
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def remove_sessions_1(self, payload: Optional[List[Any]] = None, **kw) -> Any:
        """
        Remove sessions

        :param payload: User
        :returns: Any
        """
        return self._request_adapter.request(
            "DELETE", "/dataservice/admin/user/removeSessions", payload=payload, **kw
        )
