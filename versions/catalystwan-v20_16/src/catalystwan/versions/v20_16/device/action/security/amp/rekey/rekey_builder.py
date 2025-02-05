# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RekeyBuilder:
    """
    Builds and executes requests for operations under /device/action/security/amp/rekey
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_amp_api_re_key(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Process amp api re-key operation

        :param payload: AMP API re-key request payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/security/amp/rekey", payload=payload, **kw
        )
