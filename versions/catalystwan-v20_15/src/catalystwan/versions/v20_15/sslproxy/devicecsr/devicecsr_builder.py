# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DevicecsrBuilder:
    """
    Builds and executes requests for operations under /sslproxy/devicecsr
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_device_csr(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Get CSR for all cEdges

        :param payload: Device list
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/devicecsr", payload=payload, **kw
        )
