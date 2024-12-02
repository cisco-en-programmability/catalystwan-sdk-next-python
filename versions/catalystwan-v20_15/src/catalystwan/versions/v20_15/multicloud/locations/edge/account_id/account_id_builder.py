# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam


class AccountIdBuilder:
    """
    Builds and executes requests for operations under /multicloud/locations/edge/{edgeType}/accountId
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_edge_locations_info(
        self, edge_type: EdgeTypeParam, account_id: str, **kw
    ) -> Any:
        """
        Update Edge Locations

        :param edge_type: Edge Type
        :param account_id: Edge Account Id
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "updateEdgeLocationsInfo")
        params = {
            "edgeType": edge_type,
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/multicloud/locations/edge/{edgeType}/accountId/{accountId}",
            params=params,
            **kw,
        )
