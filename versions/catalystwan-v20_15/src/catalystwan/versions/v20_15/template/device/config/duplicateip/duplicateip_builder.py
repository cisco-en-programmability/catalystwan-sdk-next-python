# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class DuplicateipBuilder:
    """
    Builds and executes requests for operations under /template/device/config/duplicateip
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_devices_with_duplicate_ip(self, payload: Optional[Any] = None, **kw) -> List[Any]:
        """
        Detects duplicate system IP from a list of devices


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param payload: Device list
        :returns: List[Any]
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/device/config/duplicateip", return_type=List[Any], payload=payload, **kw
        )
