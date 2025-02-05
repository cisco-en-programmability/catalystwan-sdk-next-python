# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import Alarm


class UuidBuilder:
    """
    Builds and executes requests for operations under /alarms/uuid
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_alarm_details(
        self, alarm_uuid: str, include_tenants: Optional[bool] = None, **kw
    ) -> List[Alarm]:
        """
        Get alarm details for given UUID

        :param alarm_uuid: Alarm UUID
        :param include_tenants: Specify whether the tenant alarms need to be visible or not from provider view.
        :returns: List[Alarm]
        """
        params = {
            "alarm_uuid": alarm_uuid,
            "includeTenants": include_tenants,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/alarms/uuid/{alarm_uuid}",
            return_type=List[Alarm],
            params=params,
            **kw,
        )
