# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class FeaturesBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/cli/features
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        feature_type: Optional[str] = "config",
        **kw,
    ) -> Any:
        """
        GetSdroutingFeatureProfilesByFamilyAndType

        :param offset: Pagination offset
        :param limit: Pagination limit
        :param feature_type: feature type
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
            "featureType": feature_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/cli/features", params=params, **kw
        )
