# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class OvsnetworkBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks/ovsnetwork
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_nfvirtual_ovs_networks_feature_profile_by_profile_id(
        self, network_id: str, details: bool, **kw
    ) -> Any:
        """
        Get all Nfvirtual OVS Networks Feature Profile with networkId

        :param network_id: Feature Profile Id
        :param details: get feature details
        :returns: Any
        """
        params = {
            "networkId": network_id,
            "details": details,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/ovsnetwork/{networkId}",
            params=params,
            **kw,
        )

    def create_nfvirtual_ovs_network_parcel(
        self, networks_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create OVS Network Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param payload: OVS Network Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_ovs_network_parcel(self, networks_id: str, ovs_network_id: str, **kw) -> str:
        """
        Get OVS Network Profile Parcels for Networks feature profile

        :param networks_id: Feature Profile ID
        :param ovs_network_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "ovsNetworkId": ovs_network_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_ovs_network_parcel(
        self, networks_id: str, ovs_network_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a OVS Network Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param ovs_network_id: Profile Parcel ID
        :param payload: OVS Network Profile Parcel
        :returns: str
        """
        params = {
            "networksId": networks_id,
            "ovsNetworkId": ovs_network_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_ovs_network_parcel(self, networks_id: str, ovs_network_id: str, **kw):
        """
        Delete a OVS Network Profile Parcel for Networks feature profile

        :param networks_id: Feature Profile ID
        :param ovs_network_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "networksId": networks_id,
            "ovsNetworkId": ovs_network_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}",
            params=params,
            **kw,
        )
