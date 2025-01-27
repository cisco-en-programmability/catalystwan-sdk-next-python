# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeviceLists


class DeviceBuilder:
    """
    Builds and executes requests for operations under /security/policy/fwall/device
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_post_fwall_by_query(self, payload: Optional[Any] = None, **kw) -> List[DeviceLists]:
        """
        Get firewall devices list

        :param payload: Stats query string
        :returns: List[DeviceLists]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/security/policy/fwall/device",
            return_type=List[DeviceLists],
            payload=payload,
            **kw,
        )
