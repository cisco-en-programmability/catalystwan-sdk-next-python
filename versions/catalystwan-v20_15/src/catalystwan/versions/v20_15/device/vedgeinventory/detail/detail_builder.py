# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import VedgeInventoryData


class DetailBuilder:
    """
    Builds and executes requests for operations under /device/vedgeinventory/detail
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vedge_inventory(
        self, status: Optional[str] = None, **kw
    ) -> VedgeInventoryData:
        """
        Get detailed vEdge inventory

        :param status: Status
        :returns: VedgeInventoryData
        """
        params = {
            "status": status,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/vedgeinventory/detail",
            return_type=VedgeInventoryData,
            params=params,
            **kw,
        )
