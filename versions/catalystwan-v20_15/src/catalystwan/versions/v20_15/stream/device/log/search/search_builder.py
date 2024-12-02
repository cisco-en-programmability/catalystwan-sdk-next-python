# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class SearchBuilder:
    """
    Builds and executes requests for operations under /stream/device/log/search
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def search_device_log(self):
        class search_device_log_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, session_id: str, payload: Optional[str] = None, **kw):
                """
                Search device log

                :param session_id: Session Id
                :param payload: Payload
                :returns: None
                """
                params = {
                    "sessionId": session_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/log/search/{sessionId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return search_device_log_(self._request_adapter)
