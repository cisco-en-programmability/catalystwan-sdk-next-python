# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DeleteBuilder:
    """
    Builds and executes requests for operations under /tenant/{tenantId}/delete
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def delete_tenant(self, tenant_id: str, payload: Optional[Any] = None, **kw):
        """
        Delete a tenant by Id


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param tenant_id: Tenant Id
        :param payload: Tenant model
        :returns: None
        """
        params = {
            "tenantId": tenant_id,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/tenant/{tenantId}/delete", params=params, payload=payload, **kw
        )
