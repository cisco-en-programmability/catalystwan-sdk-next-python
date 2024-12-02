# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import CoreNetworkPolicyResponse


class CorenetworkpolicyBuilder:
    """
    Builds and executes requests for operations under /multicloud/corenetworkpolicy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cwan_core_network_policy(self, **kw) -> CoreNetworkPolicyResponse:
        """
        Get AWS Cloudwan core network policy

        :returns: CoreNetworkPolicyResponse
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/corenetworkpolicy",
            return_type=CoreNetworkPolicyResponse,
            **kw,
        )
