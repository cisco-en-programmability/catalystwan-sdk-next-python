# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ConfigBuilder1:
    """
    Builds and executes requests for operations under /template/device/config/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_configuration_preview(self, payload: Optional[Any] = None, **kw) -> str:
        """
        Get device configuration


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Device template
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/device/config/config", return_type=str, payload=payload, **kw
        )
