# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import LicenseDistribution


class LicensedDistributionDetailsBuilder:
    """
    Builds and executes requests for operations under /msla/monitoring/licensedDistributionDetails
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_license_distribution_details(self, **kw) -> LicenseDistribution:
        """
        Get all license distribution

        :returns: LicenseDistribution
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/msla/monitoring/licensedDistributionDetails",
            return_type=LicenseDistribution,
            **kw,
        )
