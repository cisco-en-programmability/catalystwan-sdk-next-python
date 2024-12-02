# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import IsVnetAttached


class VnetsNoofAttachedBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/vnetsNoofAttached
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_azure_virtual_vnets_attached(
        self, cloud_type: str, cloud_gateway_name: str, **kw
    ) -> IsVnetAttached:
        """
        Discover Azure Virtual HUBs

        :param cloud_type: Multicloud provider type
        :param cloud_gateway_name: Cloud gateway name
        :returns: IsVnetAttached
        """
        params = {
            "cloudType": cloud_type,
            "cloudGatewayName": cloud_gateway_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/cloudgateway/vnetsNoofAttached",
            return_type=IsVnetAttached,
            params=params,
            **kw,
        )
