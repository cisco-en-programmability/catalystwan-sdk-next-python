# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class RateplansBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/rateplans
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_rate_plans_by_acct_id(self, account_id: str, **kw):
        """
        Get rate plans by account Id

        :param account_id: Account id
        :returns: None
        """
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/securedeviceonboarding/rateplans", params=params, **kw
        )
