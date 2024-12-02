# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class ClearBuilder:
    """
    Builds and executes requests for operations under /alarms/clear
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def clear_stale_alarm(self):
        class clear_stale_alarm_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Clear the alarm for a specific UUID.

                :param payload: Clear Alarm
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/alarms/clear", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return clear_stale_alarm_(self._request_adapter)
