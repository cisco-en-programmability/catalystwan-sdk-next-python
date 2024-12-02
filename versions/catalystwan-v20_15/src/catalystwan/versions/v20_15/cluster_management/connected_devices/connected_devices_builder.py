# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List

from catalystwan.abc import RequestAdapterInterface


class ConnectedDevicesBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/connectedDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_connected_devices(self, vmanage_ip: str, **kw) -> List[Any]:
        """
        Get connected device for vManage


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param vmanage_ip: vManage IP
        :returns: List[Any]
        """
        params = {
            "vmanageIP": vmanage_ip,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/clusterManagement/connectedDevices/{vmanageIP}",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def get_connected_devices_per_tenant(
        self, tenant_id: str, vmanage_ip: str, **kw
    ) -> List[Any]:
        """
        Get connected device for vManage for a tenant


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param tenant_id: Tenant Id
        :param vmanage_ip: vManage IP
        :returns: List[Any]
        """
        params = {
            "tenantId": tenant_id,
            "vmanageIP": vmanage_ip,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}",
            return_type=List[Any],
            params=params,
            **kw,
        )
