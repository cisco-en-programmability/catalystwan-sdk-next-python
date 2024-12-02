# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder


class CellularBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_global_vrf_interface_cellular_parcels_for_transport(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get Global VRF Interface Cellular Features for transport Parcel

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular",
            return_type=str,
            params=params,
            **kw,
        )

    def create_global_vrf_interface_cellular_parcel_for_transport(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Global VRF Cellular interface Feature for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param payload: Global VRF Interface Cellular Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_global_vrf_interface_cellular_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vrf_id: str, intf_id: str, **kw
    ) -> str:
        """
        Get Global VRF Cellular interface Feature by intfId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param intf_id: Cellular Interface Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "intfId": intf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_global_vrf_interface_cellular_parcel_for_transport(
        self, transport_id: str, vrf_id: str, intf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Global VRF Cellular Interface Feature for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param intf_id: Cellular Interface Parcel ID
        :param payload: Global VRF Cellular Interface Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "intfId": intf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_global_vrf_interface_cellular_for_transport(
        self, transport_id: str, vrf_id: str, intf_id: str, **kw
    ):
        """
        Delete a Global VRF Cellular interface Feature for transport feature profile

        :param transport_id: Feature Profile ID
        :param vrf_id: Global VRF Profile ID
        :param intf_id: Cellular Interface Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "intfId": intf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}",
            params=params,
            **kw,
        )

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
