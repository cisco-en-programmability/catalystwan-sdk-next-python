# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any
from catalystwan.abc import RequestAdapterInterface
import logging


class SizeBuilder:
    """
    Builds and executes requests for operations under /template/cor/transitvpc/size
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_transit_vpc_supported_size(
        self, cloud_environment: str, cloudtype: Optional[str] = "AWS", **kw
    ) -> List[Any]:
        """
        Get transit VPC supported size

        :param cloudtype: Cloud type
        :param cloud_environment: Cloud environment
        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "getTransitVPCSupportedSize")
        params = {
            "cloudtype": cloudtype,
            "cloudEnvironment": cloud_environment,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/cor/transitvpc/size",
            return_type=List[Any],
            params=params,
            **kw,
        )
