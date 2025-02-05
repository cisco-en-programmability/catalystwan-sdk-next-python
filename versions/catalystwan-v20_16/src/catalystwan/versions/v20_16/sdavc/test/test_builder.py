# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class TestBuilder:
    """
    Builds and executes requests for operations under /sdavc/test
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def test_load_balancer(self, **kw):
        """
        Test SD_AVC load balancer

        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/sdavc/test", **kw)
