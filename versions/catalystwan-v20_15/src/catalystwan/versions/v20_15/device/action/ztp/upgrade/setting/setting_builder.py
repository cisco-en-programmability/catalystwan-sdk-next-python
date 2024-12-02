# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class SettingBuilder:
    """
    Builds and executes requests for operations under /device/action/ztp/upgrade/setting
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_ztp_upgrade_config_setting(self, **kw):
        """
        Get ZTP upgrade configuration setting

        :returns: None
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/ztp/upgrade/setting", **kw
        )

    def process_ztp_upgrade_config_setting(self, payload: Optional[Any] = None, **kw):
        """
        Process ZTP upgrade configuration setting

        :param payload: Request body for Device bootstrap configuration
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/ztp/upgrade/setting", payload=payload, **kw
        )
