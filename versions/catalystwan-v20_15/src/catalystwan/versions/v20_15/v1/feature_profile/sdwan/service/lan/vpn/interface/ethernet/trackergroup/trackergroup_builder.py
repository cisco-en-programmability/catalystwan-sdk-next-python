# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_interface_ethernet_associated_tracker_group_parcels_for_transport(
        self, service_id: str, vpn_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get LanVpnInterfaceEthernet associated TrackerGroup Parcels for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def get_lan_vpn_interface_ethernet_associated_tracker_group_parcel_by_parcel_id_for_transport(
        self, service_id: str, vpn_id: str, ethernet_id: str, trackergroup_id: str, **kw
    ) -> str:
        """
        Get LanVpnInterfaceEthernet associated TrackerGroup Parcel by trackergroupId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param trackergroup_id: TrackerGroup Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport(self):
        class edit_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                ethernet_id: str,
                trackergroup_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LanVpnInterfaceEthernet parcel and a TrackerGroup Parcel association for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ethernet_id: Interface Profile Parcel ID
                :param trackergroup_id: TrackerGroup ID
                :param payload: TrackerGroup Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "ethernetId": ethernet_id,
                    "trackergroupId": trackergroup_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}",
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

        return edit_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport_(
            self._request_adapter
        )

    def delete_lan_vpn_interface_ethernet_and_tracker_group_association_for_transport(
        self, service_id: str, vpn_id: str, ethernet_id: str, trackergroup_id: str, **kw
    ):
        """
        Delete a LanVpnInterfaceEthernet and a TrackerGroup Parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ethernet_id: Interface Profile Parcel ID
        :param trackergroup_id: TrackerGroup Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ethernetId": ethernet_id,
            "trackergroupId": trackergroup_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}",
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport(self):
        class create_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_parcel_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a LanVpnInterfaceEthernet parcel with a TrackerGroup Parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_parcel_id: VPN Profile Parcel ID
                :param ethernet_id: Interface Profile Parcel ID
                :param payload: TrackerGroup Profile Parcel Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnParcelId": vpn_parcel_id,
                    "ethernetId": ethernet_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/trackergroup",
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

        return create_lan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport_(
            self._request_adapter
        )
