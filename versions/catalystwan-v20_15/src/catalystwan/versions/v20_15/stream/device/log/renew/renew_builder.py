# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import Uuid


class RenewBuilder:
    """
    Builds and executes requests for operations under /stream/device/log/renew
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def renew_session_info(self, session_id: Uuid, **kw):
        """
        Renew session info

        :param session_id: Session id
        :returns: None
        """
        params = {
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/log/renew/{sessionId}",
            params=params,
            **kw,
        )
