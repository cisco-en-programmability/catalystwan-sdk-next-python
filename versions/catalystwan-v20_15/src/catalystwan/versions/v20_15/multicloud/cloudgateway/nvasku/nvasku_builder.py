# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import NvaSkuListResponse


class NvaskuBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/nvasku
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_azure_nva_sku_resources(self, cloud_type: str, **kw) -> NvaSkuListResponse:
        """
        Get Azure NVA SKUs

        :param cloud_type: Multicloud provider type
        :returns: NvaSkuListResponse
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/cloudgateway/nvasku", return_type=NvaSkuListResponse, params=params, **kw
        )
