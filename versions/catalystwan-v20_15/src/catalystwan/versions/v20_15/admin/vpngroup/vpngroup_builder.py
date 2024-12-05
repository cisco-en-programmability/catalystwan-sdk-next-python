# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class VpngroupBuilder:
    """
    Builds and executes requests for operations under /admin/vpngroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vpn_groups(self, **kw) -> List[Any]:
        """
        Get VPN groups

        :returns: List[Any]
        """
        return self._request_adapter.request("GET", "/dataservice/admin/vpngroup", return_type=List[Any], **kw)

    def create_vpn_group(self, payload: Optional[Any] = None, **kw):
        """
        Add VPN group

        :param payload: VPN group
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/admin/vpngroup", payload=payload, **kw)

    def edit_vpn_group(self, id: str, payload: Optional[Any] = None, **kw):
        """
        Update VPN group

        :param id: VPN group Id
        :param payload: VPN group
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/admin/vpngroup/{id}", params=params, payload=payload, **kw
        )

    def delete_vpn_group(self, id: str, **kw):
        """
        Delete VPN group

        :param id: VPN group Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request("DELETE", "/dataservice/admin/vpngroup/{id}", params=params, **kw)
