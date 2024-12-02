# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .detail.detail_builder import DetailBuilder


class TlocutilBuilder:
    """
    Builds and executes requests for operations under /device/tlocutil
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_tloc_util(self, site_id: Optional[str] = None, **kw) -> Any:
        """
        Get TLOC list

        :param site_id: Optional site ID  to filter devices
        :returns: Any
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/tlocutil", params=params, **kw
        )

    @property
    def detail(self) -> DetailBuilder:
        """
        The detail property
        """
        from .detail.detail_builder import DetailBuilder

        return DetailBuilder(self._request_adapter)
