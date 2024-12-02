# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class Ipv6TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_interface_ethernet_associated_ipv6_tracker_group_parcels_for_transport(
        self, transport_id: str, vpn_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceEthernet associated IPv6 TrackerGroup Parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def get_wan_vpn_interface_ethernet_associated_ipv6_tracker_group_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, ethernet_id: str, ipv6_trackergroup_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceEthernet associated IPv6 TrackerGroup Parcel by ipv6-trackergroupId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param ipv6_trackergroup_id: TrackerGroup Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
            "ipv6-trackergroupId": ipv6_trackergroup_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_wan_vpn_interface_ethernet_and_ipv6_tracker_group_parcel_association_for_transport(
        self,
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        ipv6_trackergroup_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a WanVpnInterfaceEthernet parcel and a IPv6 TrackerGroup Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param ipv6_trackergroup_id: TrackerGroup ID
        :param payload: IPv6 TrackerGroup Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
            "ipv6-trackergroupId": ipv6_trackergroup_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_wan_vpn_interface_ethernet_and_ipv6_tracker_group_association_for_transport(
        self, transport_id: str, vpn_id: str, ethernet_id: str, ipv6_trackergroup_id: str, **kw
    ):
        """
        Delete a WanVpnInterfaceEthernet and a IPv6 TrackerGroup Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param ipv6_trackergroup_id: TrackerGroup Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
            "ipv6-trackergroupId": ipv6_trackergroup_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}",
            params=params,
            **kw,
        )

    def create_wan_vpn_interface_ethernet_and_ipv6_tracker_group_parcel_association_for_transport(
        self,
        transport_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Associate a WanVpnInterfaceEthernet parcel with a IPv6 TrackerGroup Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_parcel_id: VPN Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param payload: IPv6 TrackerGroup Profile Parcel Id
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnParcelId": vpn_parcel_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/ipv6-trackergroup",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )
