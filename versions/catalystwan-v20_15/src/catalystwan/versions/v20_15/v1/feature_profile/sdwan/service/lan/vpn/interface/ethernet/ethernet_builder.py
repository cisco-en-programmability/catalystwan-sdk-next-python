# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder
    from .schema.schema_builder import SchemaBuilder
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn/interface/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interface_ethernet_parcels_for_service_lan_vpn(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get InterfaceEthernet Parcels for service LanVpn Parcel

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
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    def create_lan_vpn_interface_ethernet_parcel_for_service(
        self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a LanVpn InterfaceEthernet parcel for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param payload: Lan Vpn Interface Ethernet Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get LanVpn InterfaceEthernet Parcel by ethernetId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_lan_vpn_interface_ethernet_parcel_for_service(
        self, service_id: str, vpn_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a LanVpn InterfaceEthernet Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface ID
        :param payload: Lan Vpn Interface Ethernet Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_lan_vpn_interface_ethernet_for_service(
        self, service_id: str, vpn_id: str, ethernet_id: str, **kw
    ):
        """
        Delete a  LanVpn InterfaceEthernet Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
            params=params,
            **kw,
        )

    @property
    def dhcp_server(self) -> DhcpServerBuilder:
        """
        The dhcp-server property
        """
        from .dhcp_server.dhcp_server_builder import DhcpServerBuilder

        return DhcpServerBuilder(self._request_adapter)

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)

    @property
    def tracker(self) -> TrackerBuilder:
        """
        The tracker property
        """
        from .tracker.tracker_builder import TrackerBuilder

        return TrackerBuilder(self._request_adapter)

    @property
    def trackergroup(self) -> TrackergroupBuilder:
        """
        The trackergroup property
        """
        from .trackergroup.trackergroup_builder import TrackergroupBuilder

        return TrackergroupBuilder(self._request_adapter)
