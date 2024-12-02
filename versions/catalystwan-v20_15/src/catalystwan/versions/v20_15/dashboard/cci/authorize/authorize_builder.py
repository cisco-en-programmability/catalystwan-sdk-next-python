# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class AuthorizeBuilder:
    """
    Builds and executes requests for operations under /dashboard/cci/authorize
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def cci_authorize(self, **kw):
        """
        Login into CCI

        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dashboard/cci/authorize", **kw
        )
