# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AlarmCount


class MarkviewedBuilder:
    """
    Builds and executes requests for operations under /alarms/markviewed
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def mark_alarms_as_viewed(self):
        class mark_alarms_as_viewed_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[AlarmCount]:
                """
                Mark alarms as acknowledged based on list of UUIDs.

                :param payload: Mark alarms as viewed
                :returns: List[AlarmCount]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/alarms/markviewed",
                    return_type=List[AlarmCount],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return mark_alarms_as_viewed_(self._request_adapter)
