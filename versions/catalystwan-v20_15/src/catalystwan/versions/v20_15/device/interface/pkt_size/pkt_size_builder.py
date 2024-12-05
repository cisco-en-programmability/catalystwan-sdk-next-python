# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import AfTypeParam, IfnameParam


class PktSizeBuilder:
    """
    Builds and executes requests for operations under /device/interface/pkt_size
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_interface_pkt_sizes(
        self,
        device_id: str,
        vpn_id: Optional[str] = None,
        ifname: Optional[IfnameParam] = None,
        af_type: Optional[AfTypeParam] = None,
        **kw,
    ) -> Any:
        """
        Get interface packet size

        :param vpn_id: VPN Id
        :param ifname: IF Name
        :param af_type: AF Type
        :param device_id: deviceId - Device IP
        :returns: Any
        """
        params = {
            "vpn-id": vpn_id,
            "ifname": ifname,
            "af-type": af_type,
            "deviceId": device_id,
        }
        return self._request_adapter.request("GET", "/dataservice/device/interface/pkt_size", params=params, **kw)
