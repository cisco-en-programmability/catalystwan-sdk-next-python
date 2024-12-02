# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import TypeParam


class AttachedBuilder:
    """
    Builds and executes requests for operations under /template/config/attached
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_attached_config(
        self, device_id: str, type_: Optional[TypeParam] = "CFS", **kw
    ) -> Any:
        """
        Get local template attached config for given device

        :param device_id: Device Model ID
        :param type_: Config type
        :returns: Any
        """
        params = {
            "deviceId": device_id,
            "type": type_,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/config/attached/{deviceId}",
            params=params,
            **kw,
        )
