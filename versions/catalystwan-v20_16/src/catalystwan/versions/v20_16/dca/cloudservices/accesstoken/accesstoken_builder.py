# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AccesstokenBuilder:
    """
    Builds and executes requests for operations under /dca/cloudservices/accesstoken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_access_token(self, **kw) -> Any:
        """
        Get DCA access token

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/dca/cloudservices/accesstoken", **kw
        )

    def store_access_token(self, payload: Optional[Any] = None, **kw):
        """
        Set DCA access token

        :param payload: DCA access token
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dca/cloudservices/accesstoken", payload=payload, **kw
        )
