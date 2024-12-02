# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class BifrostControllerRegistrationBuilder:
    """
    Builds and executes requests for operations under /dashboard/bifrostControllerRegistration
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def bifrost_controller_registration(self, **kw):
        """
        Register Controller to BiFrost Dashboard (by Controller)

        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dashboard/bifrostControllerRegistration", **kw
        )
