# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class WanBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/{networksId}/wan
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_wan_parcel(
        self, networks_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a WAN Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param payload: WAN config Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_wan_parcel(self, networks_id: str, wan_id: str, **kw) -> str:
        """
        Get WAN Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param wan_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "wanId": wan_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_wan_parcel(
        self, networks_id: str, wan_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a WAN Profile Parcel for networks feature profile

        :param networks_id: Feature Profile ID
        :param wan_id: Profile Parcel ID
        :param payload: WAN Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "wanId": wan_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_wan_parcel(self, networks_id: str, wan_id: str, **kw):
        """
        Delete a WAN Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param wan_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "wanId": wan_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}",
            params=params,
            **kw,
        )
