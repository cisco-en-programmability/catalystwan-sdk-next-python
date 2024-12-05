# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import EdgeTypeParam

if TYPE_CHECKING:
    from .credentials.credentials_builder import CredentialsBuilder


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/accounts/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_edge_accounts(self, edge_type: Optional[EdgeTypeParam] = None, **kw) -> Any:
        """
        Get all Multicloud edge accounts

        :param edge_type: Edge type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeAccounts")
        params = {
            "edgeType": edge_type,
        }
        return self._request_adapter.request("GET", "/dataservice/multicloud/accounts/edge", params=params, **kw)

    def validate_edge_account_add(self, payload: Optional[Any] = None, **kw):
        """
        Authenticate edge account credentials

        :param payload: Multicloud edge account info
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "validateEdgeAccountAdd")
        return self._request_adapter.request("POST", "/dataservice/multicloud/accounts/edge", payload=payload, **kw)

    def get_edge_account_details(self, account_id: str, **kw) -> Any:
        """
        Get edge account by account Id

        :param account_id: Edge Account Id
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeAccountDetails")
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/accounts/edge/{accountId}", params=params, **kw
        )

    def update_edge_account(self, account_id: str, payload: Optional[Any] = None, **kw):
        """
        Update Multicloud edge account

        :param account_id: Multicloud Edge Account Id
        :param payload: Multicloud edge account info
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "updateEdgeAccount")
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/multicloud/accounts/edge/{accountId}", params=params, payload=payload, **kw
        )

    def delete_edge_account(self, account_id: str, **kw):
        """
        Delete edge account

        :param account_id: Edge Account Id
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "deleteEdgeAccount")
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/multicloud/accounts/edge/{accountId}", params=params, **kw
        )

    @property
    def credentials(self) -> CredentialsBuilder:
        """
        The credentials property
        """
        from .credentials.credentials_builder import CredentialsBuilder

        return CredentialsBuilder(self._request_adapter)
