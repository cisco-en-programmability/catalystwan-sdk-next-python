# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class OptinBuilder:
    """
    Builds and executes requests for operations under /cloudservices/telemetry/optin
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def opt_in(self, payload: Optional[str] = None, **kw) -> Any:
        """
        Telemetry Opt In

        :param payload: Payload
        :returns: Any
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/cloudservices/telemetry/optin", payload=payload, **kw
        )
