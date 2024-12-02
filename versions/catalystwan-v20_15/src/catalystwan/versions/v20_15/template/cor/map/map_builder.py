# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class MapBuilder:
    """
    Builds and executes requests for operations under /template/cor/map
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_mapped_vp_cs(self, accountid: str, cloudregion: str, **kw) -> Any:
        """
        Get mapped VPC/VNet list

        :param accountid: Account Id
        :param cloudregion: Cloud region
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getMappedVPCs")
        params = {
            "accountid": accountid,
            "cloudregion": cloudregion,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/cor/map", params=params, **kw
        )

    def map_vp_cs(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Map host to transit VPC/VNet

        :param payload: Map host to VPC/VNet
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "mapVPCs")
        return self._request_adapter.request(
            "POST", "/dataservice/template/cor/map", payload=payload, **kw
        )

    def unmap_vp_cs(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Unmap host from transit VPC/VNet

        :param payload: Unmap host to VPC/VNet
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "unmapVPCs")
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/cor/map", payload=payload, **kw
        )
