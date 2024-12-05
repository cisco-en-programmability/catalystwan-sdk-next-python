# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RootcaBuilder:
    """
    Builds and executes requests for operations under /sslproxy/settings/enterprise/rootca
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_v_manage_enterprise_root_certificate(self, **kw) -> Any:
        """
        Get vManage enterprise root certificate

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/sslproxy/settings/enterprise/rootca", **kw)

    def set_enterprise_root_ca_cert(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Set vManage enterprise root certificate

        :param payload: Set enterprise root CA request
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sslproxy/settings/enterprise/rootca", payload=payload, **kw
        )
