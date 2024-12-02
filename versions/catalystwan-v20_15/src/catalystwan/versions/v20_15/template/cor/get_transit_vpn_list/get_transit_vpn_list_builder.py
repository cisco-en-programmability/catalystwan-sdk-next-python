# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface
import logging


class GetTransitVpnListBuilder:
    """
    Builds and executes requests for operations under /template/cor/getTransitVpnList
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_transit_vpc_vpn_list(self, account_id: str, **kw) -> List[Any]:
        """
        Get transit VPN list

        :param account_id: Account Id
        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "getTransitVpcVpnList")
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/cor/getTransitVpnList",
            return_type=List[Any],
            params=params,
            **kw,
        )
