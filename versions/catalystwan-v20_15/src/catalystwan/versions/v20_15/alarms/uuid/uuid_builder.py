# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import AlarmResponse


class UuidBuilder:
    """
    Builds and executes requests for operations under /alarms/uuid
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_alarm_details(self, alarm_uuid: str, **kw) -> AlarmResponse:
        """
        Get alarm details for given UUID

        :param alarm_uuid: Alarm UUID
        :returns: AlarmResponse
        """
        params = {
            "alarm_uuid": alarm_uuid,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/uuid/{alarm_uuid}", return_type=AlarmResponse, params=params, **kw
        )
