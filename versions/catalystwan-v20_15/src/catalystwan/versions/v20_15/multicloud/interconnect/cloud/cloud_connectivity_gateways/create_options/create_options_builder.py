# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional
from catalystwan.abc import RequestAdapterInterface
from .models import InlineResponse20014
from .models import ConnectivityGatewayTypeParam


class CreateOptionsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways/create-options
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_connectivity_gateway_create_options(
        self,
        cloud_type: str,
        cloud_account_id: str,
        connectivity_gateway_type: Optional[ConnectivityGatewayTypeParam] = None,
        refresh: Optional[str] = "false",
        **kw,
    ) -> InlineResponse20014:
        """
        API to retrieve Cloud Connectivity Gateway create options.

        :param cloud_type: Cloud Provider Type
        :param cloud_account_id: Cloud account id
        :param connectivity_gateway_type: Cloud Connectivity Gateway Type
        :param refresh: Refresh
        :returns: InlineResponse20014
        """
        params = {
            "cloud-type": cloud_type,
            "cloud-account-id": cloud_account_id,
            "connectivity-gateway-type": connectivity_gateway_type,
            "refresh": refresh,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/cloud/{cloud-type}/cloud-connectivity-gateways/create-options",
            return_type=InlineResponse20014,
            params=params,
            **kw,
        )
