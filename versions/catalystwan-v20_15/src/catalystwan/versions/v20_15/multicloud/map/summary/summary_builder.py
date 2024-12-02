# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
from .models import MapSummary
from .models import CloudTypeParam


class SummaryBuilder:
    """
    Builds and executes requests for operations under /multicloud/map/summary
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_mapping_summary(
        self,
        cloud_type: Optional[CloudTypeParam] = None,
        vpn_tunnel_status: Optional[str] = None,
        **kw,
    ) -> List[MapSummary]:
        """
        Get mapping summary

        :param cloud_type: Cloud type
        :param vpn_tunnel_status: Vpn tunnel status
        :returns: List[MapSummary]
        """
        params = {
            "cloudType": cloud_type,
            "vpnTunnelStatus": vpn_tunnel_status,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/map/summary",
            return_type=List[MapSummary],
            params=params,
            **kw,
        )
