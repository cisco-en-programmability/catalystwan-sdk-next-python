# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_interface_cellular_associated_tracker_group_parcels_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceCellular associated Tracker Group Parcels for transport feature profile

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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def get_wan_vpn_interface_cellular_associated_tracker_group_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, tracker_group_id: str, **kw
    ) -> str:
        """
        Get WanVpnInterfaceCellular associated Tracker Group Parcel by trackerId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param tracker_group_id: Tracker Group Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
            "trackerGroupId": tracker_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_wan_vpn_interface_cellular_and_tracker_group_parcel_association_for_transport(
        self,
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        tracker_group_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a WanVpnInterfaceCellular parcel and a Tracker Group Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param tracker_group_id: Tracker Group ID
        :param payload: Tracker Group Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
            "trackerGroupId": tracker_group_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_wan_vpn_interface_cellular_and_tracker_group_association_for_transport(
        self, transport_id: str, vpn_id: str, cellular_id: str, tracker_group_id: str, **kw
    ):
        """
        Delete a WanVpnInterfaceCellular and a Tracker Group Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param tracker_group_id: Tracker Group Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "cellularId": cellular_id,
            "trackerGroupId": tracker_group_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}",
            params=params,
            **kw,
        )

    def create_wan_vpn_interface_cellular_and_tracker_group_parcel_association_for_transport(
        self,
        transport_id: str,
        vpn_parcel_id: str,
        cellular_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Associate a WanVpnInterfaceCellular parcel with a TrackerGroup Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_parcel_id: VPN Profile Parcel ID
        :param cellular_id: Interface Profile Parcel ID
        :param payload: TrackerGroup Profile Parcel Id
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnParcelId": vpn_parcel_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/trackergroup",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )
