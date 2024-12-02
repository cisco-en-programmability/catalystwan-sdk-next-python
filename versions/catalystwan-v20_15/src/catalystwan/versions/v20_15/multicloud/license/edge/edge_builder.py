# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam
from .models import ProductTypeParam


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/license/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_licenses(
        self,
        edge_type: Optional[EdgeTypeParam] = None,
        account_id: Optional[str] = None,
        product_type: Optional[ProductTypeParam] = None,
        refresh: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get License Info for Edge Gateways/Connections

        :param edge_type: Edge type
        :param account_id: Edge Account Id
        :param product_type: product Type
        :param refresh: Refresh License Cache from Megaport
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getLicenses")
        params = {
            "edgeType": edge_type,
            "accountId": account_id,
            "productType": product_type,
            "refresh": refresh,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/license/edge", params=params, **kw
        )
