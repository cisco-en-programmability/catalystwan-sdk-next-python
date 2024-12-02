# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class DefaultsiteBuilder:
    """
    Builds and executes requests for operations under /template/policy/list/site/defaultsite
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_default_site_list(self, **kw) -> Any:
        """
        Create default site list for sites missing from centralized policy

        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/list/site/defaultsite", **kw
        )
