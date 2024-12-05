# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class QuickconnectvariableBuilder:
    """
    Builds and executes requests for operations under /template/device/config/quickconnectvariable
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_quick_connect_variables(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get connection variables to be configured

        :param payload: Device List
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/device/config/quickconnectvariable", payload=payload, **kw
        )
