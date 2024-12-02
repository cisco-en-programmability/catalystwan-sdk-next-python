# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class WebexBuilder:
    """
    Builds and executes requests for operations under /monitor/sdavccloudconnector/webex
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_webex_app_data(self, **kw) -> Any:
        """
        Get SD AVC App Rules for Webex

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/monitor/sdavccloudconnector/webex", **kw
        )
