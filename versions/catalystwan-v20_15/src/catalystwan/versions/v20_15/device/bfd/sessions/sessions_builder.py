# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any
from catalystwan.abc import RequestAdapterInterface
from .models import ColorParam
from .models import RegionTypeParam


class SessionsBuilder:
    """
    Builds and executes requests for operations under /device/bfd/sessions
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_bfd_sessions(
        self,
        device_id: str,
        system_ip: Optional[str] = None,
        color: Optional[ColorParam] = None,
        local_color: Optional[ColorParam] = None,
        region_type: Optional[RegionTypeParam] = None,
        **kw,
    ) -> List[Any]:
        """
        Get list of BFD sessions from vManage (Real Time)

        :param system_ip: System IP
        :param color: Remote color
        :param local_color: Source color
        :param region_type: Region type
        :param device_id: deviceId - Device IP
        :returns: List[Any]
        """
        params = {
            "system-ip": system_ip,
            "color": color,
            "local-color": local_color,
            "region-type": region_type,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/bfd/sessions",
            return_type=List[Any],
            params=params,
            **kw,
        )
