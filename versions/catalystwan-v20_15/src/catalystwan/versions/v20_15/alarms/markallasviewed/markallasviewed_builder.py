# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class MarkallasviewedBuilder:
    """
    Builds and executes requests for operations under /alarms/markallasviewed
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def mark_all_alarms_as_viewed(self):
        class mark_all_alarms_as_viewed_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, type_: Optional[str] = None, **kw
            ):
                """
                Mark all alarms as acknowledged by the user

                :param type_: Specify type. Allowed values: ["active", "cleared"]
                :param payload: Query
                :returns: None
                """
                params = {
                    "type": type_,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/alarms/markallasviewed",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return mark_all_alarms_as_viewed_(self._request_adapter)
