# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class DcatenantownersBuilder:
    """
    Builds and executes requests for operations under /dca/dcatenantowners
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dca_tenant_owners(self, **kw) -> Any:
        """
        Get DCA tenant owners

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/dca/dcatenantowners", **kw
        )
