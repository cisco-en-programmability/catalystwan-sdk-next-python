# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class RoutesBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/{networksId}/routes
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_routes_parcel(
        self, networks_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create Routes Profile config for Networks feature profile

        :param networks_id: Feature Profile ID
        :param payload: Routes config Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_routes_parcel(self, networks_id: str, routes_id: str, **kw) -> str:
        """
        Get Routes Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param routes_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "routesId": routes_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_routes_parcel(
        self, networks_id: str, routes_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a Routes Profile Parcel for networks feature profile

        :param networks_id: Feature Profile ID
        :param routes_id: Profile Parcel ID
        :param payload: Routes Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "routesId": routes_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_routes_parcel(self, networks_id: str, routes_id: str, **kw):
        """
        Delete Routes Profile config for Networks feature profile

        :param networks_id: Feature Profile ID
        :param routes_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "routesId": routes_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}",
            params=params,
            **kw,
        )
