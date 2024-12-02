# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List
from catalystwan.abc import RequestAdapterInterface
from .models import GetTunnelsResponse
from .models import CloudTypeParam


class TunnelsBuilder:
    """
    Builds and executes requests for operations under /multicloud/tunnels
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tunnel_names(
        self, cloud_type: CloudTypeParam, cloud_gateway_name: str, **kw
    ) -> List[GetTunnelsResponse]:
        """
        Get the tunnels for cloudType

        :param cloud_type: Cloud type
        :param cloud_gateway_name: Cloud gateway name
        :returns: List[GetTunnelsResponse]
        """
        params = {
            "cloudType": cloud_type,
            "cloudGatewayName": cloud_gateway_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/tunnels/{cloudType}",
            return_type=List[GetTunnelsResponse],
            params=params,
            **kw,
        )
