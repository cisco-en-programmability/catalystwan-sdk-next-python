# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ConfigBuilder:
    """
    Builds and executes requests for operations under /fedramp/dnssec/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def configure_dns_sec(self, payload: Optional[Any] = None, **kw):
        """
        Configure DNS-Sec

        :param payload: DNS sec config request
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/fedramp/dnssec/config", payload=payload, **kw
        )
