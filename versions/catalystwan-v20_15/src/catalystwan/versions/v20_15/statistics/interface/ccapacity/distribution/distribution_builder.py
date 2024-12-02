# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import CapacityResp


class DistributionBuilder:
    """
    Builds and executes requests for operations under /statistics/interface/ccapacity/distribution
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_bandwidth_distribution(
        self, site_id: Optional[str] = None, **kw
    ) -> CapacityResp:
        """
        Get bandwidth distribution

        :param site_id: Site id
        :returns: CapacityResp
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/interface/ccapacity/distribution",
            return_type=CapacityResp,
            params=params,
            **kw,
        )
