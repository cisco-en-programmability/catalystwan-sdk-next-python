# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import CloudTypeParam


class CloudgatewaytypeBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgatewaytype
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cgw_types(self, cloud_type: Optional[CloudTypeParam] = None, **kw) -> Any:
        """
        Get cloud gateway types for specified cloudType

        :param cloud_type: Cloud type
        :returns: Any
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/cloudgatewaytype", params=params, **kw
        )
