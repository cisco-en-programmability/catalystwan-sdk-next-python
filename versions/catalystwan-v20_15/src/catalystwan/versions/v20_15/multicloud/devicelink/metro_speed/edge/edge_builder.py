# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/devicelink/metroSpeed/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_link_metro_speed(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get Device Link Metro Speed based on device link config

        :param payload: Device Link
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getDeviceLinkMetroSpeed")
        return self._request_adapter.request(
            "POST", "/dataservice/multicloud/devicelink/metroSpeed/edge", payload=payload, **kw
        )
