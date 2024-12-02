# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class LinkStateAlarmBuilder:
    """
    Builds and executes requests for operations under /alarms/link-state-alarm
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_link_state_alarm_config(self, **kw) -> str:
        """
        Get configuration for link-state alarm

        :returns: str
        """
        return self._request_adapter.request(
            "GET", "/dataservice/alarms/link-state-alarm", return_type=str, **kw
        )

    def enable_disable_link_state_alarm(self, link_name: str, enable: bool, **kw):
        """
        Enable/Disable a specific link-state alarm

        :param link_name: Link Name
        :param enable: Enable
        :returns: None
        """
        params = {
            "linkName": link_name,
            "enable": enable,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/alarms/link-state-alarm", params=params, **kw
        )
