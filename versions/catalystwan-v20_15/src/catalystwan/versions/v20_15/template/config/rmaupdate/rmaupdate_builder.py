# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RmaupdateBuilder:
    """
    Builds and executes requests for operations under /template/config/rmaupdate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def rma_update(self, payload: Optional[Any] = None, **kw):
        """
        Update new device

        :param payload: Template config
        :returns: None
        """
        return self._request_adapter.request("PUT", "/dataservice/template/config/rmaupdate", payload=payload, **kw)
