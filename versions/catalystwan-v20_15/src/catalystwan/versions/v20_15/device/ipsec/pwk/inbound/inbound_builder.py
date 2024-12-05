# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import RemoteTlocColorParam


class InboundBuilder:
    """
    Builds and executes requests for operations under /device/ipsec/pwk/inbound
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_i_psec_pwk_inbound_connections(
        self,
        device_id: str,
        remote_tloc_address: Optional[str] = None,
        remote_tloc_color: Optional[RemoteTlocColorParam] = None,
        local_tloc_color: Optional[RemoteTlocColorParam] = None,
        **kw,
    ) -> Any:
        """
        Get IPSEC pairwise key inbound entry from device

        :param remote_tloc_address: Remote TLOC address
        :param remote_tloc_color: Remote tloc color
        :param local_tloc_color: Local tloc color
        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "remote-tloc-address": remote_tloc_address,
            "remote-tloc-color": remote_tloc_color,
            "local-tloc-color": local_tloc_color,
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/ipsec/pwk/inbound", params=params, **kw)
