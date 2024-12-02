# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import GetControlConnections


class ControlBuilder:
    """
    Builds and executes requests for operations under /troubleshooting/control
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_control_connections(self, uuid: str, **kw) -> GetControlConnections:
        """
        Troubleshoot control connections

        :param uuid: Uuid
        :returns: GetControlConnections
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/troubleshooting/control/{uuid}",
            return_type=GetControlConnections,
            params=params,
            **kw,
        )
