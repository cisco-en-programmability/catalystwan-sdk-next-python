# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import CloudTypeParam, GetRegions


class RegionsBuilder:
    """
    Builds and executes requests for operations under /multicloud/regions
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_regions(self, cloud_type: Optional[CloudTypeParam] = None, **kw) -> List[GetRegions]:
        """
        Obtain all supported Cloud Service Provider (CSP) types

        :param cloud_type: Cloud type
        :returns: List[GetRegions]
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/regions", return_type=List[GetRegions], params=params, **kw
        )
