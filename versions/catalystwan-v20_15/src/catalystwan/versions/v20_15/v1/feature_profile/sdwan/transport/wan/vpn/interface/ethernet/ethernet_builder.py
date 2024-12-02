# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder
    from .ipv6_tracker.ipv6_tracker_builder import Ipv6TrackerBuilder
    from .ipv6_trackergroup.ipv6_trackergroup_builder import Ipv6TrackergroupBuilder
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/wan/vpn/interface/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interface_ethernet_parcels_for_transport_wan_vpn(
        self, transport_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get InterfaceEthernet Parcels for transport WanVpn Parcel

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_wan_vpn_interface_ethernet_parcel_for_transport(self):
        class create_wan_vpn_interface_ethernet_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Create a WanVpn InterfaceEthernet parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param payload: Wan Vpn Interface Ethernet Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_wan_vpn_interface_ethernet_parcel_for_transport_(
            self._request_adapter
        )

    def get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get WanVpn InterfaceEthernet Parcel by ethernetId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wan_vpn_interface_ethernet_parcel_for_transport(self):
        class edit_wan_vpn_interface_ethernet_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                ethernet_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a WanVpn InterfaceEthernet Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ethernet_id: Interface ID
                :param payload: Wan Vpn Interface Ethernet Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "ethernetId": ethernet_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_wan_vpn_interface_ethernet_parcel_for_transport_(
            self._request_adapter
        )

    def delete_wan_vpn_interface_ethernet_for_transport(
        self, transport_id: str, vpn_id: str, ethernet_id: str, **kw
    ):
        """
        Delete a  WanVpn InterfaceEthernet Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}",
            params=params,
            **kw,
        )

    @property
    def ipv6_tracker(self) -> Ipv6TrackerBuilder:
        """
        The ipv6-tracker property
        """
        from .ipv6_tracker.ipv6_tracker_builder import Ipv6TrackerBuilder

        return Ipv6TrackerBuilder(self._request_adapter)

    @property
    def ipv6_trackergroup(self) -> Ipv6TrackergroupBuilder:
        """
        The ipv6-trackergroup property
        """
        from .ipv6_trackergroup.ipv6_trackergroup_builder import Ipv6TrackergroupBuilder

        return Ipv6TrackergroupBuilder(self._request_adapter)

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
