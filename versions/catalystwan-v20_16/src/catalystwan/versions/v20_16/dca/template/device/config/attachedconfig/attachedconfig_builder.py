# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AttachedconfigBuilder:
    """
    Builds and executes requests for operations under /dca/template/device/config/attachedconfig
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dca_attached_config_to_device(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get attached config to device

        :param payload: Query string
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dca/template/device/config/attachedconfig", payload=payload, **kw
        )
