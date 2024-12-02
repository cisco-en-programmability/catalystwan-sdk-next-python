# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class TrackerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_interface_gre_associated_tracker_parcels_for_transport(
        self, transport_id: str, vpn_id: str, gre_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceGre associated Tracker Parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :param gre_id: Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "greId": gre_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport(self):
        class create_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                gre_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Associate a WanVpnInterfaceGre parcel with a Tracker Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: VPN Profile Parcel ID
                :param gre_id: Interface Profile Parcel ID
                :param payload: Tracker Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "greId": gre_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker",
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

        return (
            create_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport_(
                self._request_adapter
            )
        )

    def get_wan_vpn_interface_gre_associated_tracker_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, gre_id: str, tracker_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceGre associated Tracker Parcel by trackerId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param gre_id: Interface Profile Parcel ID
        :param tracker_id: Tracker Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "greId": gre_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport(self):
        class edit_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                gre_id: str,
                tracker_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a WanVpnInterfaceGre parcel and a Tracker Parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param gre_id: Interface Profile Parcel ID
                :param tracker_id: Tracker ID
                :param payload: Tracker Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "greId": gre_id,
                    "trackerId": tracker_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}",
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

        return edit_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport_(
            self._request_adapter
        )

    def delete_wan_vpn_interface_gre_and_tracker_association_for_transport(
        self, transport_id: str, vpn_id: str, gre_id: str, tracker_id: str, **kw
    ):
        """
        Delete a WanVpnInterfaceGre and a Tracker Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param gre_id: Interface Profile Parcel ID
        :param tracker_id: Tracker Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "greId": gre_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}",
            params=params,
            **kw,
        )
