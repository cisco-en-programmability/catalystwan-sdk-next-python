# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class TrackergroupBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_global_vrf_interface_cellular_associated_tracker_parcels_for_transport(
        self, transport_id: str, vrf_id: str, cellular_id: str, **kw
    ) -> str:
        """
        Get GlobalVRFInterfaceCellular associated Tracker Group Features for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param cellular_id: Cellular Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup",
            return_type=str,
            params=params,
            **kw,
        )

    def create_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport(
        self, transport_id: str, vrf_id: str, cellular_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a GlobalVRFInterfaceCellular feature with a Tracker Group Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param cellular_id: Cellular Interface Profile Parcel ID
        :param payload: Tracker Profile Parcel Id
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "cellularId": cellular_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_global_vrf_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str, **kw
    ) -> str:
        """
        Get GlobalVRFInterfaceCellular associated Tracker Group Feature by trackerId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param cellular_id: Cellular Interface Profile Parcel ID
        :param tracker_id: Tracker Group Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "cellularId": cellular_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport(
        self,
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        tracker_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a GlobalVRFInterfaceCellular feature and a Tracker Group Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param cellular_id: Cellular Interface Profile Parcel ID
        :param tracker_id: Tracker ID
        :param payload: Tracker Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "cellularId": cellular_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_global_vrf_interface_cellular_and_tracker_association_for_transport(
        self, transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str, **kw
    ):
        """
        Delete a GlobalVRFInterfaceCellular and a Tracker Group Feature association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param cellular_id: Cellular Interface Profile Parcel ID
        :param tracker_id: Tracker Group Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "cellularId": cellular_id,
            "trackerId": tracker_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}",
            params=params,
            **kw,
        )
