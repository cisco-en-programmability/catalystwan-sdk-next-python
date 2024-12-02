# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import IfNameParam


class SessionsBuilder:
    """
    Builds and executes requests for operations under /device/cellular/sessions
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_sessions_list(
        self,
        device_id: str,
        if_name: Optional[IfNameParam] = None,
        ipv4_dns_pri: Optional[str] = None,
        **kw,
    ) -> List[Any]:
        """
        Get cellular session list from device

        :param if_name: Interface name
        :param ipv4_dns_pri: DNS primary IP
        :param device_id: Device IP
        :returns: List[Any]
        """
        params = {
            "if-name": if_name,
            "ipv4-dns-pri": ipv4_dns_pri,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/cellular/sessions",
            return_type=List[Any],
            params=params,
            **kw,
        )
