# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
from .models import PeerTypeParam


class ConnectionsBuilder:
    """
    Builds and executes requests for operations under /device/control/connections
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_real_time_connection_list(
        self,
        device_id: str,
        peer_type: Optional[PeerTypeParam] = None,
        system_ip: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get connections list from device (Real Time)

        :param peer_type: Peer type
        :param system_ip: Peer system IP
        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "peer-type": peer_type,
            "system-ip": system_ip,
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/control/connections", params=params, **kw
        )
