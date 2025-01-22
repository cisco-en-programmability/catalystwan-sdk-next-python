# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AlarmCount


class MarkviewedBuilder:
    """
    Builds and executes requests for operations under /alarms/markviewed
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def mark_alarms_as_viewed(self, payload: Optional[Any] = None, **kw) -> List[AlarmCount]:
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
