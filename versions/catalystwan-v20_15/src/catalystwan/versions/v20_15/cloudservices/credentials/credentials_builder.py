# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class CredentialsBuilder:
    """
    Builds and executes requests for operations under /cloudservices/credentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_credentials(self, **kw) -> Any:
        """
        Get cloud service credentials

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/cloudservices/credentials", **kw)

    def add_cloud_credentials(self, payload: Optional[Any] = None, **kw):
        """
        Add cloud service credentials

        :param payload: Cloud service credentials
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/cloudservices/credentials", payload=payload, **kw
        )
