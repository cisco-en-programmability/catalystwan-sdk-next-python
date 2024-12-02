# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class DefaultBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/default
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_default_system_pack(self, **kw):
        """
        Get all default protocol pack details

        :returns: None
        """
        return self._request_adapter.request(
            "GET", "/dataservice/sdavc/protocol-pack/default", **kw
        )
