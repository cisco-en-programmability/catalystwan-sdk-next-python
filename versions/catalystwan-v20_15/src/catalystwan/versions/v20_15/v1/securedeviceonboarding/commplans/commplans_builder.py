# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class CommplansBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/{accountId}/commplans
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_comm_plans_by_acct_id(self, account_id: str, **kw):
        """
        Get communication plans by account Id

        :param account_id: Service User Account ID
        :returns: None
        """
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/securedeviceonboarding/{accountId}/commplans",
            params=params,
            **kw,
        )
