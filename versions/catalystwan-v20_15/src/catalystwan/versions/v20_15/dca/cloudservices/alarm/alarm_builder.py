# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AlarmBuilder:
    """
    Builds and executes requests for operations under /dca/cloudservices/alarm
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_alarm(self, payload: Optional[Any] = None, **kw):
        """
        Generate DCA alarms

        :param payload: DCA alarm message
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/dca/cloudservices/alarm", payload=payload, **kw)
