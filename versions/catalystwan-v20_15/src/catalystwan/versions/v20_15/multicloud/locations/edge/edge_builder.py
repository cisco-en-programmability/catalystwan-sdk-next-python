# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam

if TYPE_CHECKING:
    from .account_id.account_id_builder import AccountIdBuilder


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/locations/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_edge_locations_info(
        self,
        edge_type: EdgeTypeParam,
        account_id: Optional[str] = None,
        region: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get Edge Locations

        :param edge_type: Edge Type
        :param account_id: Edge Account Id
        :param region: Region
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeLocationsInfo")
        params = {
            "edgeType": edge_type,
            "accountId": account_id,
            "region": region,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/locations/edge/{edgeType}",
            params=params,
            **kw,
        )

    def delete_edge_account_1(self, edge_type: EdgeTypeParam, **kw):
        """
        Delete edge account

        :param edge_type: Edge Type
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "deleteEdgeAccount_1")
        params = {
            "edgeType": edge_type,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/locations/edge/{edgeType}",
            params=params,
            **kw,
        )

    @property
    def account_id(self) -> AccountIdBuilder:
        """
        The accountId property
        """
        from .account_id.account_id_builder import AccountIdBuilder

        return AccountIdBuilder(self._request_adapter)
