# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import DeviceIp

if TYPE_CHECKING:
    from .site.site_builder import SiteBuilder


class DeviceBuilder:
    """
    Builds and executes requests for operations under /topology/device
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_device_topology(self, device_id: List[DeviceIp], **kw) -> Any:
        """
        Create device topology

        :param device_id: Device Id list
        :returns: Any
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/topology/device", params=params, **kw
        )

    @property
    def site(self) -> SiteBuilder:
        """
        The site property
        """
        from .site.site_builder import SiteBuilder

        return SiteBuilder(self._request_adapter)
