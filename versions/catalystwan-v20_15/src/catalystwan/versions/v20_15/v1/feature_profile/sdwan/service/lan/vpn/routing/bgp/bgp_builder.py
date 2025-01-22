# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class BgpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_associated_routing_bgp_parcels_for_service(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get LanVpn associated Routing Bgp Parcels for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_lan_vpn_and_routing_bgp_parcel_association_for_service(
        self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a lanvpn parcel with a routingbgp Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Lan Vpn Profile Parcel ID
        :param payload: Routing Bgp Profile Parcel Id
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, bgp_id: str, **kw
    ) -> str:
        """
        Get LanVpn parcel associated RoutingBgp Parcel by bgpId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param bgp_id: Routing Bgp Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_lan_vpn_and_routing_bgp_parcel_association_for_service(
        self, service_id: str, vpn_id: str, bgp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param bgp_id: Routing Bgp ID
        :param payload: Routing Bgp Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_lan_vpn_and_routing_bgp_association_for_service(
        self, service_id: str, vpn_id: str, bgp_id: str, **kw
    ):
        """
        Delete a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param bgp_id: Routing Bgp Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}",
            params=params,
            **kw,
        )
