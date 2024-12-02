# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class IscreatedBuilder:
    """
    Builds and executes requests for operations under /system/device/selfsignedcert/iscreated
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def check_self_signed_cert_1(self, **kw) -> Any:
        """
        Whether self signed certificate created

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/system/device/selfsignedcert/iscreated", **kw
        )
