# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import PackagingDistribution


class PackagingDistributionDetailsBuilder:
    """
    Builds and executes requests for operations under /msla/monitoring/packagingDistributionDetails
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_packaging_distribution_details(self, **kw) -> PackagingDistribution:
        """
        Get all license distribution

        :returns: PackagingDistribution
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/msla/monitoring/packagingDistributionDetails",
            return_type=PackagingDistribution,
            **kw,
        )
