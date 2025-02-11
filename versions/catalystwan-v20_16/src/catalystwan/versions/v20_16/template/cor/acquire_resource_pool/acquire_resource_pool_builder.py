# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AcquireResourcePoolBuilder:
    """
    Builds and executes requests for operations under /template/cor/acquireResourcePool
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def acquire_resource_pool(self, payload: Optional[Any] = None, **kw):
        """
        Acquire IP from resource pool

        :param payload: Add IP from resource pool request
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "acquireResourcePool")
        return self._request_adapter.request(
            "POST", "/dataservice/template/cor/acquireResourcePool", payload=payload, **kw
        )
