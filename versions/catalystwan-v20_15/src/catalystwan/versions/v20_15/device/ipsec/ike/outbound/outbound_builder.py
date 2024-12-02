# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class OutboundBuilder:
    """
    Builds and executes requests for operations under /device/ipsec/ike/outbound
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_ike_outbound_list(self, device_id: str, **kw) -> List[Any]:
        """
        Get IPsec IKE outbound connection list from device

        :param device_id: deviceId - Device IP
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/ipsec/ike/outbound",
            return_type=List[Any],
            params=params,
            **kw,
        )
