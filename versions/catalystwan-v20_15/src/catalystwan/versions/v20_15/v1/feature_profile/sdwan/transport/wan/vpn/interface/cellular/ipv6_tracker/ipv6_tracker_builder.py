# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class Ipv6TrackerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcels_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceCellular associated IPv6 Tracker Parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker",
            return_type=str,
            params=params,
            **kw,
        )

    def get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, ipv6_tracker_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceCellular associated IPv6 Tracker Parcel by ipv6-trackerId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param ipv6_tracker_id: Tracker Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
            "ipv6-trackerId": ipv6_tracker_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport(self):
        class edit_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                cellular_id: str,
                ipv6_tracker_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a WanVpnInterfaceCellular parcel and a IPv6 Tracker Parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param cellular_id: Interface Profile Parcel ID
                :param ipv6_tracker_id: Tracker ID
                :param payload: IPv6 Tracker Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "cellularId": cellular_id,
                    "ipv6-trackerId": ipv6_tracker_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}",
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

        return edit_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport_(self._request_adapter)

    def delete_wan_vpn_interface_cellular_and_ipv6_tracker_association_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, ipv6_tracker_id: str, **kw
    ):
        """
        Delete a WanVpnInterfaceCellular and a IPv6 Tracker Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param ipv6_tracker_id: Tracker Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
            "ipv6-trackerId": ipv6_tracker_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}",
            params=params,
            **kw,
        )

    @property
    def create_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport(self):
        class create_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, vpn_parcel_id: str, cellular_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a WanVpnInterfaceCellular parcel with a IPv6 Tracker Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_parcel_id: VPN Profile Parcel ID
                :param cellular_id: Interface Profile Parcel ID
                :param payload: Tracker Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnParcelId": vpn_parcel_id,
                    "cellularId": cellular_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/ipv6-tracker",
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

        return create_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport_(
            self._request_adapter
        )
