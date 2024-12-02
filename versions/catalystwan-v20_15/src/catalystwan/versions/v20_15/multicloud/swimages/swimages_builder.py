# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
from .models import SwImagesResponse
from .models import CloudTypeParam


class SwimagesBuilder:
    """
    Builds and executes requests for operations under /multicloud/swimages
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_supported_software_image_list(
        self,
        cloud_type: CloudTypeParam,
        account_id: Optional[str] = None,
        cloud_region: Optional[str] = None,
        **kw,
    ) -> List[SwImagesResponse]:
        """
        Get software image list

        :param cloud_type: Cloud type
        :param account_id: Account id
        :param cloud_region: Cloud region
        :returns: List[SwImagesResponse]
        """
        params = {
            "cloudType": cloud_type,
            "accountId": account_id,
            "cloudRegion": cloud_region,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/swimages",
            return_type=List[SwImagesResponse],
            params=params,
            **kw,
        )
