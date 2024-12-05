# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ReverseproxyBuilder:
    """
    Builds and executes requests for operations under /system/reverseproxy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_reverse_proxy_mappings(self, uuid: str, **kw) -> Any:
        """
        Get reverse proxy IP/Port mappings for controller

        :param uuid: Device uuid
        :returns: Any
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request("GET", "/dataservice/system/reverseproxy/{uuid}", params=params, **kw)

    def create_reverse_proxy_mappings(self, uuid: str, payload: Optional[Any] = None, **kw):
        """
        Create reverse proxy IP/Port mappings for controller

        :param uuid: Device uuid
        :param payload: Device reverse proxy mappings
        :returns: None
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/system/reverseproxy/{uuid}", params=params, payload=payload, **kw
        )
