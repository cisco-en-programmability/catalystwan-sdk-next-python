# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class FieldsBuilder:
    """
    Builds and executes requests for operations under /device/dpi/device/fields
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_field_json(self, **kw) -> Any:
        """
        Get DPI field from device

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/device/dpi/device/fields", **kw)
