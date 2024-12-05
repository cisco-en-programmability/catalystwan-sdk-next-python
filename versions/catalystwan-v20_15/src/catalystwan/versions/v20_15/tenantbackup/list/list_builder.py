# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class ListBuilder:
    """
    Builds and executes requests for operations under /tenantbackup/list
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_tenant_backup(self, **kw) -> Any:
        """
        List all backup files of a tenant stored in vManage


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/tenantbackup/list", **kw)
