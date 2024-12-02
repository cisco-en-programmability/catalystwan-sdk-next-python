# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import GetTenantManagementSystemIPsInner


class SystemipBuilder:
    """
    Builds and executes requests for operations under /system/device/tenant/management/systemip
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tenant_management_system_i_ps(
        self, **kw
    ) -> List[GetTenantManagementSystemIPsInner]:
        """
        Get management system IP


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: List[GetTenantManagementSystemIPsInner]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/system/device/tenant/management/systemip",
            return_type=List[GetTenantManagementSystemIPsInner],
            **kw,
        )
