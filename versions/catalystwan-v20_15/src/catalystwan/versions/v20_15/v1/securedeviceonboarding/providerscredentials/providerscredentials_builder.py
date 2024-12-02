# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class ProviderscredentialsBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/providerscredentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_accounts(self, **kw):
        """
        Get all providers credentials

        :returns: None
        """
        return self._request_adapter.request(
            "GET", "/dataservice/v1/securedeviceonboarding/providerscredentials", **kw
        )
